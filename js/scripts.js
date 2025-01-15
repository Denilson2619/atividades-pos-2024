let allMotos = [];
let currentPage = 1;
const motosPerPage = 6;

// Dados das motos
const hondaMotos = [
    { model: "CB 500X", year: 2023, engine: "471cc", type: "Adventure", color: "Vermelha" },
    { model: "CB 1000R", year: 2023, engine: "998cc", type: "Street", color: "Preta" },
    { model: "CRF 250R", year: 2023, engine: "249cc", type: "Off-road", color: "Branca" },
    { model: "CBR 650R", year: 2023, engine: "649cc", type: "Sport", color: "Azul" },
    { model: "X-ADV", year: 2023, engine: "745cc", type: "Scooter", color: "Prata" },
    { model: "NC 750X", year: 2023, engine: "745cc", type: "Adventure", color: "Verde" },
    { model: "Honda Rebel 500", year: 2023, engine: "471cc", type: "Cruiser", color: "Preta" },
    { model: "CB 650R", year: 2023, engine: "648cc", type: "Naked", color: "Branca" },
    { model: "Africa Twin", year: 2023, engine: "1084cc", type: "Adventure", color: "Amarela" },
    { model: "CB 300R", year: 2023, engine: "286cc", type: "Street", color: "Vermelha" }
];

async function loadMotos() {
    try {
        allMotos = hondaMotos; 
        currentPage = 1;
        displayMotos();
    } catch (error) {
        console.error('Erro ao carregar as motos:', error);
        alert('Não foi possível carregar as motos.');
    }
}

async function createMotoCard(moto) {
    const motoContainer = document.getElementById('moto-container');
    const card = document.createElement('div');
    card.className = 'moto-card';

    card.innerHTML = `
        <div class="moto-card-body">
            <div class="moto-name">${moto.model}</div>
            <p class="moto-info"><span>Ano:</span> ${moto.year}</p>
            <p class="moto-info"><span>Cilindrada:</span> ${moto.engine}</p>
            <p class="moto-info"><span>Tipo:</span> ${moto.type}</p>
            <p class="moto-info"><span>Cor:</span> ${moto.color}</p>
        </div>
    `;

    motoContainer.appendChild(card);
}

function displayMotos() {
    const motoContainer = document.getElementById('moto-container');
    motoContainer.innerHTML = '';

    const start = (currentPage - 1) * motosPerPage;
    const end = start + motosPerPage;

    const paginatedMotos = allMotos.slice(start, end);

    paginatedMotos.forEach(createMotoCard);

    document.getElementById('prev-btn').disabled = currentPage === 1;
    document.getElementById('next-btn').disabled = end >= allMotos.length;
}

function changePage(direction) {
    currentPage += direction;
    displayMotos();
}

document.getElementById('load-motos-btn').addEventListener('click', loadMotos);
