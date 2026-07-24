// app/static/js/timeline.js

const ERA_COLORES = {
  raices: '#f2a93b',
  nueva_york: '#4fc3d9',
  fania: '#ef3f5d',
  expansion: '#8bd17c',
  medellin: '#e85fc0'
};

async function cargarTimeline() {
  const contenedor = document.getElementById('timeline-track');
  const progreso = obtenerProgreso();

  try {
    const respuesta = await fetch('/api/timeline');
    if (!respuesta.ok) throw new Error('No se pudo cargar la línea de tiempo');
    const nodos = await respuesta.json();

    contenedor.innerHTML = '';
    nodos.forEach(nodo => {
      contenedor.appendChild(crearTarjetaNodo(nodo, progreso));
    });
  } catch (error) {
    contenedor.innerHTML = '<p class="error">No pudimos cargar la historia. Intenta recargar la página.</p>';
    console.error(error);
  }
}

function crearTarjetaNodo(nodo, progreso) {
  const tarjeta = document.createElement('article');
  tarjeta.className = 'nodo';
  tarjeta.style.setProperty('--era-color', ERA_COLORES[nodo.era] || '#a393c9');
  if (progreso[nodo.id]) {
    tarjeta.classList.add('nodo--visitado');
  }

  tarjeta.innerHTML = `
    <span class="nodo__marcador"></span>
    <span class="nodo__anio">${nodo.anio_inicio}–${nodo.anio_fin}</span>
    <h2 class="nodo__titulo">${nodo.titulo}</h2>
    <p class="nodo__descripcion">${nodo.descripcion_corta}</p>
  `;

  tarjeta.addEventListener('click', () => {
    tarjeta.classList.add('nodo--visitado');
    marcarCompletado(nodo.id);
  });

  return tarjeta;
}

function obtenerProgreso() {
  return JSON.parse(localStorage.getItem('salsaquest_progreso')) || {};
}

function marcarCompletado(nodoId) {
  const progreso = obtenerProgreso();
  progreso[nodoId] = true;
  localStorage.setItem('salsaquest_progreso', JSON.stringify(progreso));
}

document.addEventListener('DOMContentLoaded', cargarTimeline);
