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

            // Category badge
            const catBadge = ev.category ? `<span class="badge bg-secondary ms-2" style="font-size:0.6rem;text-transform:uppercase;letter-spacing:0.05em;">${ev.category}</span>` : "";

            item.innerHTML = `
                <div class="d-flex align-items-start gap-3">
                    <div class="rs-timeline-year">${yearLabel}</div>
                    <div class="flex-grow-1">
                        <h6 class="rs-timeline-title">
                            ${ev.title}${statusBadge(ev.evidence_status)}${catBadge}
                        </h6>
                        <p class="rs-timeline-desc">${ev.description}</p>
                        ${ev.location ? `<p class="rs-timeline-location"><i class="fa-solid fa-location-dot me-1"></i>${ev.location}</p>` : ""}
                        ${ev.people && ev.people.length ? `<p class="rs-timeline-people"><i class="fa-solid fa-user me-1"></i>${ev.people.join(", ")}</p>` : ""}
                        ${ev.attribution ? `<p class="rs-timeline-attribution">${ev.attribution}</p>` : ""}
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
                            ${v.coordinates ? `<button class="btn btn-sm rs-card-map-btn" data-venue-id="${v.id}" aria-label="Ver ${v.name} en el mapa" style="border:1px solid var(--rs-gold);color:var(--rs-gold);border-radius:20px;font-size:0.78rem;background:transparent;cursor:pointer;"><i class="fa-solid fa-map-location-dot me-1"></i>Ver en mapa</button>` : ""}
                            ${v.whatsapp_url ? `<a href="${v.whatsapp_url}" target="_blank" rel="noopener" class="btn btn-sm" style="border:1px solid #25d366;color:#25d366;border-radius:20px;font-size:0.78rem;"><i class="fa-brands fa-whatsapp me-1"></i>WhatsApp</a>` : ""}
                            ${v.external_links?.google_maps ? `<a href="${v.external_links.google_maps}" target="_blank" rel="noopener" class="btn btn-sm" style="border:1px solid var(--rs-muted);color:var(--rs-muted);border-radius:20px;font-size:0.78rem;"><i class="fa-solid fa-map me-1"></i>Google Maps</a>` : ""}
                            ${v.website ? `<a href="${v.website}" target="_blank" rel="noopener" class="btn btn-sm" style="border:1px solid var(--rs-muted);color:var(--rs-muted);border-radius:20px;font-size:0.78rem;"><i class="fa-solid fa-globe me-1"></i>Web</a>` : ""}
                            ${v.id === "son-havana" ? `<a href="/son-havana" class="btn btn-sm" style="border:1px solid var(--rs-gold);color:var(--rs-gold);border-radius:20px;font-size:0.78rem;"><i class="fa-solid fa-arrow-right me-1"></i>Ver más</a>` : ""}
                        </div>
                    </div>
                </div>
            `;
            c.appendChild(col);
        });

        // Add "Ver en mapa" click handlers
        document.querySelectorAll(".rs-card-map-btn").forEach(btn => {
            btn.addEventListener("click", function () {
                const venueId = this.dataset.venueId;
                focusMapOnVenue(venueId);
            });
        });
    }

    function focusMapOnVenue(venueId) {
        if (!window._rsMap || !window._rsMarkers) return;

        const marker = window._rsMarkers.find(m => m._venueId === venueId);
        if (!marker) return;

        // Scroll to map
        const mapSection = document.getElementById("rs-map-section");
        if (mapSection) {
            mapSection.scrollIntoView({ behavior: "smooth", block: "start" });
        }

        // Open popup after scroll
        setTimeout(() => {
            window._rsMap.setView(marker.getLatLng(), 16, { animate: true });
            marker.openPopup();
        }, 400);
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

        // Category-based marker colors
        const categoryColors = {
            bar: "#ffc107",
            club: "#ffc107",
            discoteca: "#ffc107",
            restaurante: "#ffc107",
            default: "#ffc107",
        };

        const markers = [];
        venues.forEach(v => {
            if (!v.coordinates) return;
            const color = categoryColors[v.type] || categoryColors.default;
            const icon = L.divIcon({
                className: "rs-marker",
                html: `<div style="width:16px;height:16px;background:${color};border:2.5px solid #000;border-radius:50%;box-shadow:0 0 10px ${color}80;"></div>`,
                iconSize: [16, 16],
                iconAnchor: [8, 8],
            });

            const m = L.marker([v.coordinates.lat, v.coordinates.lng], { icon }).addTo(map);

            // Enhanced popup content
            let popupHtml = `<strong>${v.name}</strong>`;
            if (v.type) {
                popupHtml += `<div class="rs-popup-type">${v.type}</div>`;
            }
            popupHtml += `<div class="rs-popup-addr"><i class="fa-solid fa-location-dot me-1" style="color:var(--rs-gold)"></i>${v.address}</div>`;
            if (v.music_style) {
                popupHtml += `<div class="rs-popup-style">${v.music_style}</div>`;
            }
            popupHtml += `<div class="rs-popup-actions">`;
            if (v.whatsapp_url) {
                popupHtml += `<a href="${v.whatsapp_url}" target="_blank" rel="noopener" class="rs-popup-btn rs-popup-btn-gold"><i class="fa-brands fa-whatsapp me-1"></i>WhatsApp</a>`;
            }
            if (v.external_links?.google_maps) {
                popupHtml += `<a href="${v.external_links.google_maps}" target="_blank" rel="noopener" class="rs-popup-btn rs-popup-btn-outline"><i class="fa-solid fa-map me-1"></i>Mapa</a>`;
            }
            if (v.website) {
                popupHtml += `<a href="${v.website}" target="_blank" rel="noopener" class="rs-popup-btn rs-popup-btn-outline"><i class="fa-solid fa-globe me-1"></i>Web</a>`;
            }
            if (v.id === "son-havana") {
                popupHtml += `<a href="/son-havana" class="rs-popup-btn rs-popup-btn-outline"><i class="fa-solid fa-arrow-right me-1"></i>Ver más</a>`;
            }
            popupHtml += `</div>`;

            m.bindPopup(popupHtml, { maxWidth: 280, minWidth: 200 });
            m._venueId = v.id;
            markers.push(m);
        });

        // Polyline estática conectando los 3 lugares en route_order (Fase 5C.1)
        const routeVenues = venues
            .filter(v => v.route_order != null && v.coordinates)
            .sort((a, b) => a.route_order - b.route_order);
        let routePolyline = null;
        if (routeVenues.length >= 2) {
            const latLngs = routeVenues.map(v => [v.coordinates.lat, v.coordinates.lng]);
            routePolyline = L.polyline(latLngs, {
                color: "#ffc107",
                weight: 3,
                opacity: 0.8,
                className: "rs-route-polyline",
            }).addTo(map);
        }

        if (markers.length) {
            const group = L.featureGroup(markers);
            map.fitBounds(group.getBounds().pad(0.15));
        } else {
            map.setView([6.2477, -75.5910], 14);
        }

        // Store map reference for filter sync
        window._rsMap = map;
        window._rsMarkers = markers;
        window._rsRoutePolyline = routePolyline;
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

                // Sync map markers with filter
                syncMapWithFilter(cat);
            });
        });
    }

    function syncMapWithFilter(category) {
        if (!window._rsMarkers) return;

        // Map only shows venues (physical locations).
        // Show markers only when "all" or "lugares" is selected.
        // Hide markers for other categories (historia, musica, artistas, radio, eventos)
        // since those sections don't have markers on the map.
        const showMarkers = (category === "all" || category === "lugares");

        window._rsMarkers.forEach(marker => {
            marker.setOpacity(showMarkers ? 1 : 0);
        });

        // Polyline de ruta (Fase 5C.1): se añade/remueve del mapa junto con los marcadores
        // (removeLayer/addLayer evita que una polyline oculta intercepte eventos mouse/touch)
        if (window._rsRoutePolyline && window._rsMap) {
            if (showMarkers) {
                if (!window._rsMap.hasLayer(window._rsRoutePolyline)) {
                    window._rsRoutePolyline.addTo(window._rsMap);
                }
            } else {
                if (window._rsMap.hasLayer(window._rsRoutePolyline)) {
                    window._rsMap.removeLayer(window._rsRoutePolyline);
                }
            }
        }
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

    // ── sticky nav (appears when scrolling past hero) ────────────

    function initStickyNav() {
        const stickyNav = document.getElementById("rs-sticky-nav");
        if (!stickyNav) return;

        const hero = document.querySelector(".rs-hero");
        const quickNav = document.querySelector(".rs-quick-nav");
        if (!hero) return;

        const triggerEl = quickNav || hero;
        const pills = stickyNav.querySelectorAll(".rs-sticky-nav-pill");
        const sections = document.querySelectorAll(".rs-section[id]");

        // Show/hide sticky nav on scroll
        const observer = new IntersectionObserver(
            ([entry]) => {
                stickyNav.classList.toggle("is-visible", !entry.isIntersecting);
            },
            { threshold: 0, rootMargin: "-60px 0px 0px 0px" }
        );
        observer.observe(triggerEl);

        // Update active pill on scroll
        const sectionObserver = new IntersectionObserver(
            (entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const id = entry.target.id;
                        pills.forEach(p => {
                            p.classList.toggle("active", p.dataset.section === id);
                        });
                    }
                });
            },
            { threshold: 0.2, rootMargin: "-80px 0px -60% 0px" }
        );

        sections.forEach(sec => sectionObserver.observe(sec));

        // Click to scroll
        pills.forEach(pill => {
            pill.addEventListener("click", function (e) {
                e.preventDefault();
                const target = document.getElementById(this.dataset.section);
                if (target) {
                    target.scrollIntoView({ behavior: "smooth", block: "start" });
                }
            });
        });
    }

    // ── init ─────────────────────────────────────────────────────

    initFilters();
    initSmoothScroll();
    initStickyNav();

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
