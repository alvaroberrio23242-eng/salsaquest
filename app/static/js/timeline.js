// app/static/js/timeline.js

document.addEventListener('DOMContentLoaded', () => {
    cargarTimeline();
    cargarLeaderboard();
});

// 1. CARGAR TARJETAS CON VIDEOS / ENTREVISTAS DE YOUTUBE
async function cargarTimeline() {
    const track = document.getElementById('timeline-track');
    if (!track) return;

    try {
        const response = await fetch('/api/timeline');
        const eventos = await response.json();

        if (!eventos || eventos.length === 0) {
            track.innerHTML = '<p class="text-center w-100 text-secondary">No hay hitos disponibles por ahora.</p>';
            return;
        }

        track.innerHTML = eventos.map(evento => {
            const tieneVideo = evento.audio_url && evento.audio_url.includes('youtube');

            return `
                <div class="col">
                    <div class="card h-100 bg-dark text-white border-secondary shadow-sm rounded-4 overflow-hidden">
                        <img src="${evento.imagen || 'https://via.placeholder.com/300x180?text=SalsaQuest'}" 
                             class="card-img-top" 
                             alt="${evento.titulo}" 
                             style="height: 180px; object-fit: cover;">
                        
                        <div class="card-body d-flex flex-column">
                            <div class="d-flex justify-content-between align-items-center mb-2">
                                <span class="badge bg-warning text-dark fw-bold px-3 py-2 fs-6">${evento.anio}</span>
                                ${tieneVideo ? '<span class="badge bg-danger"><i class="fa-brands fa-youtube me-1"></i> Entrevista / Video</span>' : ''}
                            </div>
                            
                            <h5 class="card-title text-warning fw-bold mt-1">${evento.titulo}</h5>
                            <p class="card-text text-light small">${evento.descripcion}</p>

                            ${tieneVideo ? `
                                <div class="ratio ratio-16x9 my-2 rounded-3 overflow-hidden shadow">
                                    <iframe src="${evento.audio_url}" title="Entrevista ${evento.titulo}" allowfullscreen style="border:0;"></iframe>
                                </div>
                            ` : ''}

                            ${evento.trivia ? `
                                <div class="mt-auto pt-2 border-top border-secondary">
                                    <small class="text-info"><i class="fa-solid fa-lightbulb me-1"></i> <strong>Dato Curioso:</strong> ${evento.trivia}</small>
                                </div>
                            ` : ''}
                        </div>
                    </div>
                </div>
            `;
        }).join('');

    } catch (error) {
        console.error("Error al cargar la línea de tiempo:", error);
        track.innerHTML = '<p class="text-center w-100 text-danger">No pudimos cargar la historia. Revisa la conexión con el servidor.</p>';
    }
}

// 2. GUARDAR NUEVO EVENTO DESDE EL FORMULARIO
async function guardarNuevoEvento(e) {
    e.preventDefault();

    const anio = document.getElementById('anio').value;
    const titulo = document.getElementById('titulo').value;
    const descripcion = document.getElementById('descripcion').value;
    const trivia = document.getElementById('dato_curioso').value;
    const imagen = document.getElementById('imagen_url').value;

    try {
        const response = await fetch('/api/timeline', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ anio, titulo, descripcion, trivia, imagen })
        });

        if (response.ok) {
            alert('¡Hito guardado con éxito!');
            document.getElementById('form-nuevo-evento').reset();
            cargarTimeline();
        } else {
            alert('Error al guardar el hito.');
        }
    } catch (error) {
        console.error("Error:", error);
    }
}

// 3. SECCIÓN DE QUIZ & TABLA DE POSICIONES
const preguntasQuiz = [
    { pregunta: "¿En qué país nació el Son Cubano?", opciones: ["Puerto Rico", "Cuba", "Colombia"], correcta: 1 },
    { pregunta: "¿Quién era conocido como 'El Cantante de los Cantantes'?", opciones: ["Héctor Lavoe", "Ismael Rivera", "Cheo Feliciano"], correcta: 0 },
    { pregunta: "¿Cuál es el álbum de salsa más vendido de la historia?", opciones: ["Siembra", "El Malo", "Comedia"], correcta: 0 },
    { pregunta: "¿En qué ciudad nació el Grupo Niche?", opciones: ["Cali", "Bogotá", "Medellín"], correcta: 0 }
];

