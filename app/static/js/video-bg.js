/**
 * video-bg.js
 * ------------
 * Hace rotar varios clips de video como fondo de pantalla completo.
 * Si un clip no existe todavia (404) o falla al reproducir, salta al
 * siguiente en vez de romper la pagina o dejar la pantalla en negro.
 */
(function () {
    const video = document.getElementById('video-bg');
    if (!video) return;

    const baseUrl = video.dataset.baseUrl || '';

    // Nombres de los clips que rotan de fondo. Agrega o quita nombres
    // aqui segun los archivos que tengas realmente en
    // app/static/videos/ (deben coincidir exacto, incluyendo mayusculas/minusculas).
    const clips = [
        'habana-1.mp4',
        'habana-2.mp4',
        'habana-3.mp4',
        'habana-carro.mp4',
    ];

    let indice = 0;
    let intentosFallidos = 0;

    function reproducirClip(i) {
        video.src = baseUrl + clips[i];
        video.load();
        const promesa = video.play();
        if (promesa && typeof promesa.catch === 'function') {
            promesa.catch(() => {
                // Autoplay bloqueado por el navegador, o el archivo no
                // sirve: probamos con el siguiente clip de la lista.
                irAlSiguiente();
            });
        }
    }

    function irAlSiguiente() {
        intentosFallidos += 1;
        if (intentosFallidos >= clips.length) {
            // Ya probamos todos los clips y ninguno funcionó: nos
            // quedamos quietos con el color/poster de respaldo definido
            // en el CSS, en vez de seguir reintentando en bucle.
            return;
        }
        indice = (indice + 1) % clips.length;
        reproducirClip(indice);
    }

    video.addEventListener('ended', function () {
        intentosFallidos = 0;
        indice = (indice + 1) % clips.length;
        reproducirClip(indice);
    });

    video.addEventListener('error', irAlSiguiente);

    if (clips.length > 0) {
        reproducirClip(indice);
    }
})();
