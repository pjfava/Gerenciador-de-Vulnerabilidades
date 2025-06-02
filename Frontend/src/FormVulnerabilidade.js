import React, { useState, useEffect } from 'react';

function FormVulnerabilidade({ onSalvar, editando, cancelar }) {
  const [titulo, setTitulo] = useState('');
  const [descricao, setDescricao] = useState('');
  const [criticidade, setCriticidade] = useState('');

  useEffect(() => {
    if (editando) {
      setTitulo(editando.titulo);
      setDescricao(editando.descricao);
      setCriticidade(editando.criticidade);
    } else {
      setTitulo('');
      setDescricao('');
      setCriticidade('');
    }
  }, [editando]);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSalvar({ id: editando?.id, titulo, descricao, criticidade });
  };

  return (
    <form onSubmit={handleSubmit} className="card p-3 mb-4">
      <div className="mb-3">
        <label className="form-label">Título</label>
        <input 
          type="text" 
          className="form-control" 
          value={titulo} 
          onChange={e => setTitulo(e.target.value)} 
          required 
        />
      </div>
      <div className="mb-3">
        <label className="form-label">Descrição</label>
        <textarea 
          className="form-control" 
          value={descricao} 
          onChange={e => setDescricao(e.target.value)} 
          required 
        />
      </div>
      <div className="mb-3">
        <label className="form-label">Criticidade</label>
        <input 
          type="text" 
          className="form-control" 
          value={criticidade} 
          onChange={e => setCriticidade(e.target.value)} 
          required 
        />
      </div>
      <button type="submit" className="btn btn-primary">Salvar</button>
      {editando && (
        <button type="button" className="btn btn-secondary ms-2" onClick={cancelar}>
          Cancelar Edição
        </button>
      )}
    </form>
  );
}

export default FormVulnerabilidade;
