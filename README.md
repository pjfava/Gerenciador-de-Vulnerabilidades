
# 🔐 Gerenciador de Vulnerabilidades

## 📌 Descrição do Projeto

O Gerenciador de Vulnerabilidades é uma aplicação desenvolvida com o objetivo de registrar, acompanhar, atualizar e excluir vulnerabilidades de segurança detectadas em sistemas, servidores ou redes.

Este projeto foi desenvolvido como parte da disciplina **Tecnologias Emergentes**, atendendo ao requisito de criar uma aplicação funcional com operações CRUD (**Create, Read, Update e Delete**) e persistência de dados em banco de dados.

---

## 🎯 Objetivo da Aplicação

Auxiliar profissionais e equipes de segurança da informação a manter o controle sobre vulnerabilidades conhecidas, monitorando seu status e a evolução do processo de correção, de forma centralizada e prática.

---

## 🛠️ Tecnologias utilizadas

### Backend:
- Linguagem de Programação: **Python 3.x**
- Framework: **FastAPI**
- Banco de Dados: **SQLite**
- ORM: **SQLAlchemy**
- Ferramentas de Teste: **Swagger UI** / **Postman**

### Frontend:
- **ReactJS**
- **Axios** — integração com API
- **Bootstrap** — estilização

### Ferramentas de Desenvolvimento:
- IDE: **Visual Studio Code**
- Gerenciador de Pacotes: **pip** / **npm**
- Hospedagem de Código: **GitHub**

---

## 🚧 Status do Projeto

✅ **Concluído** — Etapa Final: Desenvolvimento Full Stack com integração entre Frontend e Backend.

---

## 🗂️ Estrutura do Projeto

```
Gerenciador-de-Vulnerabilidades/
├── Backend/
│   ├── app/
│   │   ├── crud.py
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   ├── requirements.txt
│   └── vulnerabilidades.db (gerado automaticamente)
│
├── Frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.js
│   │   ├── FormVulnerabilidade.js
│   │   ├── ListaVulnerabilidades.js
│   │   ├── VulnerabilidadeItem.js
│   │   └── index.js
│   ├── package.json
│   └── package-lock.json
│
├── README.md
└── .gitignore
```

---

## 🚀 Como executar o projeto

### ✅ Pré-requisitos

- **Node.js** >= 14.x
- **Python** >= 3.8
- **npm** / **pip** instalados

---

## 🔧 Backend

### 1. Acessar o diretório:

```bash
cd Backend
```

### 2. Criar ambiente virtual:

```bash
python -m venv venv
```

### 3. Ativar ambiente virtual:

- **Windows**: `venv\Scripts\activate`
- **Linux/macOS**: `source venv/bin/activate`

### 4. Instalar dependências:

```bash
pip install -r requirements.txt
```

### 5. Executar a aplicação:

```bash
uvicorn app.main:app --reload
```

➡️ API disponível em: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
➡️ Documentação interativa: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🎨 Frontend

### 1. Acessar o diretório:

```bash
cd Frontend
```

### 2. Instalar dependências:

```bash
npm install
```

### 3. Executar a aplicação:

```bash
npm start
```

➡️ Aplicação disponível em: [http://localhost:3000](http://localhost:3000)

---

## ✅ Observações importantes

- O banco `vulnerabilidades.db` será criado automaticamente ao iniciar o backend.
- Se quiser compartilhar um exemplo pré-preenchido, pode subir este arquivo no repositório.
- O frontend consome a API desenvolvida no backend via **Axios**.
- CORS foi configurado para permitir o funcionamento local.

```

➡️ Em seguida, siga as instruções de **Backend** e **Frontend**.

---

## ✅ Requisitos para rodar

- Python 3.8+
- Node.js 14+
- npm
- pip

---
## ✅ Sistema rodando
![image](https://github.com/user-attachments/assets/71a19d7d-433e-47f5-931f-72491e55da96)

---

## 👤 Desenvolvido por

- **Nome:** Paulo Fava  
- **Curso:** Análise e Desenvolvimento de Sistemas  
- **Disciplina:** Tecnologias Emergentes  
