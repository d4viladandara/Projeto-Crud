<h1>Doce Amore - Confeitaria</h1>

<h2>📖 Sobre o projeto</h2>

Este projeto é uma aplicação web desenvolvida em Flask com o padrão de camadas (Repository e Service), utilizando SQLAlchemy para persistência de dados em SQLite.

O sistema possui duas entidades principais:
- **Categoria**
- **Produto** (relacionado a uma categoria por chave estrangeira)

O objetivo é gerenciar categorias e produtos de forma simples através de uma aplicação web.

---

<h2>📦 Estrutura das entidades</h2>

**Categoria**
- `id` → Identificador único (PK)
- `name` → Nome da categoria
- `created_at` → Data de criação

**Produto**
- `id` → Identificador único (PK)
- `name` → Nome do produto
- `price` → Preço
- `description` → Descrição
- `created_at` → Data de criação
- `category_id` → Chave estrangeira que referencia `Categoria.id`

---

<h2>🚀 Tecnologias utilizadas</h2>

- Python 3.11+
- Flask
- Flask-SQLAlchemy
- Jinja2 (templates)
- SQLite (banco de dados local)

---

<h2>🌐 Rotas principais</h2>

- `/` → Página inicial  
- `/categorias` → Listar e cadastrar categorias  
- `/produtos` → Listar e cadastrar produtos

<h2>👩‍💻 Autor</h2>
Projeto desenvolvido por D'Ávila Dandara da Nóbrega Amador
