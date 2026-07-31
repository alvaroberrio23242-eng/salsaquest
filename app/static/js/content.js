// ==========================================
// SalsaQuest - Contenido nuevo (content.js)
// Grandes eventos, récords, artistas/ritmos, timba,
// filtros de la línea del tiempo, y contador de visitas.
// ==========================================

document.addEventListener('DOMContentLoaded', () => {
    cargarEventosGrandes();
    cargarRecordsSalsa();
    cargarArtistas();
    cargarGrammy();
    cargarTimba();
    cargarEntrevistas();
    cargarCaratulas();
    cargarOrquestas();
    cargarInstrumentos();
    cargarMuseos();
    cargarMapaLugares();
    cargarRankingAlbumes();
    cargarMedellin();
    cargarSonHavana();
    cargarFiltrosTimeline();
    cargarVisitas();
});

// 1. GRANDES EVENTOS
async function cargarEventosGrandes() {
    const container = document.getElementById('eventos-container');
    if (!container) return;

    try {
        const res = await fetch('/api/eventos-grandes');
        const eventos = await res.json();
        container.innerHTML = '';

        eventos.forEach(ev => {
            container.innerHTML += `
                <div class="col-md-6 col-lg-3 mb-4">
                    <div class="card h-100 card-glass text-white shadow-sm rounded-4 overflow-hidden">
                        <img src="${ev.imagen_url}" class="card-img-top" alt="${ev.titulo}" style="height: 160px; object-fit: cover;">
                        <div class="card-body p-3">
                            <span class="badge bg-warning text-dark fw-bold mb-2">${ev.anio}</span>
                            <h6 class="text-warning fw-bold">${ev.titulo}</h6>
                            <p class="small text-secondary mb-1"><i class="fa-solid fa-location-dot me-1"></i>${ev.lugar}</p>
                            <p class="small text-light">${ev.descripcion}</p>
                        </div>
                    </div>
                </div>
            `;
        });
    } catch (e) {
        container.innerHTML = '<p class="text-danger text-center w-100">No se pudieron cargar los eventos.</p>';
    }
}

// 2. RÉCORDS DE LA SALSA
async function cargarRecordsSalsa() {
    const container = document.getElementById('records-container');
    if (!container) return;

    try {
        const res = await fetch('/api/records-salsa');
        const records = await res.json();
        container.innerHTML = '';

        records.forEach(r => {
            container.innerHTML += `
                <div class="col-md-6 col-lg-3 mb-4">
                    <div class="card h-100 card-glass text-white shadow-sm rounded-4 p-3">
                        <i class="fa-solid fa-trophy text-warning fa-2x mb-2"></i>
                        <h6 class="text-warning fw-bold">${r.titulo}</h6>
                        <p class="small fw-bold text-info mb-1">${r.dato}</p>
                        <p class="small text-light">${r.descripcion}</p>
                    </div>
                </div>
            `;
        });
    } catch (e) {
        container.innerHTML = '<p class="text-danger text-center w-100">No se pudieron cargar los récords.</p>';
    }
}

// 3. ARTISTAS Y RITMOS (con modal de detalle)
let cacheArtistas = [];

async function cargarArtistas() {
    const container = document.getElementById('artistas-container');
    if (!container) return;

    try {
        const res = await fetch('/api/artistas');
        cacheArtistas = await res.json();
        container.innerHTML = '';

        cacheArtistas.forEach(a => {
            const etiqueta = a.tipo === 'ritmo' ? 'Ritmo' : 'Artista';
            container.innerHTML += `
                <div class="col-md-6 col-lg-3 mb-4">
                    <div class="card h-100 card-glass text-white shadow-sm rounded-4 overflow-hidden" 
                         style="cursor:pointer" onclick="abrirModalArtista('${a.slug}')">
                        <img src="${a.imagen_url}" class="card-img-top" alt="${a.nombre}" style="height: 150px; object-fit: cover;">
                        <div class="card-body p-3">
                            <span class="badge bg-secondary small mb-2">${etiqueta}</span>
                            <h6 class="text-warning fw-bold">${a.nombre}</h6>
                            <p class="small text-light">${a.resumen}</p>
                            <span class="small text-info">Leer más <i class="fa-solid fa-arrow-right ms-1"></i></span>
                        </div>
                    </div>
                </div>
            `;
        });
    } catch (e) {
        container.innerHTML = '<p class="text-danger text-center w-100">No se pudieron cargar las historias.</p>';
    }
}

