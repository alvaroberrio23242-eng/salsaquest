// app/static/js/trivia.js

// ==========================================
// 1. ESTADO GLOBAL DE LA APLICACIÓN
// ==========================================
let questions = [];
let currentQuestionIndex = 0;
let score = 0;

// ==========================================
// 2. REFERENCIAS A ELEMENTOS DEL DOM
// ==========================================
const questionText = document.getElementById('question-text');
const optionsContainer = document.getElementById('options-container');
const scoreBadge = document.getElementById('score-badge');
const questionCount = document.getElementById('question-count');
const nextBtn = document.getElementById('next-btn');
const feedback = document.getElementById('feedback');
const quizCard = document.getElementById('quiz-card');
const resultCard = document.getElementById('result-card');
const finalScore = document.getElementById('final-score');

// ==========================================
// 3. FUNCIONES PRINCIPALES DE LA TRIVIA
// ==========================================

/**
 * Carga las preguntas desde la API de Flask (/api/trivia)
 */
async function loadQuestions() {
    try {
        const response = await fetch('/api/trivia');
        questions = await response.json();

        if (questions.length > 0) {
            showQuestion();
        } else {
            if (questionText) {
                questionText.innerText = "No se encontraron preguntas disponibles.";
            }
        }
    } catch (error) {
        console.error("Error al cargar la trivia:", error);
        if (questionText) {
            questionText.innerText = "Error al conectar con el servidor.";
        }
    }
}

/**
 * Muestra la pregunta actual y genera dinámicamente los botones de opciones
 */
function showQuestion() {
    resetState();
    const q = questions[currentQuestionIndex];

    if (questionCount) {
        questionCount.innerText = `Pregunta ${currentQuestionIndex + 1} de ${questions.length}`;
    }
    if (questionText) {
        questionText.innerText = q.pregunta;
    }

    q.opciones.forEach((opcion, index) => {
        const btn = document.createElement('button');
        btn.innerText = opcion;
        btn.classList.add('btn', 'btn-outline-light', 'btn-lg', 'text-start', 'py-3');
        btn.onclick = () => selectOption(index, q.correcta);
        optionsContainer.appendChild(btn);
    });
}

/**
 * Limpia el contenedor de opciones y oculta botones y mensajes de feedback
 */
function resetState() {
    if (nextBtn) nextBtn.classList.add('d-none');
    if (feedback) feedback.classList.add('d-none');
    if (optionsContainer) optionsContainer.innerHTML = '';
}

/**
 * Maneja la selección de una respuesta y valida si es correcta
 */
function selectOption(selectedIndex, correctIndex) {
    const buttons = optionsContainer.children;

    // Deshabilitar todas las opciones para prevenir múltiples clics
    for (let btn of buttons) {
        btn.disabled = true;
    }

    if (selectedIndex === correctIndex) {
        buttons[selectedIndex].classList.replace('btn-outline-light', 'btn-success');
        score += 100;
        if (scoreBadge) scoreBadge.innerText = `Puntos: ${score}`;
        
        if (feedback) {
            feedback.innerText = "🎉 ¡Correcto! Sabes de salsa.";
            feedback.className = "mt-4 text-center alert alert-success fw-bold";
        }
    } else {
        buttons[selectedIndex].classList.replace('btn-outline-light', 'btn-danger');
        buttons[correctIndex].classList.replace('btn-outline-light', 'btn-success');
        
        if (feedback) {
            feedback.innerText = "❌ Incorrecto, ¡sigue practicando!";
            feedback.className = "mt-4 text-center alert alert-danger fw-bold";
        }
    }

    if (feedback) feedback.classList.remove('d-none');

    // Control del flujo: siguiente pregunta o mostrar pantalla final
    if (currentQuestionIndex + 1 < questions.length) {
        if (nextBtn) nextBtn.classList.remove('d-none');
    } else {
        setTimeout(showResults, 1500);
    }
}

/**
 * Oculta la tarjeta del juego y muestra la pantalla final con la puntuación
 */
function showResults() {
    if (quizCard) quizCard.classList.add('d-none');
    if (resultCard) resultCard.classList.remove('d-none');
    if (finalScore) finalScore.innerText = `${score} pts`;
}

// ==========================================
// 4. EVENTOS E INICIALIZACIÓN
// ==========================================
if (nextBtn) {
    nextBtn.addEventListener('click', () => {
        currentQuestionIndex++;
        showQuestion();
    });
}

// Iniciar la trivia
loadQuestions();