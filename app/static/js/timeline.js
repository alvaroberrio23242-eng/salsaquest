// ==========================================
// SalsaQuest - Módulo Principal (timeline.js)
// ==========================================

let puntajeActual = 0;

document.addEventListener('DOMContentLoaded', () => {
    cargarTimeline();
    cargarLeaderboard();
    cargarRetoDelDia();
    iniciarQuiz();
});

// 1. CARGAR LÍNEA DEL TIEMPO
async function cargarTimeline() {
    const container = document.getElementById('timeline-container') || 
                      document.getElementById('timeline-track') || 
                      document.getElementById('timeline');

    if (!container) return;

    try {
        const response = await fetch('/api/timeline');
        if (!response.ok) throw new Error('Error en la respuesta del servidor');
        
        const eventos = await response.json();
        container.innerHTML = ''; // Limpia el spinner

        if (!eventos || eventos.length === 0) {
            container.innerHTML = '<p class="text-center w-100 text-secondary">No hay hitos disponibles por ahora.</p>';
            return;
        }

        eventos.forEach((evento) => {
            const tieneVideo = evento.audio_url && evento.audio_url.includes('youtube');
            const imagenSrc = evento.imagen_url || evento.imagen || 'https://via.placeholder.com/400x250?text=SalsaQuest';
            
            const textoShare = encodeURIComponent(`🔥 ¡Mira este dato histórico en SalsaQuest! ${evento.titulo} (${evento.anio}): ${evento.trivia || evento.descripcion}`);
            const linkWhatsApp = `https://api.whatsapp.com/send?text=${textoShare}`;

            let mediaHTML = '';
            if (evento.audio_url) {
                if (tieneVideo) {
                    const videoWatchUrl = evento.audio_url.replace('embed/', 'watch?v=').replace('youtube-nocookie.com', 'youtube.com');
                    mediaHTML = `
                        <div class="ratio ratio-16x9 my-2 rounded-3 overflow-hidden shadow bg-black">
                            <iframe src="${evento.audio_url}" title="${evento.titulo}" allowfullscreen style="border:0;"></iframe>
                        </div>
                        <a href="${videoWatchUrl}" target="_blank" class="btn btn-sm btn-outline-danger w-100 mb-2">
                            <i class="fa-brands fa-youtube me-1"></i> Abrir en YouTube ↗
                        </a>
                    `;
                } else {
                    mediaHTML = `
                        <div class="my-2">
                            <label class="form-label small text-warning fw-bold"><i class="fa-solid fa-music me-1"></i> Escucha el ritmo:</label>
                            <audio controls class="w-100">
                                <source src="${evento.audio_url}" type="audio/mpeg">
                            </audio>
                        </div>
                    `;
                }
            }

            const triviaHTML = evento.trivia ? `
                <div class="mt-auto pt-2 border-top border-secondary">
                    <small class="text-info"><i class="fa-solid fa-lightbulb me-1"></i> <strong>Dato Curioso:</strong> ${evento.trivia}</small>
                </div>
            ` : '';

            const eventCard = `
                <div class="col-md-6 mb-4 timeline-card" data-anio="${evento.anio}">
                    <div class="card h-100 card-glass text-white shadow-sm rounded-4 overflow-hidden">
                        <img src="${imagenSrc}" class="card-img-top" alt="${evento.titulo}" style="height: 180px; object-fit: cover;">
                        
                        <div class="card-body d-flex flex-column p-4">
                            <div class="d-flex justify-content-between align-items-center mb-2">
                                <span class="badge bg-warning text-dark fw-bold px-3 py-2 fs-6">${evento.anio}</span>
                                ${tieneVideo ? '<span class="badge bg-danger"><i class="fa-brands fa-youtube me-1"></i> Entrevista / Video</span>' : ''}
                            </div>
                            
                            <h5 class="card-title text-warning fw-bold mt-1">${evento.titulo}</h5>
                            <p class="card-text text-light small">${evento.descripcion}</p>

                            ${mediaHTML}
                            ${triviaHTML}

                            <a href="${linkWhatsApp}" target="_blank" class="btn btn-sm btn-outline-success w-100 mt-3">
                                <i class="fa-brands fa-whatsapp me-1"></i> Compartir en WhatsApp
                            </a>
                        </div>
                    </div>
                </div>
            `;

            container.innerHTML += eventCard;
        });

    } catch (error) {
        console.error("Error al cargar la línea de tiempo:", error);
        container.innerHTML = `
            <div class="col-12 text-center text-danger py-3">
                <p class="mb-0">⚠️ Ocurrió un error al cargar la línea del tiempo.</p>
            </div>
        `;
    }
}

// 2. QUIZ Y TRIVIA INTERACTIVA
const preguntasQuiz = [
    { pregunta: "¿En qué país nació el Son Cubano?", opciones: ["Puerto Rico", "Cuba", "Colombia"], correcta: 1 },
    { pregunta: "¿Quién era conocido como 'El Cantante de los Cantantes'?", opciones: ["Héctor Lavoe", "Ismael Rivera", "Cheo Feliciano"], correcta: 0 },
    { pregunta: "¿Cuál es el álbum de salsa más vendido de la historia?", opciones: ["Siembra", "El Malo", "Comedia"], correcta: 0 },
    { pregunta: "¿En qué ciudad nació el Grupo Niche?", opciones: ["Cali", "Bogotá", "Medellín"], correcta: 0 }
];