function abrirModalArtista(slug) {
    const artista = cacheArtistas.find(a => a.slug === slug);
    if (!artista) return;

    document.getElementById('modalArtistaTitulo').innerText = artista.nombre;
    document.getElementById('modalArtistaImagen').src = artista.imagen_url;
    document.getElementById('modalArtistaImagen').alt = artista.nombre;
    document.getElementById('modalArtistaTexto').innerText = artista.texto;

    const modalElement = document.getElementById('modalArtista');
    if (modalElement) new bootstrap.Modal(modalElement).show();
}

// GRAMMY: fila horizontal estilo Netflix
let cacheGrammy = [];
async function cargarGrammy() {
    const container = document.getElementById('grammy-container');
    if (!container) return;

    try {
        const res = await fetch('/api/grammy');
        cacheGrammy = await res.json();
        container.innerHTML = '';

        cacheGrammy.forEach(g => {
            container.innerHTML += `
                <div class="card card-glass text-white shadow-sm rounded-4 p-3 flex-shrink-0"
                     style="width: 220px; cursor:pointer; scroll-snap-align: start;"
                     onclick="abrirModalGrammy('${g.slug}')">
                    <i class="fa-solid fa-award text-warning fa-2x mb-2"></i>
                    <h6 class="text-warning fw-bold mb-1">${g.artista}</h6>
                    <p class="small text-secondary mb-1">${g.anio}</p>
                    <p class="small mb-0">${g.album}</p>
                </div>
            `;
        });
    } catch (e) {
        container.innerHTML = '<p class="text-danger text-center w-100">No se pudieron cargar los Grammy.</p>';
    }
}

function abrirModalGrammy(slug) {
    const g = cacheGrammy.find(x => x.slug === slug);
    if (!g) return;

    document.getElementById('modalGrammyTitulo').innerText = `${g.artista} — Grammy ${g.anio}`;
    document.getElementById('modalGrammyAlbum').innerText = g.album;
    document.getElementById('modalGrammyCategoria').innerText = g.categoria;
    document.getElementById('modalGrammyTexto').innerText = g.descripcion;

    const modalElement = document.getElementById('modalGrammy');
    if (modalElement) new bootstrap.Modal(modalElement).show();
}

// 4. TIMBA
async function cargarTimba() {
    const container = document.getElementById('timba-container');
    if (!container) return;

    try {
        const res = await fetch('/api/timba');
        const timba = await res.json();

        const recordsHTML = timba.records.map(r => `
            <li class="list-group-item card-glass text-white">
                <strong class="text-warning">${r.titulo}</strong> — ${r.dato}
                <br><span class="small text-secondary">${r.descripcion}</span>
            </li>
        `).join('');

        const playlistsHTML = timba.playlists.map(p => `
            <a href="${p.url}" target="_blank" class="btn btn-outline-success text-start mb-2 w-100">
                <i class="fa-brands fa-spotify me-2"></i><strong>${p.titulo}</strong>
                <br><span class="small text-secondary">${p.descripcion}</span>
            </a>
        `).join('');

        container.innerHTML = `
            <div class="row g-4">
                <div class="col-lg-6">
                    <div class="card card-glass text-white p-3 h-100">
                        <h6 class="text-warning fw-bold">Origen de la Timba</h6>
                        <p class="small text-light">${timba.historia}</p>
                        <ul class="list-group list-group-flush mt-2">${recordsHTML}</ul>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="card card-glass text-white p-3 h-100">
                        <h6 class="text-warning fw-bold mb-3"><i class="fa-brands fa-spotify me-2"></i>Playlists de Timba</h6>
                        ${playlistsHTML}
                    </div>
                </div>
            </div>
        `;
    } catch (e) {
        container.innerHTML = '<p class="text-danger text-center">No se pudo cargar la sección de Timba.</p>';
    }
}

