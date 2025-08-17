from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

# ---------- MODELO ----------
class Categoria(db.Model):  # singular (representa UMA categoria)
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), unique=True, nullable=False)
    
class Produtos(db.Model):  # singular (representa UMA categoria)
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), unique=True, nullable=False)


# ---------- ROTAS ----------
@app.route('/')
def index():
    return render_template('base.html')


# ----- LISTAR -----
@app.route('/categorias')
def categorias():
    categorias = Categoria.query.all()
    return render_template('categorias.html', categorias=categorias)



# ----- CRIAR -----
@app.route('/categorias/create', methods=['POST'])
def criar_categoria():
    description = request.form['description']

    # verificar duplicado
    existe = Categoria.query.filter_by(description=description).first()
    if existe:
        return 'Erro: Categoria já cadastrada'

    nova = Categoria(description=description)
    db.session.add(nova)
    db.session.commit()
    return redirect('/categorias')


# ----- DELETAR -----
@app.route('/categorias/delete/<int:id>', methods=['POST'])
def deletar_categoria(id):
    categoria = Categoria.query.get(id)  # singular pq é só uma
    if categoria:
        db.session.delete(categoria)
        db.session.commit()
    return redirect('/categorias')


# ----- ATUALIZAR -----
@app.route('/categorias/update/<int:id>', methods=['POST'])
def atualizar_categoria(id):
    categoria = Categoria.query.get(id)
    if categoria:
        categoria.description = request.form['description']
        db.session.commit()
    return redirect('/categorias')


# ---------- MAIN ----------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)



# ---------- ROTAS PRODUTOS----------
@app.route('/produtos')
def produtos():
    produtos = Produtos.query.all()
    return render_template('produtos.html', produtos=produtos)
