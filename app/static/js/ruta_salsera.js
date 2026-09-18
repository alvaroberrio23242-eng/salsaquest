// app/static/js/ruta_salsera.js
// La Ruta Salsera de Medellín — Frontend module
// Fetches /api/ruta-salsera and renders: timeline, venues, map,
// orchestras, radio, labels, events, curiosities, sources.

(function () {
    "use strict";

    const container = document.getElementById("ruta-salsera-section");
    if (!container) return;

    const API = "/api/ruta-salsera";

    // --- helpers ---
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
        const colors = {
            VERIFIED_PRIMARY: "success",
            VERIFIED_SECONDARY: "info",
            ATTRIBUTED: "warning",
            PROBABLE: "secondary",
            PENDING: "secondary",
            CONTRADICTED: "danger",
        };
        return `<span class="badge bg-${colors[status] || "secondary"} ms-2" style="font-size:0.7rem">${status}</span>`;
    }

    // --- renderers ---

    function renderIntro(meta) {
        const intro = document.getElementById("ruta-intro");
        if (intro) {
            intro.innerHTML = meta.description;
        }
        const disclaimer = document.getElementById("ruta-disclaimer");
        if (disclaimer) {
            disclaimer.textContent = meta.disclaimer || "";
        }
    }

    function renderTimeline(events) {
        const c = clearSpinner("ruta-timeline-container");
        if (!c || !events.length) return;

        const sorted = [...events].sort((a, b) => {
            const ya = parseInt((a.year_start || "").match(/\d+/)?.[0] || "9999");
            const yb = parseInt((b.year_start || "").match(/\d+/)?.[0] || "9999");
            return ya - yb;
        });

        const timeline = el("div", { className: "timeline-vertical" });

        sorted.forEach(ev => {
            const item = el("div", { className: "timeline-item mb-3" });
            const yearLabel = ev.year_end
                ? `${ev.year_start}–${ev.year_end}`
                : ev.year_start;

            item.innerHTML = `
                <div class="d-flex align-items-start gap-3">
                    <div class="text-warning fw-bold fs-5" style="min-width: 90px;">${yearLabel}</div>
                    <div class="flex-grow-1">
                        <h6 class="text-warning fw-bold mb-1">
                            ${ev.title}${statusBadge(ev.evidence_status)}
                        </h6>
                        <p class="text-light small mb-1">${ev.description}</p>
                        ${ev.attribution ? `<p class="text-secondary small fst-italic mb-0">${ev.attribution}</p>` : ""}
                    </div>
                </div>
            `;
            timeline.appendChild(item);
        });

        c.appendChild(timeline);
    }

    function renderVenues(venues) {
        const c = clearSpinner("ruta-lugares-container");
        if (!c || !venues.length) return;

        venues.forEach(v => {
            const col = el("div", { className: "col-md-4" });
            col.innerHTML = `
                <div class="card h-100" style="background: rgba(30, 27, 38, 0.75); backdrop-filter: blur(10px); border: 1px solid rgba(255, 193, 7, 0.2); border-radius: 1rem;">
                    <div class="card-body">
                        <h6 class="card-title text-warning fw-bold">
                            ${v.name}${v.is_underground ? ' <i class="fa-solid fa-arrow-down ms-1" style="font-size:0.7rem"></i>' : ""}
                        </h6>
                        <p class="text-light small mb-1"><i class="fa-solid fa-location-dot me-1 text-warning"></i>${v.address}</p>
                        ${v.phone ? `<p class="text-light small mb-1"><i class="fa-solid fa-phone me-1 text-warning"></i>${v.phone}</p>` : ""}
                        ${v.operating_hours ? `<p class="text-light small mb-1"><i class="fa-solid fa-clock me-1 text-warning"></i>${v.operating_hours}</p>` : ""}
                        <p class="text-secondary small mb-1"><em>${v.music_style}</em></p>
                        <p class="text-light small">${v.description}</p>
                        ${v.whatsapp_url ? `<a href="${v.whatsapp_url}" target="_blank" rel="noopener" class="btn btn-sm btn-outline-success mt-1"><i class="fa-brands fa-whatsapp me-1"></i>WhatsApp</a>` : ""}
                        ${v.external_links?.google_maps ? `<a href="${v.external_links.google_maps}" target="_blank" rel="noopener" class="btn btn-sm btn-outline-warning mt-1"><i class="fa-solid fa-map me-1"></i>Mapa</a>` : ""}
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

        const map = L.map(mapEl);
        L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
            attribution: '&copy; OpenStreetMap',
            maxZoom: 18,
        }).addTo(map);

        const markers = [];
        venues.forEach(v => {
            if (!v.coordinates) return;
            const m = L.marker([v.coordinates.lat, v.coordinates.lng]).addTo(map);
            m.bindPopup(`<strong>${v.name}</strong><br>${v.address}`);
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
                <div class="card h-100" style="background: rgba(30, 27, 38, 0.75); backdrop-filter: blur(10px); border: 1px solid rgba(255, 193, 7, 0.15); border-radius: 1rem;">
                    <div class="card-body">
                        <h6 class="card-title text-warning fw-bold">${o.name}${statusBadge(o.evidence_status)}</h6>
                        ${o.founding_year ? `<p class="text-light small mb-1"><i class="fa-solid fa-calendar me-1 text-warning"></i>${o.founding_year}</p>` : ""}
                        ${o.label ? `<p class="text-light small mb-1"><i class="fa-solid fa-compact-disc me-1 text-warning"></i>${o.label}</p>` : ""}
                        <p class="text-light small mb-1">${o.contribution}</p>
                        ${o.notable_works.length ? `<p class="text-secondary small mb-0"><em>Obras: ${o.notable_works.join(", ")}</em></p>` : ""}
                        ${o.attribution ? `<p class="text-secondary small fst-italic mt-1 mb-0">${o.attribution}</p>` : ""}
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
                <div class="card h-100" style="background: rgba(30, 27, 38, 0.75); backdrop-filter: blur(10px); border: 1px solid rgba(255, 193, 7, 0.15); border-radius: 1rem;">
                    <div class="card-body">
                        <h6 class="card-title text-warning fw-bold">
                            <i class="fa-solid fa-radio me-1"></i>${r.name}${statusBadge(r.evidence_status)}
                        </h6>
                        <p class="text-light small mb-1"><i class="fa-solid fa-signal me-1 text-warning"></i>${r.frequency}</p>
                        <p class="text-light small mb-1"><em>"${r.slogan}"</em></p>
                        <p class="text-light small mb-0">${r.role}</p>
                        ${r.attribution ? `<p class="text-secondary small fst-italic mt-1 mb-0">${r.attribution}</p>` : ""}
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
                <div class="card h-100" style="background: rgba(30, 27, 38, 0.75); backdrop-filter: blur(10px); border: 1px solid rgba(255, 193, 7, 0.15); border-radius: 1rem;">
                    <div class="card-body">
                        <h6 class="card-title text-warning fw-bold">
                            <i class="fa-solid fa-compact-disc me-1"></i>${l.name}${statusBadge(l.evidence_status)}
                        </h6>
                        <p class="text-light small mb-1"><i class="fa-solid fa-calendar me-1 text-warning"></i>${l.founding_year} — ${l.founding_location}</p>
                        <p class="text-light small mb-0">${l.description}</p>
                        ${l.attribution ? `<p class="text-secondary small fst-italic mt-1 mb-0">${l.attribution}</p>` : ""}
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
                    <h6 class="text-warning fw-bold mb-1">
                        ${ev.title}${statusBadge(ev.evidence_status)}
                    </h6>
                    <p class="text-light small mb-1"><i class="fa-solid fa-calendar me-1 text-warning"></i>${ev.date}</p>
                    <p class="text-light small mb-1"><i class="fa-solid fa-location-dot me-1 text-warning"></i>${ev.location}</p>
                    <p class="text-light small mb-0">${ev.description}</p>
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
                <p class="text-light small mb-1">${item.text}</p>
                ${item.attribution ? `<p class="text-secondary small fst-italic mb-0">${item.attribution}</p>` : ""}
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
                <a href="${s.url}" target="_blank" rel="noopener" class="text-warning text-decoration-none">${s.title}</a>
                <span class="text-secondary ms-1">— ${s.publisher}</span>
                <span class="badge bg-secondary ms-1" style="font-size:0.65rem">Nivel ${s.source_level}</span>
            `;
            c.appendChild(div);
        });
    }

    // --- init ---
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
                intro.innerHTML = '<span class="text-danger">Error al cargar datos. Intenta de nuevo más tarde.</span>';
            }
        });
})();
