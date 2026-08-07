/**
 * video-bg.js
 * ------------
 * Hace rotar varios clips de video como fondo de pantalla completo,
 * con un fundido cruzado (crossfade) entre uno y el siguiente en vez
 * de un corte duro. Usa dos <video> superpuestos (#video-bg-a y
 * #video-bg-b): mientras uno se reproduce, el otro ya viene
 * precargado con el próximo clip, así el cambio es instantáneo y
 * sin parpadeo ni pantalla en negro.
 *
 * Accesibilidad y datos: si el usuario tiene activado
 * "reducir movimiento" en su sistema, o el navegador reporta modo
 * ahorro de datos, no se reproduce ningún video -- se deja el
 * poster fijo (mismo patrón que usa RockQuest en su propio
 * video-bg.js).
 */
(function () {
    const contenedor = document.querySelector('.video-bg-container');
    if (!contenedor) return;

    const capas = [
        document.getElementById('video-bg-a'),
        document.getElementById('video-bg-b'),
    ];
    if (!capas[0] || !capas[1]) return;

    const baseUrl = capas[0].dataset.baseUrl || '';

    // Nombres de los clips que rotan de fondo. Agrega o quita nombres
    // aqui segun los archivos que tengas realmente en
    // app/static/videos/ (deben coincidir exacto, incluyendo mayusculas/minusculas).
    const clipsBase = [
        'habana-1.mp4',
        'habana-2.mp4',
        'habana-3.mp4',
        'habana-carro.mp4',
    ];

    const prefiereMenosMovimiento = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const ahorraDatos = !!(navigator.connection && navigator.connection.saveData);

    if (prefiereMenosMovimiento || ahorraDatos || clipsBase.length === 0) {
        // Nos quedamos con el poster fijo definido en el HTML/CSS y
        // ni siquiera pedimos el primer video: ahorra datos y
        // respeta la preferencia del usuario.
        contenedor.classList.add('video-bg-estatico');
        return;
    }

    // Orden aleatorio en cada carga de página, para que no sea
    // siempre el mismo primer clip.
    const clips = clipsBase.slice();
    for (let i = clips.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [clips[i], clips[j]] = [clips[j], clips[i]];
    }

    const DURACION_CROSSFADE_MS = 1000;
    const ANTICIPACION_CAMBIO_S = 1.2; // arrancar el fundido este tiempo antes de que termine el clip

    let capaActivaIdx = 0;
    let indiceClip = 0;
    let intentosFallidos = 0;

    function url(nombreClip) {
        return baseUrl + nombreClip;
    }

    function capaActiva() { return capas[capaActivaIdx]; }
    function capaOculta() { return capas[1 - capaActivaIdx]; }

    function precargar(capa, nombreClip) {
        capa.src = url(nombreClip);
        capa.load();
    }

    function programarCambio(capa) {
        function alAcercarseElFinal() {
            if (!capa.duration) return;
            if (capa.duration - capa.currentTime <= ANTICIPACION_CAMBIO_S) {
                capa.removeEventListener('timeupdate', alAcercarseElFinal);
                cruzar();
            }
        }
        capa.addEventListener('timeupdate', alAcercarseElFinal);
    }

    function cruzar() {
        const siguienteIndice = (indiceClip + 1) % clips.length;
        const entrante = capaOculta();
        const saliente = capaActiva();

        const promesa = entrante.play();
        if (promesa && typeof promesa.catch === 'function') {
            promesa.catch(manejarFallo);
        }

        entrante.classList.add('is-active');
        saliente.classList.remove('is-active');

        setTimeout(function () {
            saliente.pause();
            capaActivaIdx = 1 - capaActivaIdx;
            indiceClip = siguienteIndice;
            intentosFallidos = 0;

            const proximoIndice = (indiceClip + 1) % clips.length;
            precargar(capaOculta(), clips[proximoIndice]);
            programarCambio(capaActiva());
        }, DURACION_CROSSFADE_MS);
    }

    function manejarFallo() {
        intentosFallidos += 1;
        if (intentosFallidos >= clips.length) {
            // Ya probamos todos los clips y ninguno funcionó: nos
            // quedamos quietos con el poster de respaldo.
            contenedor.classList.add('video-bg-estatico');
            return;
        }
        cruzar();
    }

    // Arranque: el primer clip entra directo (sin fundido, recién
    // estamos cargando la página) y el segundo queda precargado.
    precargar(capaActiva(), clips[indiceClip]);
    capaActiva().classList.add('is-active');
    const promesaInicial = capaActiva().play();
    if (promesaInicial && typeof promesaInicial.catch === 'function') {
        promesaInicial.catch(manejarFallo);
    }
    precargar(capaOculta(), clips[(indiceClip + 1) % clips.length]);
    programarCambio(capaActiva());

    capas[0].addEventListener('error', manejarFallo);
    capas[1].addEventListener('error', manejarFallo);
})();
