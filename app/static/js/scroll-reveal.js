/**
 * scroll-reveal.js
 * ------------------
 * Efecto de entrada al hacer scroll: los titulos, tarjetas, imagenes
 * y videos aparecen con un leve desplazamiento + fundido cuando entran
 * en pantalla, en vez de aparecer de golpe.
 *
 * Funciona de forma AUTOMATICA con contenido que se agrega
 * dinamicamente (fetch + innerHTML, como en content.js/timeline.js):
 * usa un MutationObserver para detectar elementos nuevos, asi que no
 * hace falta llamar nada manualmente desde cada funcion cargarX().
 */
(function () {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        // Respeta la preferencia de accesibilidad: sin animaciones.
        return;
    }

    const SELECTOR_REVELAR = [
        'main h3',
        'main .card',
        'main .card-glass',
        '#entrevistas-container video',
        '.form-container',
        '.quiz-container',
    ].join(', ');

    const observadorInterseccion = new IntersectionObserver((entradas) => {
        entradas.forEach((entrada) => {
            if (entrada.isIntersecting) {
                entrada.target.classList.add('reveal-visible');
                observadorInterseccion.unobserve(entrada.target);
            }
        });
    }, { threshold: 0.12 });

    function prepararElemento(el) {
        if (el.dataset.revelado) return;
        el.dataset.revelado = '1';
        el.classList.add('reveal-init');
        observadorInterseccion.observe(el);
    }

    function escanear(raiz) {
        if (!raiz.querySelectorAll) return;
        raiz.querySelectorAll(SELECTOR_REVELAR).forEach(prepararElemento);
    }

    // Escaneo inicial, por si algo ya esta en el DOM al cargar la pagina
    document.addEventListener('DOMContentLoaded', () => escanear(document));

    // El resto del contenido se inyecta dinamicamente via fetch en
    // content.js / timeline.js -- este observer detecta esos cambios
    // y aplica el efecto automaticamente a lo nuevo, sin tocar esos
    // archivos.
    const observadorMutaciones = new MutationObserver((mutaciones) => {
        mutaciones.forEach((m) => {
            m.addedNodes.forEach((nodo) => {
                if (nodo.nodeType !== 1) return; // solo elementos, no texto
                if (nodo.matches && nodo.matches(SELECTOR_REVELAR)) {
                    prepararElemento(nodo);
                }
                escanear(nodo);
            });
        });
    });

    observadorMutaciones.observe(document.body, { childList: true, subtree: true });
})();
