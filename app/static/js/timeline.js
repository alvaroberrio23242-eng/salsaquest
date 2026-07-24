// app/static/js/timeline.js

// 1. Configuración de colores por Era (Opcional)
const ERA_COLORES = {
    raices: '#f2a93b',
    nueva_york: '#4fc3d9',
    fania: '#ef3f5d',
    expansion: '#8bd17c',
    medellin: '#e85fc0'
};

// 2. Event Listener de inicio al cargar la página
document.addEventListener('DOMContentLoaded', () => {
    cargarLineaDeTiempo();
});

// 3. Obtener todos los eventos desde la Base de Datos (GET)
async function cargarLineaDeTiempo() {
    const contenedor = document.getElementById('timeline-container') || document.getElementById('timeline-track');
    if (!contenedor) return;

    const progreso = obtenerProgreso();

    try {
        const response = await fetch('/api/timeline');
        if (!response.ok) throw new Error('No se pudo obtener la línea de tiempo');
        
        const eventos = await response.json();
        contenedor.innerHTML = '';

        eventos.forEach(evento => {
            contenedor.innerHTML += crearTarjetaHTML(evento, progreso);
        });

    } catch (error) {
        console.error("Error al cargar la línea de tiempo:", error);
        contenedor.innerHTML = '<p class="error">No pudimos cargar la historia. Intenta recargar la página.</p>';
    }
}

// 4. Plantilla para renderizar cada tarjeta de evento con sus botones
function crearTarjetaHTML(evento, progreso) {
    const visitado = progreso[evento.id] ? 'nodo--visitado' : '';
    const colorEra = ERA_COLORES[evento.era] || '#a393c9';
    const anioTexto = evento.anio_fin ? `${evento.anio_inicio}–${evento.anio_fin}` : (evento.anio || evento.anio_inicio);

    return `
        <article class="timeline-item nodo ${visitado}" data-id="${evento.id}" style="--era-color: ${colorEra};" onclick="marcarCompletado(${evento.id})">
            <span class="timeline-year nodo__anio">${anioTexto}</span>
            <h3 class="timeline-title nodo__titulo">${evento.titulo}</h3>
            <p class="timeline-desc nodo__descripcion">${evento.descripcion || evento.descripcion_corta}</p>
            
            <div style="display: flex; gap: 8px; margin-top: 10px;">
                <button class="btn-trivia" onclick="event.stopPropagation(); cargarTrivia(${evento.id})">
                    💡 ¿Sabías qué?
                </button>
                <button class="btn-eliminar" onclick="event.stopPropagation(); eliminarEvento(${evento.id})" style="background: #e74c3c; color: white; border: none; padding: 6px 12px; border-radius: 20px; cursor: pointer; font-weight: bold;">
                    🗑️
                </button>
            </div>
            
            <div id="trivia-box-${evento.id}" class="trivia-box" style="display: none;">
                <p id="trivia-texto-${evento.id}"></p>
            </div>
        </article>
    `;
}

// 5. Cargar o toggle de la Trivia por evento (GET)
async function cargarTrivia(nodoId) {
    const cajaTrivia = document.getElementById(`trivia-box-${nodoId}`);
    const textoTrivia = document.getElementById(`trivia-texto-${nodoId}`);

    if (!cajaTrivia || !textoTrivia) return;

    // Toggle: Ocultar si ya está visible
    if (cajaTrivia.style.display === 'block') {
        cajaTrivia.style.display = 'none';
        return;
    }

    try {
        textoTrivia.innerText = "Cargando...";
        cajaTrivia.style.display = 'block';

        const response = await fetch(`/api/timeline/${nodoId}/trivia`);
        const data = await response.json();

        if (response.ok) {
            textoTrivia.innerText = data.dato_curioso;
        } else {
            textoTrivia.innerText = "No se pudo obtener el dato curioso.";
        }
    } catch (error) {
        console.error("Error al conectar con la API:", error);
        textoTrivia.innerText = "Error al conectar con el servidor.";
    }
}