let puntajeActual = 0;

function iniciarQuiz() {
    const quizBox = document.getElementById('quiz-box');
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
        resultado.innerText = `¡Correcto! 🔥 Ganaste 50 puntos (Total: ${puntajeActual} pts)`;
        guardarPuntajeJugador();
    } else {
        resultado.innerText = `¡Incorrecto! 😅 Inténtalo de nuevo.`;
    }
    iniciarQuiz();
}

async function guardarPuntajeJugador() {
    const nombre = document.getElementById('nombre-jugador').value || 'Jugador Anónimo';
    try {
        await fetch('/api/leaderboard', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ nombre_jugador: nombre, puntaje: puntajeActual })
        });
        cargarLeaderboard();
    } catch (error) {
        console.error("Error al guardar puntaje:", error);
    }
}

async function cargarLeaderboard() {
    const lista = document.getElementById('lista-leaderboard');
    if (!lista) return;

    try {
        const response = await fetch('/api/leaderboard');
        const jugadores = await response.json();

        if (jugadores.length === 0) {
            lista.innerHTML = '<li class="list-group-item bg-dark text-secondary border-secondary">Aún no hay puntuaciones.</li>';
            return;
        }

        lista.innerHTML = jugadores.map((j, i) => `
            <li class="list-group-item bg-dark text-white border-secondary d-flex justify-content-between align-items-center">
                <span><strong>#${i + 1}</strong> ${j.nombre_jugador || j.username}</span>
                <span class="badge bg-warning text-dark fw-bold">${j.puntaje || j.score} pts</span>
            </li>
        `).join('');
    } catch (error) {
        lista.innerHTML = '<li class="list-group-item bg-dark text-secondary border-secondary">Puntuaciones locales de prueba.</li>';
    }
}

// 4. CAMBIO RÁPIDO DE IDIOMA (ES / EN)
function toggleLanguage() {
    const langText = document.getElementById('lang-text');
    if (langText.innerText.includes('ES')) {
        langText.innerText = 'EN / ES';
        alert('Language switched to English (Demo mode)');
    } else {
        langText.innerText = 'ES / EN';
        alert('Idioma cambiado a Español');
    }
}
// En la tarjeta del evento en timeline.js
const textoShare = encodeURIComponent(`🔥 ¡Mira este dato histórico en SalsaQuest! ${evento.titulo} (${evento.anio}): ${evento.trivia}`);
const linkWhatsApp = `https://api.whatsapp.com/send?text=${textoShare}`;

// Añadir dentro del HTML de la tarjeta:
<a href="${linkWhatsApp}" target="_blank" class="btn btn-sm btn-outline-success w-100 mt-2">
  <i class="fa-brands fa-whatsapp me-1"></i> Compartir dato en WhatsApp
</a>
// Generador Autónomo del Reto del Día
function cargarRetoDelDia() {
    const hoy = new Date();
    const diaDelAnio = Math.floor((hoy - new Date(hoy.getFullYear(), 0, 0)) / (1000 * 60 * 60 * 24));
    
    const retos = [
        " Hoy se cumplen años del auge de la Timba Cubana en La Habana.",
        " ¿Sabías que Héctor Lavoe improvisaba el 90% de sus soneos en vivo?",
        " El ritmo Songo fue creado mezclando la batería americana con la percusión afrocubana.",
        " Cali, Colombia es oficialmente reconocida como la Capital Mundial de la Salsa."
    ];

    const retoHoy = retos[diaDelAnio % retos.length];
    
    const quizInstruccion = document.getElementById('quiz-instruccion');
    if (quizInstruccion) {
        quizInstruccion.innerHTML = `<span class="badge bg-danger mb-2">🔥 RETO DIARIO</span><br>${retoHoy}`;
    }
}

// Ejecutar al cargar la página
document.addEventListener('DOMContentLoaded', cargarRetoDelDia);