function iniciarQuiz() {
    const quizBox = document.getElementById('quiz-box');
    if (!quizBox) return;

    const preg = preguntasQuiz[Math.floor(Math.random() * preguntasQuiz.length)];

    quizBox.innerHTML = `
        <p class="fw-bold mb-3">${preg.pregunta}</p>
        <div class="d-grid gap-2">
            ${preg.opciones.map((opc, index) => `
                <button class="btn btn-outline-warning text-white" onclick="verificarRespuesta(${index}, ${preg.correcta})">${opc}</button>
            `).join('')}
        </div>
    `;
}

function verificarRespuesta(seleccion, correcta) {
    const resultado = document.getElementById('quiz-resultado');
    if (seleccion === correcta) {
        puntajeActual += 50;
        if (resultado) {
            resultado.innerHTML = `
                <span class="text-success fw-bold">¡Correcto! 🔥 Ganaste 50 puntos (Total: ${puntajeActual} pts)</span>
                <br>
                <button class="btn btn-sm btn-warning mt-2 fw-bold text-dark" onclick="abrirModalRegistro()">
                    💾 Guardar mi Puntaje
                </button>
            `;
        }
    } else {
        if (resultado) resultado.innerText = `¡Incorrecto! 😅 Inténtalo de nuevo.`;
    }
    iniciarQuiz();
}

// 3. CAPTURA DE LEADS Y GUARDADO EN LEADERBOARD
function abrirModalRegistro() {
    const modalElement = document.getElementById('modalRegistroLead');
    if (modalElement) {
        const modal = new bootstrap.Modal(modalElement);
        modal.show();
    } else {
        // Respaldo si no existe el modal
        const nombre = prompt('Ingresa tu nombre para el Leaderboard:');
        if (nombre) guardarPuntajeDirecto(nombre);
    }
}

async function guardarPuntajeConLead(event) {
    event.preventDefault();

    const nombre = document.getElementById('lead-nombre')?.value || 'Salsero';
    const whatsapp = document.getElementById('lead-whatsapp')?.value || '';
    const email = document.getElementById('lead-email')?.value || '';
    const acepta_promociones = document.getElementById('lead-consentimiento')?.checked ?? true;

    try {
        const response = await fetch('/api/leaderboard', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                nombre_jugador: nombre,
                whatsapp: whatsapp,
                email: email,
                puntaje: puntajeActual,
                acepta_promociones: acepta_promociones
            })
        });

        const data = await response.json();

        if (response.ok) {
            const msj = document.getElementById('mensaje-recompensa');
            if (msj) msj.classList.remove('d-none');
            
            document.getElementById('form-captura-lead')?.reset();
            cargarLeaderboard();
        } else {
            alert('Error al guardar datos: ' + (data.error || 'Inténtalo de nuevo'));
        }
    } catch (error) {
        console.error('Error enviando lead:', error);
        alert('Ocurrió un error de conexión.');
    }
}

async function cargarLeaderboard() {
    const lista = document.getElementById('lista-leaderboard') || document.getElementById('ranking-list');
    if (!lista) return;

    try {
        const response = await fetch('/api/leaderboard');
        if (!response.ok) throw new Error();
        
        const jugadores = await response.json();

        if (!jugadores || jugadores.length === 0) {
            lista.innerHTML = '<li class="list-group-item card-glass text-secondary">Aún no hay puntuaciones.</li>';
            return;
        }

        lista.innerHTML = jugadores.map((j, i) => `
            <li class="list-group-item card-glass text-white d-flex justify-content-between align-items-center py-3">
                <span><strong>#${i + 1}</strong> ${j.nombre_jugador || j.username || 'Salsero'}</span>
                <span class="badge bg-warning text-dark fw-bold rounded-pill">${j.puntaje || j.score || 0} pts</span>
            </li>
        `).join('');
    } catch (error) {
        console.log("Leaderboard en espera de conexión con el backend.");
    }
}

// 4. RETO DEL DÍA
function cargarRetoDelDia() {
    const hoy = new Date();
    const diaDelAnio = Math.floor((hoy - new Date(hoy.getFullYear(), 0, 0)) / (1000 * 60 * 60 * 24));
    
    const retos = [
        "Hoy se cumplen años del auge de la Timba Cubana en La Habana.",
        "¿Sabías que Héctor Lavoe improvisaba el 90% de sus soneos en vivo?",
        "El ritmo Songo fue creado mezclando la batería americana con la percusión afrocubana.",
        "Cali, Colombia es oficialmente reconocida como la Capital Mundial de la Salsa."
    ];

    const retoHoy = retos[diaDelAnio % retos.length];
    
    const quizInstruccion = document.getElementById('quiz-instruccion');
    if (quizInstruccion) {
        quizInstruccion.innerHTML = `<span class="badge bg-danger mb-2">🔥 RETO DIARIO</span><br>${retoHoy}`;
    }
}

// 5. CAMBIO RÁPIDO DE IDIOMA
function toggleLanguage() {
    const langText = document.getElementById('lang-text');
    if (!langText) return;

    if (langText.innerText.includes('ES')) {
        langText.innerText = 'EN / ES';
        alert('Language switched to English (Demo mode)');
    } else {
        langText.innerText = 'ES / EN';
        alert('Idioma cambiado a Español');
    }
}