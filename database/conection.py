import sqlite3
from flask import g
from app import app

# Caminho do banco de dados
DATABASE = 'app/database/database.db'

# Retorna conexão ativa ou cria nova
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row  # Permite acessar colunas pelo nome
    return db

# Fecha conexão quando a aplicação encerra
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Inicializa o banco a partir do arquivo base.sql
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('database/base.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
