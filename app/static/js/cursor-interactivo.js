/**
 * cursor-interactivo.js
 * ----------------------
 * Crea un halo de luz que sigue al cursor con un leve retraso
 * (efecto "glow"). Usa requestAnimationFrame para actualizar la
 * posicion una sola vez por frame en vez de en cada evento de
 * mousemove, asi no afecta el rendimiento. Se desactiva por
 * completo en pantallas tactiles y si el usuario prefiere menos
 * animaciones (accesibilidad).
 */
(function () {
    const esTactil = window.matchMedia('(pointer: coarse)').matches;
    const prefiereMenosMovimiento = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (esTactil || prefiereMenosMovimiento) return;

    const glow = document.createElement('div');
    glow.id = 'cursor-glow';
    document.body.appendChild(glow);

    let mouseX = window.innerWidth / 2;
    let mouseY = window.innerHeight / 2;
    let glowX = mouseX;
    let glowY = mouseY;
    let animando = false;

    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
        if (!animando) {
            animando = true;
            requestAnimationFrame(actualizar);
        }
    });

    function actualizar() {
        // Suavizado (lerp): el glow "persigue" al cursor con inercia
        glowX += (mouseX - glowX) * 0.15;
        glowY += (mouseY - glowY) * 0.15;
        glow.style.transform = `translate(${glowX}px, ${glowY}px) translate(-50%, -50%)`;

        if (Math.abs(mouseX - glowX) > 0.5 || Math.abs(mouseY - glowY) > 0.5) {
            requestAnimationFrame(actualizar);
        } else {
            animando = false;
        }
    }
})();
