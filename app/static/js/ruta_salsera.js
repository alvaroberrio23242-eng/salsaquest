// app/static/js/ruta_salsera.js
// La Ruta Salsera de Medellín — Professional Product Module
// Fetches /api/ruta-salsera and renders: timeline, venues, map,
// orchestras, radio, labels, events, curiosities, sources.
// Adds: category filtering, smooth scroll, enhanced map popups.

(function () {
    "use strict";

    const container = document.getElementById("ruta-salsera-section");
    if (!container) return;

    const API = "/api/ruta-salsera";

    // ── helpers ──────────────────────────────────────────────────
    function el(tag, attrs, ...children) {
        const e = document.createElement(tag);
        if (attrs) Object.entries(attrs).forEach(([k, v]) => {
            if (k === "className") e.className = v;
            else if (k === "innerHTML") e.innerHTML = v;
            else e.setAttribute(k, v);
        });
        children.forEach(c => {
            if (typeof c === "string") e.appendChild(document.createTextNode(c));
            else if (c) e.appendChild(c);
        });
        return e;
    }

    function clearSpinner(id) {
        const c = document.getElementById(id);
        if (c) c.innerHTML = "";
        return c;
    }

    function statusBadge(status) {
        const map = {
            VERIFIED_PRIMARY:   { cls: "success",   label: "Verificado" },
            VERIFIED_SECONDARY: { cls: "info",      label: "Verificado" },
            ATTRIBUTED:         { cls: "warning",   label: "Atribuido" },
            PROBABLE:           { cls: "secondary",  label: "Probable" },
            PENDING:            { cls: "secondary",  label: "Pendiente" },
            CONTRADICTED:       { cls: "danger",    label: "Contradictado" },
            NEEDS_REVIEW:       { cls: "warning",   label: "Revisar" },
            UNVERIFIED:         { cls: "secondary",  label: "No verificado" },
        };
        const info = map[status] || { cls: "secondary", label: status };
        return `<span class="badge bg-${info.cls} ms-2" style="font-size:0.65rem">${info.label}</span>`;
    }

    // ── renderers ────────────────────────────────────────────────

    function renderIntro(meta) {
        const intro = document.getElementById("ruta-intro");
        if (intro) intro.textContent = meta.description;
        const disclaimer = document.getElementById("ruta-disclaimer");
        if (disclaimer) disclaimer.textContent = meta.disclaimer || "";
    }

    function renderTimeline(events) {
        const c = clearSpinner("ruta-timeline-container");
        if (!c || !events.length) return;

        const sorted = [...events].sort((a, b) => {
            const ya = parseInt((a.year_start || "").match(/\d+/)?.[0] || "9999");
            const yb = parseInt((b.year_start || "").match(/\d+/)?.[0] || "9999");
            return ya - yb;
        });

        const wrap = el("div", { className: "rs-timeline" });

        sorted.forEach(ev => {
            const item = el("div", { className: "timeline-item" });
            const yearLabel = ev.year_end
                ? `${ev.year_start} – ${ev.year_end}`
                : ev.year_start;

            item.innerHTML = `
                <div class="d-flex align-items-start gap-3">
                    <div class="text-warning fw-bold" style="min-width:85px;font-size:0.95rem;">${yearLabel}</div>
                    <div class="flex-grow-1">
                        <h6 class="text-warning fw-bold mb-1" style="font-family:'Fraunces',serif;font-size:1rem;">
                            ${ev.title}${statusBadge(ev.evidence_status)}
                        </h6>
                        <p class="small mb-1" style="color:var(--rs-muted);line-height:1.6;">${ev.description}</p>
                        ${ev.attribution ? `<p class="small fst-italic mb-0" style="color:#7a7590;font-size:0.78rem;">${ev.attribution}</p>` : ""}
                    </div>
                </div>
            `;
            wrap.appendChild(item);
        });

        c.appendChild(wrap);
    }

    function renderVenues(venues) {
        const c = clearSpinner("ruta-lugares-container");
        if (!c || !venues.length) return;

        venues.forEach(v => {
            const col = el("div", { className: "col-md-4 col-sm-6" });
            col.innerHTML = `
                <div class="card h-100">
                    <div class="card-body">
                        <h6 class="card-title fw-bold" style="font-family:'Fraunces',serif;">
                            ${v.name}${v.is_underground ? ' <i class="fa-solid fa-arrow-down ms-1" style="font-size:0.65rem;opacity:0.6"></i>' : ""}${statusBadge(v.evidence_status)}
                        </h6>
                        <p class="small mb-1" style="color:var(--rs-text);">
                            <i class="fa-solid fa-location-dot me-1" style="color:var(--rs-gold)"></i>${v.address}
                        </p>
                        ${v.phone ? `<p class="small mb-1" style="color:var(--rs-text);"><i class="fa-solid fa-phone me-1" style="color:var(--rs-gold)"></i>${v.phone}</p>` : ""}
                        ${v.operating_hours ? `<p class="small mb-1" style="color:var(--rs-text);"><i class="fa-solid fa-clock me-1" style="color:var(--rs-gold)"></i>${v.operating_hours}</p>` : ""}
                        <p class="small mb-1" style="color:var(--rs-muted);font-style:italic;">${v.music_style}</p>
                        <p class="small mb-2" style="color:var(--rs-muted);line-height:1.55;">${v.description}</p>
                        <div class="d-flex gap-2 flex-wrap">
                            ${v.whatsapp_url ? `<a href="${v.whatsapp_url}" target="_blank" rel="noopener" class="btn btn-sm" style="border:1px solid #25d366;color:#25d366;border-radius:20px;font-size:0.78rem;"><i class="fa-brands fa-whatsapp me-1"></i>WhatsApp</a>` : ""}
                            ${v.external_links?.google_maps ? `<a href="${v.external_links.google_maps}" target="_blank" rel="noopener" class="btn btn-sm" style="border:1px solid var(--rs-gold);color:var(--rs-gold);border-radius:20px;font-size:0.78rem;"><i class="fa-solid fa-map me-1"></i>Mapa</a>` : ""}
                        </div>
                    </div>
                </div>
            `;
            c.appendChild(col);
        });
    }

    function renderMap(venues) {
        if (typeof L === "undefined") return;
        const mapEl = document.getElementById("mapa-ruta-salsera");
        if (!mapEl || !venues.length) return;

        const map = L.map(mapEl, {
            scrollWheelZoom: false,
            zoomControl: true,
        });

        L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
            attribution: '&copy; <a href="https://openstreetmap.org/copyright">OpenStreetMap</a>',
            maxZoom: 18,
        }).addTo(map);

        const goldIcon = L.divIcon({
            className: "rs-marker",
            html: '<div style="width:14px;height:14px;background:#ffc107;border:2px solid #000;border-radius:50%;box-shadow:0 0 8px rgba(255,193,7,0.5);"></div>',
            iconSize: [14, 14],
            iconAnchor: [7, 7],
        });

        const markers = [];
        venues.forEach(v => {
            if (!v.coordinates) return;
            const m = L.marker([v.coordinates.lat, v.coordinates.lng], { icon: goldIcon }).addTo(map);
            m.bindPopup(`
                <strong>${v.name}</strong><br>
                <span style="color:#a09abc;font-size:0.82rem;">${v.address}</span>
                ${v.music_style ? `<br><span style="color:#ffc107;font-size:0.78rem;font-style:italic;">${v.music_style}</span>` : ""}
            `, { maxWidth: 240 });
            markers.push(m);
        });

        if (markers.length) {
            const group = L.featureGroup(markers);
            map.fitBounds(group.getBounds().pad(0.15));
        } else {
            map.setView([6.2477, -75.5910], 14);
        }
    }

    function renderOrchestras(orchestras) {
        const c = clearSpinner("ruta-orquestas-container");
        if (!c || !orchestras.length) return;

        orchestras.forEach(o => {
            const col = el("div", { className: "col-md-4 col-sm-6" });
            col.innerHTML = `
                <div class="card h-100">
                    <div class="card-body">
                        <h6 class="card-title fw-bold" style="font-family:'Fraunces',serif;">
                            ${o.name}${statusBadge(o.evidence_status)}
                        </h6>
                        ${o.founding_year ? `<p class="small mb-1" style="color:var(--rs-text);"><i class="fa-solid fa-calendar me-1" style="color:var(--rs-gold)"></i>${o.founding_year}</p>` : ""}
                        ${o.label ? `<p class="small mb-1" style="color:var(--rs-text);"><i class="fa-solid fa-compact-disc me-1" style="color:var(--rs-gold)"></i>${o.label}</p>` : ""}
                        <p class="small mb-1" style="color:var(--rs-muted);line-height:1.55;">${o.contribution}</p>
                        ${o.notable_works.length ? `<p class="small mb-0" style="color:#7a7590;font-style:italic;">Obras: ${o.notable_works.join(", ")}</p>` : ""}
                        ${o.attribution ? `<p class="small fst-italic mt-1 mb-0" style="color:#7a7590;font-size:0.75rem;">${o.attribution}</p>` : ""}
                    </div>
                </div>
            `;
            c.appendChild(col);
        });
    }

    function renderRadio(radio) {
        const c = clearSpinner("ruta-radio-container");
        if (!c || !radio.length) return;

        radio.forEach(r => {
            const col = el("div", { className: "col-md-6" });
            col.innerHTML = `
                <div class="card h-100">
                    <div class="card-body">
                        <h6 class="card-title fw-bold" style="font-family:'Fraunces',serif;">
                            <i class="fa-solid fa-radio me-1"></i>${r.name}${statusBadge(r.evidence_status)}
                        </h6>
                        <p class="small mb-1" style="color:var(--rs-text);"><i class="fa-solid fa-signal me-1" style="color:var(--rs-gold)"></i>${r.frequency}</p>
                        <p class="small mb-1" style="color:var(--rs-muted);font-style:italic;">"${r.slogan}"</p>
                        <p class="small mb-0" style="color:var(--rs-muted);">${r.role}</p>
                        ${r.attribution ? `<p class="small fst-italic mt-1 mb-0" style="color:#7a7590;font-size:0.75rem;">${r.attribution}</p>` : ""}
                    </div>
                </div>
            `;
            c.appendChild(col);
        });
    }

    function renderLabels(labels) {
        const c = clearSpinner("ruta-sellos-container");
        if (!c || !labels.length) return;

        labels.forEach(l => {
            const col = el("div", { className: "col-md-6" });
            col.innerHTML = `
                <div class="card h-100">
                    <div class="card-body">
                        <h6 class="card-title fw-bold" style="font-family:'Fraunces',serif;">
                            <i class="fa-solid fa-compact-disc me-1"></i>${l.name}${statusBadge(l.evidence_status)}
                        </h6>
                        <p class="small mb-1" style="color:var(--rs-text);"><i class="fa-solid fa-calendar me-1" style="color:var(--rs-gold)"></i>${l.founding_year} — ${l.founding_location}</p>
                        <p class="small mb-0" style="color:var(--rs-muted);line-height:1.55;">${l.description}</p>
                        ${l.attribution ? `<p class="small fst-italic mt-1 mb-0" style="color:#7a7590;font-size:0.75rem;">${l.attribution}</p>` : ""}
                    </div>
                </div>
            `;
            c.appendChild(col);
        });
    }

    function renderEvents(events) {
        const c = clearSpinner("ruta-eventos-container");
        if (!c || !events.length) return;

        events.forEach(ev => {
            const col = el("div", { className: "col-md-6" });
            col.innerHTML = `
                <div class="ruta-evento-card">
                    <h6 class="fw-bold mb-1" style="color:var(--rs-gold);font-family:'Fraunces',serif;">
                        ${ev.title}${statusBadge(ev.evidence_status)}
                    </h6>
                    <p class="small mb-1" style="color:var(--rs-text);"><i class="fa-solid fa-calendar me-1" style="color:var(--rs-gold)"></i>${ev.date}</p>
                    <p class="small mb-1" style="color:var(--rs-text);"><i class="fa-solid fa-location-dot me-1" style="color:var(--rs-gold)"></i>${ev.location}</p>
                    <p class="small mb-0" style="color:var(--rs-muted);line-height:1.55;">${ev.description}</p>
                </div>
            `;
            c.appendChild(col);
        });
    }

    function renderCuriosidades(items) {
        const c = clearSpinner("ruta-curiosidades-container");
        if (!c || !items.length) return;

        items.forEach(item => {
            const div = el("div", { className: "ruta-curiosidad" });
            div.innerHTML = `
                <p class="small mb-1" style="color:var(--rs-text);line-height:1.6;">${item.text}</p>
                ${item.attribution ? `<p class="small fst-italic mb-0" style="color:#7a7590;font-size:0.78rem;">${item.attribution}</p>` : ""}
            `;
            c.appendChild(div);
        });
    }

    function renderSources(sources) {
        const c = clearSpinner("ruta-fuentes-container");
        if (!c || !sources) return;

        Object.values(sources).forEach(s => {
            const div = el("div", { className: "ruta-fuente-item" });
            div.innerHTML = `
                <a href="${s.url}" target="_blank" rel="noopener" style="color:var(--rs-gold);text-decoration:none;">${s.title}</a>
                <span style="color:var(--rs-muted);margin-left:0.5rem;">— ${s.publisher}</span>
                <span class="badge bg-secondary ms-1" style="font-size:0.6rem">Nivel ${s.source_level}</span>
            `;
            c.appendChild(div);
        });
    }

    // ── category filter ──────────────────────────────────────────

    function initFilters() {
        const pills = document.querySelectorAll(".rs-filter-pill");
        const sections = document.querySelectorAll(".rs-section[data-cat]");
        if (!pills.length || !sections.length) return;

        pills.forEach(pill => {
            pill.addEventListener("click", function () {
                const cat = this.dataset.category;

                pills.forEach(p => p.classList.remove("active"));
                this.classList.add("active");

                sections.forEach(sec => {
                    if (cat === "all" || sec.dataset.cat === cat || sec.dataset.cat === "all") {
                        sec.classList.remove("rs-hidden");
                    } else {
                        sec.classList.add("rs-hidden");
                    }
                });
            });
        });
    }

    // ── smooth scroll for anchor links ───────────────────────────

    function initSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(link => {
            link.addEventListener("click", function (e) {
                const target = document.querySelector(this.getAttribute("href"));
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({ behavior: "smooth", block: "start" });
                }
            });
        });
    }

    // ── init ─────────────────────────────────────────────────────

    initFilters();
    initSmoothScroll();

    fetch(API)
        .then(r => {
            if (!r.ok) throw new Error(`HTTP ${r.status}`);
            return r.json();
        })
        .then(data => {
            renderIntro(data.meta);
            renderTimeline(data.timeline);
            renderVenues(data.venues);
            renderMap(data.venues);
            renderOrchestras(data.orchestras);
            renderRadio(data.radio);
            renderLabels(data.labels);
            renderEvents(data.events);
            renderCuriosidades(data.curiosidades);
            renderSources(data.sources);
        })
        .catch(err => {
            console.error("Ruta Salsera API error:", err);
            const intro = document.getElementById("ruta-intro");
            if (intro) {
                intro.innerHTML = '<span style="color:#ef3f5d;">Error al cargar datos. Intenta de nuevo más tarde.</span>';
            }
        });
})();
