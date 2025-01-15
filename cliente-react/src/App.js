// src/App.js
import React, { useState, useEffect } from 'react';
import MotoList from './MotoList';
import './style.css';

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

function App() {
    const [motos, setMotos] = useState([]);

    useEffect(() => {
        setMotos(hondaMotos);
    }, []);

    return (
        <div className="container">
            <h1>Catálogo de Motos</h1>
            <button
                className="btn-custom"
                onClick={() => setMotos(hondaMotos)}
            >
                Carregar Motos
            </button>
            <MotoList motos={motos} />
        </div>
    );
}

export default App;
