import React from 'react';

function VulnerabilidadeItem({ vulnerabilidade, onEditar, onExcluir }) {
  return (
    <li className="list-group-item d-flex justify-content-between align-items-start">
      <div>
        <h5>{vulnerabilidade.titulo}</h5>  {/* Título */}
        <p>
          <strong>Descrição:</strong> {vulnerabilidade.descricao}<br/>
          <strong>Criticidade:</strong> {vulnerabilidade.criticidade}
        </p>
      </div>
      <div>
        <button 
          className="btn btn-sm btn-warning me-2" 
          onClick={() => onEditar(vulnerabilidade)}
        >
          Editar
        </button>
        <button 
          className="btn btn-sm btn-danger" 
          onClick={() => onExcluir(vulnerabilidade.id)}
        >
          Excluir
        </button>
      </div>
    </li>
  );
}

export default VulnerabilidadeItem;
