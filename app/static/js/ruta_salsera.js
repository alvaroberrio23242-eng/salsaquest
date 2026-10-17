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

    function safeText(value, fallback) {
        if (
            value === null ||
            value === undefined ||
            value === "" ||
            value === "None" ||
            value === "null" ||
            value === "undefined"
        ) {
            return fallback;
        }
        return String(value);
    }

    function isEmptyValue(value) {
        return (
            value === null ||
            value === undefined ||
            value === "" ||
            value === "None" ||
            value === "null" ||
            value === "undefined"
        );
    }

    function statusBadge(status) {
        const map = {
            VERIFIED_PRIMARY:       { cls: "success",   label: "Verificado" },
            VERIFIED_SECONDARY:     { cls: "info",      label: "Verificado" },
            ATTRIBUTED:             { cls: "warning",   label: "Atribuido" },
            PROBABLE:               { cls: "secondary",  label: "Probable" },
            PENDING:                { cls: "secondary",  label: "Pendiente" },
            CONTRADICTED:           { cls: "danger",    label: "En disputa" },
            NEEDS_REVIEW:           { cls: "warning",   label: "Revisar" },
            UNVERIFIED:             { cls: "secondary",  label: "No verificado" },
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

    // -- lugares + mapa (panel estilo RockQuest) ------------------
    const esc = v => String(v == null ? "" : v).replace(/[&<>"']/g, ch => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[ch]));
    const safeUrl = u => (/^https?:\/\//i.test(String(u || "")) ? String(u) : "");
    const norm = s => String(s || "").toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
    const hasCoords = v => !!(v.coordinates && typeof v.coordinates.lat === "number" && typeof v.coordinates.lng === "number");

    const TYPE_INFO = {
        bar:         { label: "Bar",         color: "#ffc107" },
        club:        { label: "Club",        color: "#ff4fa3" },
        discoteca:   { label: "Discoteca",   color: "#19e6ff" },
        restaurante: { label: "Restaurante", color: "#ff8a3d" },
    };
    const typeKey = v => String(v.type || "").toLowerCase();
    const typeInfo = v => TYPE_INFO[typeKey(v)] || {
        label: typeKey(v) ? typeKey(v).charAt(0).toUpperCase() + typeKey(v).slice(1).replace(/_/g, " ") : "Lugar",
        color: "#ffc107",
    };
    const routeUrl = v => "https://www.google.com/maps/dir/?api=1&destination=" + v.coordinates.lat + "," + v.coordinates.lng;

    const venueState = { type: "", q: "" };
    const venueMarkers = new Map();
    const venueCards = new Map();
    let allVenues = [];
    let rsMap = null;
    let rsLayer = null;

    function venuePopup(v) {
        const info = typeInfo(v);
        const addr = safeText(v.address, "Dirección pendiente de verificación");
        const mStyle = safeText(v.music_style, "Estilo musical pendiente de verificar");
        const hours = isEmptyValue(v.operating_hours) ? null : v.operating_hours;
        const whatsapp = safeUrl(v.whatsapp_url);
        const gMaps = (v.external_links && !isEmptyValue(v.external_links.google_maps)) ? safeUrl(v.external_links.google_maps) : "";
        const website = safeUrl(v.website);
        let html = "<strong>" + esc(v.name) + "</strong>";
        html += '<div class="rs-popup-type" style="color:' + info.color + '">' + esc(info.label) + "</div>";
        html += '<div class="rs-popup-addr"><i class="fa-solid fa-location-dot me-1" style="color:var(--rs-gold)"></i>' + esc(addr) + "</div>";
        if (hours) html += '<div class="rs-popup-addr"><i class="fa-solid fa-clock me-1" style="color:var(--rs-gold)"></i>' + esc(hours) + "</div>";
        html += '<div class="rs-popup-style">' + esc(mStyle) + "</div>";
        if (v.coords_approx) html += '<div class="rs-popup-style" style="opacity:.7">Ubicaci\u00f3n aproximada (OSM) \u00b7 NO VERIFICADO</div>';
        html += '<div class="rs-popup-actions">';
        if (hasCoords(v)) html += '<a href="' + esc(routeUrl(v)) + '" target="_blank" rel="noopener noreferrer" class="rs-popup-btn rs-popup-btn-gold"><i class="fa-solid fa-route me-1"></i>Cómo llegar</a>';
        if (whatsapp) html += '<a href="' + esc(whatsapp) + '" target="_blank" rel="noopener noreferrer" class="rs-popup-btn rs-popup-btn-outline"><i class="fa-brands fa-whatsapp me-1"></i>WhatsApp</a>';
        if (gMaps) html += '<a href="' + esc(gMaps) + '" target="_blank" rel="noopener noreferrer" class="rs-popup-btn rs-popup-btn-outline"><i class="fa-solid fa-map me-1"></i>Mapa</a>';
        if (website) html += '<a href="' + esc(website) + '" target="_blank" rel="noopener noreferrer" class="rs-popup-btn rs-popup-btn-outline"><i class="fa-solid fa-globe me-1"></i>Web</a>';
        if (v.brand === "son-havana") html += '<a href="/son-havana" class="rs-popup-btn rs-popup-btn-outline"><i class="fa-solid fa-arrow-right me-1"></i>Ver más</a>';
        html += "</div>";
        return html;
    }

    function venueCard(v) {
        const info = typeInfo(v);
        const address = safeText(v.address, "Dirección pendiente de verificación");
        const musicStyle = safeText(v.music_style, "Estilo musical pendiente de verificar");
        const description = safeText(v.description, "Información pendiente de investigación");
        const phone = isEmptyValue(v.phone) ? null : v.phone;
        const hours = isEmptyValue(v.operating_hours) ? null : v.operating_hours;
        const whatsapp = safeUrl(v.whatsapp_url);
        const gMaps = (v.external_links && !isEmptyValue(v.external_links.google_maps)) ? safeUrl(v.external_links.google_maps) : "";
        const website = safeUrl(v.website);
        let statusIndicator = "";
        if (v.status === "closed") statusIndicator = '<span class="badge bg-danger ms-2" style="font-size:0.65rem">Cerrado</span>';
        else if (v.status === "unknown") statusIndicator = '<span class="badge bg-warning ms-2" style="font-size:0.65rem">Estado no confirmado</span>';
        const btn = 'style="border-radius:20px;font-size:0.78rem;"';

        const col = el("div", { className: "col-md-4 col-sm-6" });
        col.innerHTML = `
            <div class="card h-100 rs-place" tabindex="0" style="--c:${info.color}">
                <div class="card-body">
                    <span class="rs-tag">${esc(info.label)}</span>
                    <h6 class="card-title fw-bold" style="font-family:'Fraunces',serif;">
                        ${esc(v.name)}${v.is_underground ? ' <i class="fa-solid fa-arrow-down ms-1" style="font-size:0.65rem;opacity:0.6"></i>' : ""}${statusBadge(v.evidence_status)}${statusIndicator}
                    </h6>
                    <p class="small mb-1" style="color:var(--rs-text);"><i class="fa-solid fa-location-dot me-1" style="color:var(--rs-gold)"></i>${esc(address)}</p>
                    ${phone ? `<p class="small mb-1" style="color:var(--rs-text);"><i class="fa-solid fa-phone me-1" style="color:var(--rs-gold)"></i>${esc(phone)}</p>` : ""}
                    ${hours ? `<p class="small mb-1" style="color:var(--rs-text);"><i class="fa-solid fa-clock me-1" style="color:var(--rs-gold)"></i>${esc(hours)}</p>` : ""}
                    <p class="small mb-1" style="color:var(--rs-muted);font-style:italic;">${esc(musicStyle)}</p>
                    <p class="small mb-2" style="color:var(--rs-muted);line-height:1.55;">${esc(description)}</p>
                    <div class="d-flex gap-2 flex-wrap">
                        ${hasCoords(v) ? `<button type="button" class="btn btn-sm rs-card-map-btn" aria-label="Ver ${esc(v.name)} en el mapa" style="border:1px solid var(--rs-gold);color:var(--rs-gold);border-radius:20px;font-size:0.78rem;background:transparent;cursor:pointer;"><i class="fa-solid fa-map-location-dot me-1"></i>Ver en mapa</button>` : ""}
                        ${hasCoords(v) ? `<a href="${esc(routeUrl(v))}" target="_blank" rel="noopener noreferrer" class="btn btn-sm" ${btn.replace('style="', 'style="border:1px solid var(--rs-gold);color:var(--rs-gold);')}><i class="fa-solid fa-route me-1"></i>Cómo llegar</a>` : ""}
                        ${whatsapp ? `<a href="${esc(whatsapp)}" target="_blank" rel="noopener noreferrer" class="btn btn-sm" ${btn.replace('style="', 'style="border:1px solid #25d366;color:#25d366;')}><i class="fa-brands fa-whatsapp me-1"></i>WhatsApp</a>` : ""}
                        ${gMaps ? `<a href="${esc(gMaps)}" target="_blank" rel="noopener noreferrer" class="btn btn-sm" ${btn.replace('style="', 'style="border:1px solid var(--rs-muted);color:var(--rs-muted);')}><i class="fa-solid fa-map me-1"></i>Google Maps</a>` : ""}
                        ${website ? `<a href="${esc(website)}" target="_blank" rel="noopener noreferrer" class="btn btn-sm" ${btn.replace('style="', 'style="border:1px solid var(--rs-muted);color:var(--rs-muted);')}><i class="fa-solid fa-globe me-1"></i>Web</a>` : ""}
                        ${v.brand === "son-havana" ? `<a href="/son-havana" class="btn btn-sm" ${btn.replace('style="', 'style="border:1px solid var(--rs-gold);color:var(--rs-gold);')}><i class="fa-solid fa-arrow-right me-1"></i>Ver más</a>` : ""}
                    </div>
                </div>
            </div>
        `;
        return col;
    }

    function setActiveVenue(key) {
        venueCards.forEach((col, k) => {
            const card = col.querySelector(".rs-place");
            if (card) card.classList.toggle("is-active", k === key);
        });
    }

    function hotVenue(key, on) {
        const m = venueMarkers.get(key);
        const e = m && m.getElement && m.getElement();
        if (e) e.classList.toggle("rs-pin-hot", on);
    }

    function focusVenue(key) {
        const m = venueMarkers.get(key);
        if (!m || !rsMap) return;
        setActiveVenue(key);
        const mapSection = document.getElementById("rs-map-section");
        if (mapSection) mapSection.scrollIntoView({ behavior: "smooth", block: "start" });
        let opened = false;
        const open = () => { if (opened) return; opened = true; m.openPopup(); };
        rsMap.once("moveend", open);
        setTimeout(open, 1000);
        rsMap.flyTo(m.getLatLng(), Math.max(rsMap.getZoom(), 16), { duration: 0.8 });
    }

    function venueMatches(v) {
        if (venueState.type && typeKey(v) !== venueState.type) return false;
        if (venueState.q && !v._hay.includes(norm(venueState.q))) return false;
        return true;
    }

    function fitVenues(vis) {
        if (!rsMap) return;
        const pts = vis.filter(hasCoords).map(v => [v.coordinates.lat, v.coordinates.lng]);
        rsMap.invalidateSize();
        if (!pts.length) return;
        if (pts.length === 1) rsMap.setView(pts[0], 15);
        else rsMap.fitBounds(L.latLngBounds(pts).pad(0.15), { maxZoom: 15 });
    }

    function renderVenueList(refit) {
        const listEl = document.getElementById("ruta-lugares-container");
        if (!listEl) return;
        const vis = allVenues.filter(venueMatches);
        listEl.textContent = "";
        if (rsLayer) rsLayer.clearLayers();
        vis.forEach(v => {
            listEl.appendChild(venueCards.get(v._k));
            const m = venueMarkers.get(v._k);
            if (m && rsLayer) rsLayer.addLayer(m);
        });
        if (!vis.length) {
            const empty = el("div", { className: "col-12" });
            empty.innerHTML = '<p class="rs-empty">Nada por aquí. Prueba otro filtro.</p>';
            listEl.appendChild(empty);
        }
        const countEl = document.getElementById("rs-count");
        const labelEl = document.getElementById("rs-count-label");
        const resetEl = document.getElementById("rs-reset");
        const statusEl = document.getElementById("rs-map-status");
        if (countEl) countEl.textContent = vis.length;
        if (labelEl) labelEl.textContent = vis.length === 1 ? "lugar" : "lugares";
        if (resetEl) resetEl.hidden = !(venueState.type || venueState.q);
        if (statusEl) { const pins = vis.filter(hasCoords).length; statusEl.textContent = pins + " en el mapa" + (vis.length > pins ? " \u00b7 " + (vis.length - pins) + " sin ubicaci\u00f3n" : "") + " \u00b7 toca un pin o una tarjeta"; }
        document.querySelectorAll("#rs-type-chips .rs-chip").forEach(b => {
            const on = (b.dataset.type || "") === venueState.type;
            b.classList.toggle("on", on);
            b.setAttribute("aria-pressed", String(on));
        });
        if (refit) fitVenues(vis);
    }

    function buildTypeChips() {
        const wrap = document.getElementById("rs-type-chips");
        if (!wrap) return;
        const types = [...new Set(allVenues.map(typeKey).filter(Boolean))].sort();
        wrap.textContent = "";
        if (types.length < 2) { wrap.hidden = true; return; }
        wrap.hidden = false;
        [""].concat(types).forEach(t => {
            const n = allVenues.filter(v => !t || typeKey(v) === t).length;
            const info = t ? (TYPE_INFO[t] || { label: t.charAt(0).toUpperCase() + t.slice(1), color: "#ffc107" }) : { label: "Todos", color: "#ffffff" };
            const b = document.createElement("button");
            b.type = "button";
            b.className = "rs-chip";
            b.dataset.type = t;
            b.setAttribute("aria-pressed", "false");
            b.innerHTML = '<i class="rs-dot" style="--c:' + info.color + '"></i>' + esc(info.label) + ' <em class="rs-n">(' + n + ")</em>";
            wrap.appendChild(b);
        });
    }

    function initVenueControls() {
        const chips = document.getElementById("rs-type-chips");
        const search = document.getElementById("rs-search");
        const reset = document.getElementById("rs-reset");
        if (chips) chips.addEventListener("click", e => {
            const b = e.target.closest(".rs-chip");
            if (!b) return;
            venueState.type = b.dataset.type || "";
            renderVenueList(true);
        });
        let timer = null;
        if (search) search.addEventListener("input", () => {
            venueState.q = search.value.trim();
            clearTimeout(timer);
            timer = setTimeout(() => renderVenueList(true), 200);
        });
        if (reset) reset.addEventListener("click", () => {
            venueState.type = ""; venueState.q = "";
            if (search) search.value = "";
            if (rsMap) rsMap.closePopup();
            renderVenueList(true);
        });
    }

    function initVenueMap(venues) {
        const mapEl = document.getElementById("mapa-ruta-salsera");
        if (typeof L === "undefined" || !mapEl) return;

        rsMap = L.map(mapEl, { scrollWheelZoom: false, zoomControl: true });
        L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
            attribution: '&copy; <a href="https://openstreetmap.org/copyright" target="_blank" rel="noopener noreferrer">OpenStreetMap</a>',
            maxZoom: 18,
        }).addTo(rsMap);
        // En una página larga, la rueda solo hace zoom después de un clic en el mapa.
        rsMap.on("click", () => rsMap.scrollWheelZoom.enable());
        mapEl.addEventListener("mouseleave", () => rsMap.scrollWheelZoom.disable());
        if (typeof ResizeObserver !== "undefined") new ResizeObserver(() => rsMap.invalidateSize()).observe(mapEl);

        rsLayer = L.layerGroup().addTo(rsMap);
        rsMap.setView([6.2477, -75.5910], 14);

        venues.forEach(v => {
            if (!v.coordinates) return;
            if (!hasCoords(v)) return;
            const info = typeInfo(v);
            const icon = L.divIcon({
                className: "rs-pin-wrap",
                html: '<span class="rs-pin" style="--c:' + info.color + '"></span>',
                iconSize: [22, 22], iconAnchor: [11, 11], popupAnchor: [0, -12],
            });
            const m = L.marker([v.coordinates.lat, v.coordinates.lng], { icon, riseOnHover: true });
            m.bindPopup(venuePopup(v), { maxWidth: 300, minWidth: 200 });
            m.bindTooltip(v.name, { direction: "top", offset: [0, -10], className: "rs-tip" });
            m.on("click", () => setActiveVenue(v._k));
            m._venueId = v.id;
            venueMarkers.set(v._k, m);
        });

        // Polyline estática conectando los lugares en route_order (Fase 5C.1)
        const routeVenues = venues
            .filter(v => v.route_order != null && hasCoords(v))
            .sort((a, b) => a.route_order - b.route_order);
        let routePolyline = null;
        if (routeVenues.length >= 2) {
            routePolyline = L.polyline(routeVenues.map(v => [v.coordinates.lat, v.coordinates.lng]), {
                color: "#ffc107",
                weight: 3,
                opacity: 0.8,
                className: "rs-route-polyline",
            }).addTo(rsMap);
        }

        // Referencias globales usadas por el filtro de categorías
        window._rsMap = rsMap;
        window._rsMarkers = [...venueMarkers.values()];
        window._rsRoutePolyline = routePolyline;
    }

    function renderLugares(venues) {
        const c = clearSpinner("ruta-lugares-container");
        if (!c) return;
        allVenues = (venues || []).slice();
        allVenues.forEach((v, i) => {
            v._k = v.id || ("v" + i);
            v._hay = norm([v.name, v.address, v.music_style, v.description, typeInfo(v).label].filter(Boolean).join(" "));
        });
        initVenueMap(allVenues);
        allVenues.forEach(v => {
            const col = venueCard(v);
            const card = col.querySelector(".rs-place");
            const openMap = () => focusVenue(v._k);
            const mapBtn = col.querySelector(".rs-card-map-btn");
            if (mapBtn) mapBtn.addEventListener("click", e => { e.stopPropagation(); openMap(); });
            card.addEventListener("click", e => { if (e.target.closest("a, button")) return; openMap(); });
            card.addEventListener("keydown", e => {
                if (e.target !== card) return;
                if (e.key === "Enter" || e.key === " ") { e.preventDefault(); openMap(); }
            });
            card.addEventListener("mouseenter", () => hotVenue(v._k, true));
            card.addEventListener("mouseleave", () => hotVenue(v._k, false));
            venueCards.set(v._k, col);
        });
        buildTypeChips();
        initVenueControls();
        renderVenueList(true);
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
            fetch("/static/data/coords_osm.json").then(r => (r.ok ? r.json() : {})).catch(() => ({})).then(extra => {
            (data.venues || []).forEach(v => {
                const c = extra[v.id];
                if (!v.coordinates && c && typeof c.lat === "number" && typeof c.lng === "number") {
                    v.coordinates = { lat: c.lat, lng: c.lng };
                    v.coords_approx = true;
                }
            });
            renderLugares(data.venues);
        });
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
