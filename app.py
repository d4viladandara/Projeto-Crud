from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

# ---------- MODELO ----------
class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    produtos = db.relationship('Produto', backref='categoria', lazy=True)

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200))
    category_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))

# ---------- ROTAS ----------
@app.route('/')
def index():
    return render_template('index.html')



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





# ---------- ROTAS PRODUTOS----------
# ---------- LISTAR PRODUTOS ----------
@app.route('/produtos')
def listar_produtos():
    produtos = Produto.query.all()
    categorias = Categoria.query.all()  # para exibir no select
    return render_template('produtos.html', produtos=produtos, categorias=categorias)

# ---------- CRIAR PRODUTO ----------
@app.route('/produtos/create', methods=['POST'])
def criar_produto():
    name = request.form['name']
    price = request.form['price']
    description = request.form['description']
    category_id = request.form['category_id']

    novo_produto = Produto(
        name=name,
        price=price,
        description=description,
        category_id=category_id
    )
    db.session.add(novo_produto)
    db.session.commit()
    return redirect('/produtos')

# ---------- ATUALIZAR PRODUTO ----------
@app.route('/produtos/update/<int:id>', methods=['POST'])
def atualizar_produto(id):
    produto = Produto.query.get(id)
    if produto:
        produto.name = request.form['name']
        produto.price = request.form['price']
        produto.description = request.form['description']
        produto.category_id = request.form['category_id']
        db.session.commit()
    return redirect('/produtos')

# ---------- DELETAR PRODUTO ----------
@app.route('/produtos/delete/<int:id>', methods=['POST'])
def deletar_produto(id):
    produto = Produto.query.get(id)
    if produto:
        db.session.delete(produto)
        db.session.commit()
    return redirect('/produtos')


# ---------- MAIN ----------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)