// 6. Enviar nuevo evento desde el formulario a la BD (POST)
async function guardarNuevoEvento(event) {
    event.preventDefault(); // Evita recargar la página

    const nuevoEvento = {
        anio: parseInt(document.getElementById('anio').value),
        titulo: document.getElementById('titulo').value,
        descripcion: document.getElementById('descripcion').value,
        dato_curioso: document.getElementById('dato_curioso').value
    };

    try {
        const response = await fetch('/api/timeline', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(nuevoEvento)
        });

        if (response.ok) {
            alert('¡Evento agregado exitosamente!');
            document.getElementById('form-nuevo-evento').reset();
            cargarLineaDeTiempo(); // Recargar tarjetas dinámicamente
        } else {
            const err = await response.json();
            alert('Error: ' + (err.error || 'No se pudo guardar el evento.'));
        }
    } catch (error) {
        console.error('Error al guardar evento:', error);
        alert('Error de conexión con el servidor.');
    }
}

// 7. Eliminar un evento de la BD (DELETE)
async function eliminarEvento(nodoId) {
    if (!confirm('¿Estás seguro de que deseas eliminar este hito histórico?')) {
        return;
    }

    try {
        const response = await fetch(`/api/timeline/${nodoId}`, {
            method: 'DELETE'
        });

        if (response.ok) {
            cargarLineaDeTiempo(); // Recargar la línea de tiempo tras borrar
        } else {
            const data = await response.json();
            alert('Error: ' + (data.error || 'No se pudo eliminar el evento.'));
        }
    } catch (error) {
        console.error('Error al eliminar el evento:', error);
        alert('Error de conexión con el servidor.');
    }
}

// 8. Manejo del Progreso del Usuario en LocalStorage
function obtenerProgreso() {
    return JSON.parse(localStorage.getItem('salsaquest_progreso')) || {};
}

function marcarCompletado(nodoId) {
    const progreso = obtenerProgreso();
    progreso[nodoId] = true;
    localStorage.setItem('salsaquest_progreso', JSON.stringify(progreso));
    
    const tarjeta = document.querySelector(`[data-id="${nodoId}"]`);
    if (tarjeta) tarjeta.classList.add('nodo--visitado');
}
// ==========================================
// 🎯 LÓGICA DEL JUEGO / QUIZ
// ==========================================

async function iniciarQuiz() {
    const quizBox = document.getElementById('quiz-box');
    const resultado = document.getElementById('quiz-resultado');
    resultado.innerText = '';
    quizBox.innerHTML = '<p>Cargando pregunta...</p>';

    try {
        const response = await fetch('/api/quiz/pregunta');
        const data = await response.json();

        if (!response.ok) {
            quizBox.innerHTML = `<p>${data.error || 'No se pudo cargar la pregunta.'}</p>`;
            return;
        }

        // Renderizar la pregunta y las opciones
        let botonesHTML = data.opciones.map(opc => `
            <button onclick="verificarRespuesta(${opc.es_correcta})" style="margin: 5px; padding: 10px 18px; border-radius: 8px; border: none; cursor: pointer; font-weight: bold;">
                ${opc.anio}
            </button>
        `).join('');

        quizBox.innerHTML = `
            <h3>${data.pregunta}</h3>
            <p style="font-style: italic; opacity: 0.8;">"${data.descripcion}"</p>
            <div style="margin-top: 15px;">${botonesHTML}</div>
        `;

    } catch (error) {
        console.error('Error al cargar el quiz:', error);
        quizBox.innerHTML = '<p>Error de conexión con el servidor.</p>';
    }
}