// 5. FILTROS DE ÉPOCA PARA LA LÍNEA DEL TIEMPO
async function cargarFiltrosTimeline() {
    const contenedorFiltros = document.getElementById('timeline-filtros');
    if (!contenedorFiltros) return;

    try {
        // Reusa la MISMA petición/caché que timeline.js (ver
        // obtenerEventosTimeline en timeline.js), en vez de volver a
        // pedir /api/timeline por su cuenta.
        const eventos = await window.obtenerEventosTimeline();

        // Agrupa por década a partir del año (ej. "1971" -> "1970s")
        const decadas = new Set();
        eventos.forEach(ev => {
            const anioNum = parseInt(ev.anio, 10);
            if (!isNaN(anioNum)) decadas.add(Math.floor(anioNum / 10) * 10);
        });

        const decadasOrdenadas = Array.from(decadas).sort((a, b) => a - b);

        let botonesHTML = `<button class="btn btn-sm btn-warning fw-bold" onclick="filtrarTimeline('todas', this)">Todas</button>`;
        decadasOrdenadas.forEach(d => {
            botonesHTML += `<button class="btn btn-sm btn-outline-warning" onclick="filtrarTimeline('${d}', this)">${d}s</button>`;
        });

        contenedorFiltros.innerHTML = botonesHTML;
    } catch (e) {
        // Si falla, simplemente no se muestran filtros; el timeline sigue funcionando sin ellos.
    }
}

function filtrarTimeline(decada, botonClickeado) {
    // Vuelve a intentar sobre las tarjetas ya renderizadas por cargarTimeline()
    // (puede tardar un instante en existir si la timeline aun esta cargando).
    const tarjetas = document.querySelectorAll('.timeline-card');

    tarjetas.forEach(t => {
        const anio = parseInt(t.dataset.anio, 10);
        if (decada === 'todas' || isNaN(anio)) {
            t.style.display = '';
        } else {
            const decadaTarjeta = Math.floor(anio / 10) * 10;
            t.style.display = (decadaTarjeta === parseInt(decada, 10)) ? '' : 'none';
        }
    });

    document.querySelectorAll('#timeline-filtros button').forEach(b => b.classList.replace('btn-warning', 'btn-outline-warning'));
    if (botonClickeado) botonClickeado.classList.replace('btn-outline-warning', 'btn-warning');
}

// 6. CONTADOR DE VISITAS
async function cargarVisitas() {
    const span = document.getElementById('contador-visitas');
    if (!span) return;

    try {
        const res = await fetch('/api/visitas');
        const data = await res.json();
        span.innerHTML = `<i class="fa-solid fa-eye me-1"></i> ${data.total} visitas`;
    } catch (e) {
        span.innerHTML = '';
    }
}

// 7. ENTREVISTAS INÉDITAS (video real, no YouTube)
async function cargarEntrevistas() {
    const container = document.getElementById('entrevistas-container');
    if (!container) return;

    try {
        const res = await fetch('/api/entrevistas');
        const entrevistas = await res.json();

        if (!entrevistas.length) {
            container.innerHTML = '<p class="text-muted">Todavía no hay entrevistas cargadas.</p>';
            return;
        }

        container.innerHTML = entrevistas.map(e => `
            <div class="col-md-6 col-lg-4">
                <div class="card h-100 card-glass text-white rounded-4 overflow-hidden">
                    <video controls preload="metadata" class="w-100" style="max-height:220px; object-fit:cover; background:#000;"
                           ${e.miniatura_url ? `poster="/static/${e.miniatura_url}"` : ''}>
                        <source src="/static/videos/${e.video_url}" type="video/mp4">
                        Tu navegador no soporta el video.
                    </video>
                    <div class="card-body p-3">
                        <h5 class="card-title text-warning mb-1">${e.titulo}</h5>
                        <p class="small text-secondary mb-2">${e.invitado || ''}</p>
                        <p class="small mb-0">${e.descripcion}</p>
                    </div>
                </div>
            </div>
        `).join('');
    } catch (e) {
        container.innerHTML = '<p class="text-danger">No se pudieron cargar las entrevistas.</p>';
    }
}

