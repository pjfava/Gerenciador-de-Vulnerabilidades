import React from 'react';
import VulnerabilidadeItem from './VulnerabilidadeItem';

function ListaVulnerabilidades({ vulnerabilidades, onEditar, onExcluir }) {
  return (
    <div>
      <h2>Vulnerabilidades</h2>
      <ul className="list-group">
        {vulnerabilidades.map(vuln => (
          <VulnerabilidadeItem 
            key={vuln.id} 
            vulnerabilidade={vuln} 
            onEditar={onEditar} 
            onExcluir={onExcluir} 
          />
        ))}
      </ul>
    </div>
  );
}

export default ListaVulnerabilidades;