function verificarRespuesta(esCorrecta) {
    const resultado = document.getElementById('quiz-resultado');
    const quizBox = document.getElementById('quiz-box');

    if (esCorrecta) {
        resultado.innerText = '🎉 ¡CORRECTO! ¡Llevas la salsa en las venas!';
        resultado.style.color = '#2ecc71';
    } else {
        resultado.innerText = '❌ ¡Incorrecto! Revisa la línea de tiempo e inténtalo de nuevo.';
        resultado.style.color = '#e74c3c';
    }

    quizBox.innerHTML = `
        <button onclick="iniciarQuiz()" class="btn-trivia" style="padding: 10px 20px; margin-top: 10px; cursor: pointer;">
            🔄 Siguiente Pregunta
        </button>
    `;
}
// ==========================================
// 🏆 SISTEMA DE PUNTAJE Y LEADERBOARD
// ==========================================

// Cargar la tabla de posiciones al iniciar
document.addEventListener('DOMContentLoaded', () => {
    cargarLeaderboard();
});

async function verificarRespuestaConPuntaje(esCorrecta) {
    const resultado = document.getElementById('quiz-resultado');
    const quizBox = document.getElementById('quiz-box');
    const nombreInput = document.getElementById('nombre-jugador');
    const nombre = nombreInput ? nombreInput.value.trim() : 'Jugador';

    if (esCorrecta) {
        resultado.innerText = '🎉 ¡CORRECTO! +10 Puntos.';
        resultado.style.color = '#2ecc71';
        // Enviar 10 puntos a la BD
        await enviarPuntaje(nombre, 10);
    } else {
        resultado.innerText = '❌ ¡Incorrecto! Inténtalo de nuevo.';
        resultado.style.color = '#e74c3c';
    }

    quizBox.innerHTML = `
        <button onclick="iniciarQuiz()" class="btn-trivia" style="padding: 10px 20px; margin-top: 10px; cursor: pointer;">
            🔄 Siguiente Pregunta
        </button>
    `;
}

async function enviarPuntaje(nombreJugador, puntos) {
    try {
        await fetch('/api/quiz/puntaje', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ nombre_jugador: nombreJugador, puntaje: puntos })
        });
        cargarLeaderboard(); // Actualizar la tabla en tiempo real
    } catch (error) {
        console.error('Error al guardar puntaje:', error);
    }
}

async function cargarLeaderboard() {
    const lista = document.getElementById('lista-leaderboard');
    if (!lista) return;

    try {
        const response = await fetch('/api/quiz/leaderboard');
        const jugadores = await response.json();

        lista.innerHTML = jugadores.map((j, index) => `
            <li style="padding: 4px 0;">
                ${index + 1}. <strong>${j.nombre_jugador}</strong>: ${j.puntaje} pts
            </li>
        `).join('');
    } catch (error) {
        console.error('Error al cargar leaderboard:', error);
        lista.innerHTML = '<li>No se pudo cargar la clasificación.</li>';
    }
}
function crearTarjetaHTML(evento, progreso) {
    const visitado = progreso[evento.id] ? 'nodo--visitado' : '';
    const colorEra = ERA_COLORES[evento.era] || '#a393c9';
    const anioTexto = evento.anio_fin ? `${evento.anio_inicio}–${evento.anio_fin}` : (evento.anio || evento.anio_inicio);

    return `
        <article class="timeline-item nodo ${visitado}" data-id="${evento.id}" style="--era-color: ${colorEra};" onclick="marcarCompletado(${evento.id})">
            ${evento.imagen_url ? `<img src="${evento.imagen_url}" alt="${evento.titulo}" style="width: 100%; height: 160px; object-fit: cover; border-radius: 6px; margin-bottom: 10px;">` : ''}
            
            <span class="timeline-year nodo__anio">${anioTexto}</span>
            <h3 class="timeline-title nodo__titulo">${evento.titulo}</h3>
            <p class="timeline-desc nodo__descripcion">${evento.descripcion || evento.descripcion_corta}</p>
            
            <div style="display: flex; gap: 8px; margin-top: 10px;">
                <button class="btn-trivia" onclick="event.stopPropagation(); cargarTrivia(${evento.id})">
                    💡 ¿Sabías qué?
                </button>
                <button class="btn-eliminar" onclick="event.stopPropagation(); eliminarEvento(${evento.id})" style="background: #e74c3c; color: white; border: none; padding: 6px 12px; border-radius: 20px; cursor: pointer; font-weight: bold;">
                    🗑️
                </button>
            </div>
            
            <div id="trivia-box-${evento.id}" class="trivia-box" style="display: none;">
                <p id="trivia-texto-${evento.id}"></p>
            </div>
        </article>
    `;
}
const nuevoEvento = {
    anio: parseInt(document.getElementById('anio').value),
    titulo: document.getElementById('titulo').value,
    descripcion: document.getElementById('descripcion').value,
    dato_curioso: document.getElementById('dato_curioso').value,
    imagen_url: document.getElementById('imagen_url').value // 📸 Capturar la URL
};
// ==========================================
// 🔒 CONTROL DE MODO ADMINISTRADOR
// ==========================================
let esAdmin = false;
const CLAVE_ADMIN = "salsa2026"; // Puedes cambiar esta clave