// 8. CARÁTULAS ICÓNICAS (portada real via embed oficial de Spotify)
async function cargarCaratulas() {
    const container = document.getElementById('caratulas-container');
    if (!container) return;

    try {
        const res = await fetch('/api/caratulas');
        const caratulas = await res.json();

        container.innerHTML = caratulas.map(c => `
            <div class="col-md-6 col-lg-3 mb-4">
                <div class="card h-100 card-glass text-white rounded-4 overflow-hidden">
                    <iframe style="border-radius:12px 12px 0 0; border:0;"
                            src="https://open.spotify.com/embed/album/${c.spotify_album_id}?utm_source=generator&theme=0"
                            width="100%" height="152" frameBorder="0"
                            allowfullscreen=""
                            allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
                            loading="lazy">
                    </iframe>
                    <div class="card-body p-3">
                        <h6 class="text-warning fw-bold mb-0">${c.titulo}</h6>
                        <p class="small text-secondary mb-2">${c.artista} · ${c.anio}</p>
                        <p class="small mb-2"><strong class="text-success">Éxitos:</strong> ${c.exitos}</p>
                        <p class="small mb-0">${c.curiosidad}</p>
                    </div>
                </div>
            </div>
        `).join('');
    } catch (e) {
        container.innerHTML = '<p class="text-danger">No se pudieron cargar las carátulas.</p>';
    }
}

// 7. ORQUESTAS INFLUYENTES
async function cargarOrquestas() {
    const container = document.getElementById('orquestas-container');
    if (!container) return;
    try {
        const res = await fetch('/api/orquestas');
        const orquestas = await res.json();
        container.innerHTML = orquestas.map(o => `
            <div class="col-md-6 col-lg-4 mb-4">
                <div class="card h-100 card-glass text-white shadow-sm rounded-4 p-3">
                    <h6 class="text-warning fw-bold mb-1">${o.nombre}</h6>
                    <p class="small text-secondary mb-2"><i class="fa-solid fa-location-dot me-1"></i>${o.lugar} · Fundada en ${o.fundacion}</p>
                    <p class="small text-light mb-0">${o.texto}</p>
                </div>
            </div>
        `).join('');
    } catch (e) {
        container.innerHTML = '<p class="text-danger text-center w-100">No se pudieron cargar las orquestas.</p>';
    }
}

// 8. INSTRUMENTOS (galería interactiva)
let INSTRUMENTOS_CACHE = [];

async function cargarInstrumentos() {
    const container = document.getElementById('instrumentos-container');
    if (!container) return;
    try {
        const res = await fetch('/api/instrumentos');
        INSTRUMENTOS_CACHE = await res.json();
        container.innerHTML = INSTRUMENTOS_CACHE.map((i, idx) => `
            <div class="col-6 col-md-4 col-lg-2 mb-4">
                <div class="card h-100 card-glass text-white shadow-sm rounded-4 p-3 instrumento-card"
                     role="button" style="cursor:pointer;" onclick="abrirInstrumento(${idx})">
                    <img src="${i.imagen_url || 'https://via.placeholder.com/300x200?text=SalsaQuest'}" alt="${i.nombre}">
                    <span class="badge bg-warning text-dark fw-bold mb-2 align-self-start" style="font-size:0.65em;">${i.categoria}</span>
                    <h6 class="text-warning fw-bold mb-0">${i.nombre}</h6>
                    <p class="small text-secondary mt-2 mb-0"><i class="fa-solid fa-circle-info me-1"></i>Ver ficha</p>
                </div>
            </div>
        `).join('') + `
            <!-- Modal de detalle de instrumento -->
            <div class="modal fade" id="modalInstrumento" tabindex="-1" aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered modal-lg">
                    <div class="modal-content card-glass text-white border border-warning">
                        <div class="modal-header border-secondary">
                            <h5 class="modal-title text-warning fw-bold" id="modalInstrumentoTitulo"></h5>
                            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Cerrar"></button>
                        </div>
                        <div class="modal-body" id="modalInstrumentoBody"></div>
                    </div>
                </div>
            </div>
        `;
    } catch (e) {
        container.innerHTML = '<p class="text-danger text-center w-100">No se pudieron cargar los instrumentos.</p>';
    }
}

