# 🐾 FindMyPet

**FindMyPet** é um projeto interdisciplinar do curso de **Análise e Desenvolvimento de Sistemas (ADS) da Fatec Franca**.  
O objetivo é criar uma plataforma que facilite o processo de **encontrar pets desaparecidos**, conectando tutores e a comunidade de forma simples e eficiente.  

---

## 🎯 Objetivos do Projeto
- Permitir o **cadastro de usuários** (tutores e voluntários).
- Enviar e armazenar **informações sobre pets desaparecidos**.
- Criar uma base de dados centralizada, com possibilidade de expansão para mapas e notificações.
- Desenvolver uma solução inicial simples, mas escalável para nuvem.

---

## 🛠️ Tecnologias Utilizadas

### Backend
- [FastAPI](https://fastapi.tiangolo.com/) → framework Python para APIs rápidas.
- [Uvicorn](https://www.uvicorn.org/) → servidor ASGI para rodar o FastAPI.
- [Pydantic](https://docs.pydantic.dev/) → validação de dados.
- [Motor](https://motor.readthedocs.io/) → driver assíncrono para MongoDB.
- [python-dotenv](https://pypi.org/project/python-dotenv/) → gerenciamento de variáveis de ambiente.
- [Jinja2](https://jinja.palletsprojects.com/) → renderização de templates HTML.

### Frontend
- **HTML5** → estrutura da página.
- **CSS3** → estilização.
- **JavaScript (Vanilla)** → integração com a API via `fetch`.

### Banco de Dados
- [MongoDB](https://www.mongodb.com/) → banco de dados NoSQL, ideal para dados flexíveis.
- Inicialmente rodando **localmente**, mas preparado para migrar para **MongoDB Atlas (nuvem)**.

---

## 📂 Estrutura do Projeto

FindMyPet/
│
├── app/
│ ├── main.py # Entrada da aplicação FastAPI
│ ├── database.py # Conexão com o banco
│ ├── models.py # Modelos Pydantic
│ ├── templates/ # Páginas HTML
│ │ └── index.html
│ ├── static/ # Arquivos estáticos (CSS/JS)
│ │ ├── style.css
│ │ └── script.js
│
├── .env # Configurações (ex.: URL do MongoDB)
├── requirements.txt # Dependências do projeto