function toggleModoAdmin() {
    if (esAdmin) {
        esAdmin = false;
        alert("Haz salido del modo Administrador.");
    } else {
        const clave = prompt("Ingresa la clave de Administrador:");
        if (clave === CLAVE_ADMIN) {
            esAdmin = true;
            alert("¡Modo Administrador activado! 🚀");
        } else if (clave !== null) {
            alert("Clave incorrecta.");
        }
    }
    actualizarVistaAdmin();
}

function actualizarVistaAdmin() {
    const formContainer = document.getElementById('admin-form-container');
    const statusText = document.getElementById('status-admin');
    const botonesEliminar = document.querySelectorAll('.btn-admin-only');

    if (esAdmin) {
        if (formContainer) formContainer.style.display = 'block';
        if (statusText) statusText.innerText = "Modo: Administrador ⚡";
        botonesEliminar.forEach(btn => btn.style.display = 'inline-block');
    } else {
        if (formContainer) formContainer.style.display = 'none';
        if (statusText) statusText.innerText = "Modo: Visitante 👤";
        botonesEliminar.forEach(btn => btn.style.display = 'none');
    }
}
// Manejo de Modales
function openModal(id) { document.getElementById(id).style.display = 'flex'; }
function closeModal(id) { document.getElementById(id).style.display = 'none'; }

// Verificar usuario al cargar la página
document.addEventListener('DOMContentLoaded', () => {
    checkCurrentUser();
});

function checkCurrentUser() {
    fetch('/auth/current_user')
        .then(res => res.json())
        .then(data => {
            if (data.authenticated) {
                document.getElementById('auth-buttons').style.display = 'none';
                document.getElementById('user-info').style.display = 'block';
                document.getElementById('user-display-name').innerText = data.username;
                document.getElementById('user-score').innerText = data.score;
            } else {
                document.getElementById('auth-buttons').style.display = 'block';
                document.getElementById('user-info').style.display = 'none';
            }
        });
}

// Evento Login
document.getElementById('login-form')?.addEventListener('submit', (e) => {
    e.preventDefault();
    const data = {
        username: document.getElementById('login-username').value,
        password: document.getElementById('login-password').value
    };
    fetch('/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(res => {
        alert(res.message);
        if (res.success) {
            closeModal('login-modal');
            checkCurrentUser();
        }
    });
});

// Evento Registro
document.getElementById('register-form')?.addEventListener('submit', (e) => {
    e.preventDefault();
    const data = {
        username: document.getElementById('reg-username').value,
        email: document.getElementById('reg-email').value,
        password: document.getElementById('reg-password').value
    };
    fetch('/auth/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(res => {
        alert(res.message);
        if (res.success) {
            closeModal('register-modal');
            checkCurrentUser();
        }
    });
});

// Cerrar sesión
function logout() {
    fetch('/auth/logout', { method: 'POST' })
        .then(res => res.json())
        .then(data => {
            alert(data.message);
            checkCurrentUser();
        });
}