document.addEventListener('DOMContentLoaded', () => {
    const triviaButtons = document.querySelectorAll('.trivia-option');
    const feedbackDiv = document.getElementById('trivia-feedback');

    triviaButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            const isCorrect = e.target.getAttribute('data-correct') === 'true';

            triviaButtons.forEach(btn => btn.disabled = true);

            if (isCorrect) {
                e.target.classList.remove('btn-outline-warning');
                e.target.classList.add('btn-success');
                feedbackDiv.innerHTML = '<p class="text-success fw-bold mt-2 mb-0">¡Correcto! ¡Puntos sumados! 🎉</p>';
            } else {
                e.target.classList.remove('btn-outline-warning');
                e.target.classList.add('btn-danger');
                feedbackDiv.innerHTML = '<p class="text-danger fw-bold mt-2 mb-0">Incorrecto. Era Héctor Lavoe. ❌</p>';
            }
        });
    });
});