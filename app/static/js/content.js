// ==========================================
// SalsaQuest - Contenido nuevo (content.js)
// Grandes eventos, récords, artistas/ritmos, timba,
// filtros de la línea del tiempo, y contador de visitas.
// ==========================================

document.addEventListener('DOMContentLoaded', () => {
    cargarEventosGrandes();
    cargarRecordsSalsa();
    cargarArtistas();
    cargarTimba();
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
                <div class="col-md-6 col-lg-4 mb-4">
                    <div class="card h-100 bg-dark text-white border-secondary shadow-sm rounded-4 overflow-hidden">
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
                <div class="col-md-6 col-lg-4 mb-4">
                    <div class="card h-100 bg-dark text-white border-secondary shadow-sm rounded-4 p-3">
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
                    <div class="card h-100 bg-dark text-white border-secondary shadow-sm rounded-4 overflow-hidden" 
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

// 4. TIMBA
async function cargarTimba() {
    const container = document.getElementById('timba-container');
    if (!container) return;

    try {
        const res = await fetch('/api/timba');
        const timba = await res.json();

        const recordsHTML = timba.records.map(r => `
            <li class="list-group-item bg-dark text-white border-secondary">
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
                    <div class="card bg-dark text-white border-secondary p-3 h-100">
                        <h6 class="text-warning fw-bold">Origen de la Timba</h6>
                        <p class="small text-light">${timba.historia}</p>
                        <ul class="list-group list-group-flush mt-2">${recordsHTML}</ul>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="card bg-dark text-white border-secondary p-3 h-100">
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
        const res = await fetch('/api/timeline');
        const eventos = await res.json();

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