function abrirInstrumento(idx) {
    const i = INSTRUMENTOS_CACHE[idx];
    if (!i) return;
    document.getElementById('modalInstrumentoTitulo').innerHTML =
        `<i class="fa-solid fa-music me-2"></i>${i.nombre}`;
    document.getElementById('modalInstrumentoBody').innerHTML = `
        <span class="badge bg-warning text-dark fw-bold mb-3">${i.categoria}</span>
        <h6 class="text-warning small text-uppercase mt-2">Historia</h6>
        <p class="text-light">${i.texto}</p>
        <h6 class="text-warning small text-uppercase mt-3">Sonido</h6>
        <p class="text-light">${i.sonido || 'Próximamente.'}</p>
        <h6 class="text-warning small text-uppercase mt-3">Quiénes lo hicieron famoso</h6>
        <p class="text-light">${i.famosos_por || 'Próximamente.'}</p>
        ${i.video_busqueda ? `
        <a href="${i.video_busqueda}" target="_blank" rel="noopener" class="btn btn-outline-warning btn-sm mt-2">
            <i class="fa-brands fa-youtube me-1"></i>Buscar videos en YouTube
        </a>` : ''}
    `;
    const modal = new bootstrap.Modal(document.getElementById('modalInstrumento'));
    modal.show();
}

// 9. MUSEOS
async function cargarMuseos() {
    const container = document.getElementById('museos-container');
    if (!container) return;
    try {
        const res = await fetch('/api/museos');
        const museos = await res.json();
        container.innerHTML = museos.map(m => `
            <div class="col-md-6 col-lg-4 mb-4">
                <div class="card h-100 card-glass text-white shadow-sm rounded-4 p-3">
                    <h6 class="text-warning fw-bold mb-1">${m.nombre}</h6>
                    <p class="small text-secondary mb-2"><i class="fa-solid fa-location-dot me-1"></i>${m.lugar} · Desde ${m.fundacion}</p>
                    <p class="small text-light mb-0">${m.texto}</p>
                </div>
            </div>
        `).join('');
    } catch (e) {
        container.innerHTML = '<p class="text-danger text-center w-100">No se pudieron cargar los museos.</p>';
    }
}

// 10. MAPA DE LUGARES SALSEROS (Leaflet)
async function cargarMapaLugares() {
    const mapDiv = document.getElementById('mapa-lugares');
    if (!mapDiv || typeof L === 'undefined') return;
    try {
        const res = await fetch('/api/lugares-salseros');
        const lugares = await res.json();

        const mapa = L.map('mapa-lugares').setView([15, -70], 3);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; OpenStreetMap contributors',
            maxZoom: 18,
        }).addTo(mapa);

        lugares.forEach(lugar => {
            L.marker([lugar.lat, lugar.lng]).addTo(mapa)
                .bindPopup(`<strong>${lugar.nombre}</strong><br><span style="font-size:0.85em">${lugar.descripcion}</span>`);
        });
    } catch (e) {
        mapDiv.innerHTML = '<p class="text-danger text-center">No se pudo cargar el mapa.</p>';
    }
}

// 11. RANKING DE ÁLBUMES MÁS INFLUYENTES
async function cargarRankingAlbumes() {
    const container = document.getElementById('ranking-container');
    if (!container) return;
    try {
        const res = await fetch('/api/ranking-albumes');
        const data = await res.json();
        container.innerHTML = data.albumes.map(a => `
            <div class="col-12 mb-3">
                <div class="card card-glass text-white shadow-sm rounded-4 p-3 d-flex flex-row align-items-center gap-3">
                    <div class="display-6 fw-bold text-warning" style="min-width: 60px;">#${a.puesto}</div>
                    <div>
                        <h6 class="text-warning fw-bold mb-0">${a.titulo}</h6>
                        <p class="small text-secondary mb-1">${a.artista} · ${a.anio}</p>
                        <p class="small text-light mb-0">${a.motivo}</p>
                    </div>
                </div>
            </div>
        `).join('') + `
            <p class="small text-secondary text-center mt-2">
                Basado en el ranking de Rolling Stone (oct. 2024).
                <a href="${data.fuente_url}" target="_blank" rel="noopener" class="text-warning">Ver la lista completa de 50 &rarr;</a>
            </p>`;
    } catch (e) {
        container.innerHTML = '<p class="text-danger text-center w-100">No se pudo cargar el ranking.</p>';
    }
}

