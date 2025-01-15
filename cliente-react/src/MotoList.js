// src/MotoList.js
import React, { useState } from 'react';
import MotoCard from './MotoCard';

function MotoList({ motos }) {
    const [currentPage, setCurrentPage] = useState(1);
    const motosPerPage = 6;

    const paginate = (direction) => {
        setCurrentPage(prevPage => prevPage + direction);
    };

    const start = (currentPage - 1) * motosPerPage;
    const end = start + motosPerPage;
    const paginatedMotos = motos.slice(start, end);

    return (
        <div>
            <div id="moto-container">
                {paginatedMotos.map((moto, index) => (
                    <MotoCard key={index} moto={moto} />
                ))}
            </div>

            <div className="pagination-container">
                <button
                    className="pagination-btn"
                    onClick={() => paginate(-1)}
                    disabled={currentPage === 1}
                >
                    Anterior
                </button>
                <button
                    className="pagination-btn"
                    onClick={() => paginate(1)}
                    disabled={end >= motos.length}
                >
                    Próximo
                </button>
            </div>
        </div>
    );
}

export default MotoList;
