// app/static/js/trivia.js

let questions = [];
let currentQuestionIndex = 0;
let score = 0;

const questionText = document.getElementById('question-text');
const optionsContainer = document.getElementById('options-container');
const scoreBadge = document.getElementById('score-badge');
const questionCount = document.getElementById('question-count');
const nextBtn = document.getElementById('next-btn');
const feedback = document.getElementById('feedback');
const quizCard = document.getElementById('quiz-card');
const resultCard = document.getElementById('result-card');
const finalScore = document.getElementById('final-score');

// Cargar preguntas desde la API
async function loadQuestions() {
    try {
        const response = await fetch('/api/trivia');
        questions = await response.json();
        if (questions.length > 0) {
            showQuestion();
        } else {
            questionText.innerText = "No se encontraron preguntas disponibles.";
        }
    } catch (error) {
        console.error("Error al cargar la trivia:", error);
        questionText.innerText = "Error al conectar con el servidor.";
    }
}

function showQuestion() {
    resetState();
    const q = questions[currentQuestionIndex];
    questionCount.innerText = `Pregunta ${currentQuestionIndex + 1} de ${questions.length}`;
    questionText.innerText = q.pregunta;

    q.opciones.forEach((opcion, index) => {
        const btn = document.createElement('button');
        btn.innerText = opcion;
        btn.classList.add('btn', 'btn-outline-light', 'btn-lg', 'text-start', 'py-3');
        btn.onclick = () => selectOption(index, q.correcta);
        optionsContainer.appendChild(btn);
    });
}

function resetState() {
    nextBtn.classList.add('d-none');
    feedback.classList.add('d-none');
    optionsContainer.innerHTML = '';
}

function selectOption(selectedIndex, correctIndex) {
    const buttons = optionsContainer.children;
    
    // Deshabilitar todos los botones después de elegir
    for (let btn of buttons) {
        btn.disabled = true;
    }

    if (selectedIndex === correctIndex) {
        buttons[selectedIndex].classList.replace('btn-outline-light', 'btn-success');
        score += 100;
        scoreBadge.innerText = `Puntos: ${score}`;
        feedback.innerText = "🎉 ¡Correcto! Sabes de salsa.";
        feedback.className = "mt-4 text-center alert alert-success fw-bold";
    } else {
        buttons[selectedIndex].classList.replace('btn-outline-light', 'btn-danger');
        buttons[correctIndex].classList.replace('btn-outline-light', 'btn-success');
        feedback.innerText = "❌ Incorrecto, ¡sigue practicando!";
        feedback.className = "mt-4 text-center alert alert-danger fw-bold";
    }

    feedback.classList.remove('d-none');

    if (currentQuestionIndex + 1 < questions.length) {
        nextBtn.classList.remove('d-none');
    } else {
        setTimeout(showResults, 1500);
    }
}

nextBtn.addEventListener('click', () => {
    currentQuestionIndex++;
    showQuestion();
});

function showResults() {
    quizCard.classList.add('d-none');
    resultCard.classList.remove('d-none');
    finalScore.innerText = `${score} pts`;
}

// Iniciar trivia
loadQuestions();