// 12. MEDELLÍN, CAPITAL MUNDIAL DE LA SALSA
// SON HAVANA: reutiliza los datos de /api/medellin (ya trae el bar
// "Son Havana (Laureles)" verificado), en vez de duplicar informacion.
async function cargarSonHavana() {
    const direccionEl = document.getElementById('son-havana-direccion');
    const descripcionEl = document.getElementById('son-havana-descripcion');
    const playlistLink = document.getElementById('son-havana-playlist-link');
    if (!direccionEl) return;

    try {
        const res = await fetch('/api/medellin');
        const data = await res.json();
        const bar = (data.bares || []).find(b => b.slug === 'son-havana-laureles');

        if (bar) {
            direccionEl.innerHTML = `<i class="fa-solid fa-location-dot me-1"></i> ${bar.direccion}`;
            if (descripcionEl) descripcionEl.textContent = bar.descripcion;
        } else {
            direccionEl.textContent = 'Información no disponible por ahora.';
        }

        if (playlistLink && data.playlist_url) {
            playlistLink.href = data.playlist_url;
        }
    } catch (e) {
        direccionEl.textContent = 'No se pudo cargar la información de Son Havana.';
    }
}

async function cargarMedellin() {
    const historiaEl = document.getElementById('medellin-historia');
    const baresContainer = document.getElementById('medellin-bares-container');
    const emisorasContainer = document.getElementById('medellin-emisoras-container');
    const pendienteEl = document.getElementById('medellin-pendiente');
    const mapaDiv = document.getElementById('mapa-medellin');
    if (!historiaEl && !baresContainer) return;

    try {
        const res = await fetch('/api/medellin');
        const data = await res.json();

        if (historiaEl) historiaEl.textContent = data.historia;

        if (baresContainer) {
            baresContainer.innerHTML = data.bares.map(b => `
                <div class="col-md-6 col-lg-4 mb-4">
                    <div class="card h-100 card-glass text-white shadow-sm rounded-4 p-3">
                        <h6 class="text-warning fw-bold mb-1">${b.nombre}</h6>
                        <p class="small text-secondary mb-2"><i class="fa-solid fa-location-dot me-1"></i>${b.direccion}</p>
                        <p class="small text-light mb-0">${b.descripcion}</p>
                    </div>
                </div>
            `).join('');
        }

        if (emisorasContainer) {
            emisorasContainer.innerHTML = data.emisoras.map(e => `
                <div class="col-md-6 col-lg-3 mb-3">
                    <a href="${e.url}" target="_blank" rel="noopener" class="text-decoration-none">
                        <div class="card h-100 card-glass text-white shadow-sm rounded-4 p-3">
                            <h6 class="text-warning fw-bold mb-1"><i class="fa-solid fa-radio me-1"></i>${e.nombre}</h6>
                            <p class="small text-light mb-0">${e.descripcion}</p>
                        </div>
                    </a>
                </div>
            `).join('');
        }

        if (pendienteEl) {
            pendienteEl.innerHTML = data.pendiente.map(p => `<li>${p}</li>`).join('');
        }

        if (mapaDiv && typeof L !== 'undefined') {
            const mapaMed = L.map('mapa-medellin').setView([6.2477, -75.5850], 13);
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '&copy; OpenStreetMap contributors',
                maxZoom: 18,
            }).addTo(mapaMed);
            data.bares.forEach(b => {
                L.marker([b.lat, b.lng]).addTo(mapaMed)
                    .bindPopup(`<strong>${b.nombre}</strong><br><span style="font-size:0.85em">${b.direccion}</span>`);
            });
        }
    } catch (e) {
        if (baresContainer) baresContainer.innerHTML = '<p class="text-danger text-center w-100">No se pudo cargar la sección de Medellín.</p>';
    }
}
