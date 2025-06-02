import React, { useState, useEffect } from 'react';
import FormVulnerabilidade from './FormVulnerabilidade';
import ListaVulnerabilidades from './ListaVulnerabilidades';

const API_URL = 'http://127.0.0.1:8000/vulnerabilidades';

function App() {
  const [vulnerabilidades, setVulnerabilidades] = useState([]);
  const [editando, setEditando] = useState(null);

  const carregarVulnerabilidades = () => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => setVulnerabilidades(data));
  };

  useEffect(() => {
    carregarVulnerabilidades();
  }, []);

  const salvarVulnerabilidade = (vuln) => {
    const metodo = vuln.id ? 'PUT' : 'POST';
    const url = vuln.id ? `${API_URL}/${vuln.id}` : API_URL;

    fetch(url, {
      method: metodo,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(vuln)
    }).then(() => {
      setEditando(null);
      carregarVulnerabilidades();
    });
  };

  const excluirVulnerabilidade = (id) => {
    if (window.confirm('Tem certeza que deseja excluir?')) {
      fetch(`${API_URL}/${id}`, { method: 'DELETE' })
        .then(() => carregarVulnerabilidades());
    }
  };

  return (
    <div className="container mt-5">
      <h1 className="mb-4">Gerenciador de Vulnerabilidades</h1>
      <FormVulnerabilidade 
        onSalvar={salvarVulnerabilidade} 
        editando={editando} 
        cancelar={() => setEditando(null)} 
      />
      <ListaVulnerabilidades 
        vulnerabilidades={vulnerabilidades} 
        onEditar={setEditando} 
        onExcluir={excluirVulnerabilidade} 
      />
    </div>
  );
}

export default App;
