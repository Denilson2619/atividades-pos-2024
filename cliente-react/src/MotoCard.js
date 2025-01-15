import React from 'react';

function MotoCard({ moto }) {
    return (
        <div className="moto-card">
            <div className="moto-card-body">
                <div className="moto-name">{moto.model}</div>
                <p className="moto-info"><span>Ano:</span> {moto.year}</p>
                <p className="moto-info"><span>Cilindrada:</span> {moto.engine}</p>
                <p className="moto-info"><span>Tipo:</span> {moto.type}</p>
                <p className="moto-info"><span>Cor:</span> {moto.color}</p>
            </div>
        </div>
    );
}

export default MotoCard;
