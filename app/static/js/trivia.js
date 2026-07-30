/**
 * trivia.js
 * ---------
 * Lógica del reto completo de trivia en /desafio. Reescrito desde cero:
 * la versión anterior esperaba botones estáticos con clase .trivia-option
 * y data-correct ya escritos a mano en el HTML, pero desafio.html en
 * realidad tiene contenedores VACÍOS (#options-container) para llenar
 * dinámicamente. Como los IDs nunca coincidían, la página se quedaba
 * congelada en "Cargando desafío..." para siempre.
 *
 * Ahora: carga TODAS las preguntas de /api/trivia (el mismo banco único
 * que usa el quiz rápido de la portada), las recorre una por una, suma
 * puntos, y al final permite guardar el puntaje en el leaderboard real.
 */

let preguntas = [];
let indiceActual = 0;
let puntaje = 0;
const PUNTOS_POR_ACIERTO = 10;

document.addEventListener('DOMContentLoaded', () => {
    cargarPreguntas();
});

async function cargarPreguntas() {
    const textoPregunta = document.getElementById('question-text');
    try {
        const res = await fetch('/api/trivia');
        if (!res.ok) throw new Error('Error de red');
        preguntas = await res.json();

        if (!preguntas || preguntas.length === 0) {
            if (textoPregunta) textoPregunta.textContent = 'No hay preguntas disponibles ahora mismo.';
            return;
        }

        // Orden aleatorio para que rejugar no sea siempre la misma secuencia
        preguntas.sort(() => Math.random() - 0.5);

        indiceActual = 0;
        puntaje = 0;
        mostrarPregunta();
    } catch (e) {
        console.error('Error al cargar la trivia:', e);
        if (textoPregunta) textoPregunta.textContent = 'No se pudo cargar el desafío. Intenta recargar la página.';
    }
}

function mostrarPregunta() {
    const textoPregunta = document.getElementById('question-text');
    const contenedorOpciones = document.getElementById('options-container');
    const contadorPregunta = document.getElementById('question-count');
    const scoreBadge = document.getElementById('score-badge');
    const feedback = document.getElementById('feedback');
    const btnSiguiente = document.getElementById('next-btn');

    if (!textoPregunta || !contenedorOpciones) return;

    const preg = preguntas[indiceActual];

    textoPregunta.textContent = preg.pregunta;
    if (contadorPregunta) contadorPregunta.textContent = `Pregunta ${indiceActual + 1} de ${preguntas.length}`;
    if (scoreBadge) scoreBadge.textContent = `Puntos: ${puntaje}`;

    if (feedback) {
        feedback.classList.add('d-none');
        feedback.innerHTML = '';
    }
    if (btnSiguiente) btnSiguiente.classList.add('d-none');

    contenedorOpciones.innerHTML = preg.opciones.map((opcion, idx) => `
        <button class="btn btn-outline-warning text-white text-start" data-index="${idx}" onclick="responder(${idx})">
            ${opcion}
        </button>
    `).join('');
}

function responder(seleccion) {
    const preg = preguntas[indiceActual];
    const esCorrecta = seleccion === preg.correcta;
    const contenedorOpciones = document.getElementById('options-container');
    const feedback = document.getElementById('feedback');
    const scoreBadge = document.getElementById('score-badge');
    const btnSiguiente = document.getElementById('next-btn');

    // Desactiva todos los botones para que no se pueda responder dos veces
    contenedorOpciones.querySelectorAll('button').forEach(btn => {
        btn.disabled = true;
        const idx = parseInt(btn.dataset.index, 10);
        if (idx === preg.correcta) btn.classList.replace('btn-outline-warning', 'btn-success');
        else if (idx === seleccion) btn.classList.replace('btn-outline-warning', 'btn-danger');
    });

    if (esCorrecta) {
        puntaje += PUNTOS_POR_ACIERTO;
        if (scoreBadge) scoreBadge.textContent = `Puntos: ${puntaje}`;
    }

    if (feedback) {
        feedback.classList.remove('d-none');
        feedback.innerHTML = esCorrecta
            ? `<span class="text-success fw-bold">¡Correcto! +${PUNTOS_POR_ACIERTO} puntos 🎉</span>`
            : `<span class="text-danger fw-bold">Incorrecto. Era: ${preg.opciones[preg.correcta]}</span>`;
    }

    const esUltima = indiceActual === preguntas.length - 1;
    if (btnSiguiente) {
        btnSiguiente.classList.remove('d-none');
        btnSiguiente.textContent = esUltima ? 'Ver resultado final 🏆' : 'Siguiente Pregunta ➡️';
        btnSiguiente.onclick = esUltima ? mostrarResultadoFinal : siguientePregunta;
    }
}

function siguientePregunta() {
    indiceActual += 1;
    mostrarPregunta();
}

function mostrarResultadoFinal() {
    const quizCard = document.getElementById('quiz-card');
    const resultCard = document.getElementById('result-card');
    const finalScore = document.getElementById('final-score');

    if (quizCard) quizCard.classList.add('d-none');
    if (finalScore) finalScore.textContent = puntaje;
    if (resultCard) resultCard.classList.remove('d-none');
}

async function guardarPuntajeDesafio(event) {
    event.preventDefault();

    const nombre = document.getElementById('desafio-nombre')?.value || 'Salsero Anónimo';
    const mensajeGuardado = document.getElementById('desafio-guardado-msg');
    const btnGuardar = document.getElementById('btn-guardar-desafio');

    try {
        if (btnGuardar) btnGuardar.disabled = true;

        const res = await fetch('/api/leaderboard', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                nombre_jugador: nombre,
                puntaje: puntaje
            })
        });

        if (res.ok && mensajeGuardado) {
            mensajeGuardado.classList.remove('d-none');
            mensajeGuardado.textContent = '¡Puntaje guardado en el ranking! 🏆';
        } else if (mensajeGuardado) {
            mensajeGuardado.classList.remove('d-none');
            mensajeGuardado.classList.add('text-danger');
            mensajeGuardado.textContent = 'No se pudo guardar el puntaje. Intenta de nuevo.';
        }
    } catch (e) {
        console.error('Error guardando puntaje del desafío:', e);
        if (mensajeGuardado) {
            mensajeGuardado.classList.remove('d-none');
            mensajeGuardado.classList.add('text-danger');
            mensajeGuardado.textContent = 'Error de conexión al guardar el puntaje.';
        }
    } finally {
        if (btnGuardar) btnGuardar.disabled = false;
    }
}
