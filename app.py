from flask import Flask, render_template, request, redirect
from models import db
import services as service

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)

# ---------- ROTAS ----------
@app.route('/')
def index():
    return render_template('index.html')

# ----- CATEGORIAS -----
@app.route('/categorias')
def listar_categorias():
    categorias = service.CategoriaService.listar_categorias()
    return render_template('categorias.html', categorias=categorias)

@app.route('/categorias/create', methods=['POST'])
def criar_categoria():
    name = request.form['name']
    description = request.form['description']
    service.CategoriaService.criar_categoria(name, description)
    return redirect('/categorias')

@app.route('/categorias/update/<int:id>', methods=['POST'])
def atualizar_categoria(id):
    description = request.form['description']
    service.CategoriaService.atualizar_categoria(id, description)
    return redirect('/categorias')

@app.route('/categorias/delete/<int:id>', methods=['POST'])
def deletar_categoria(id):
    service.CategoriaService.deletar_categoria(id)
    return redirect('/categorias')

# ----- PRODUTOS -----
@app.route('/produtos')
def listar_produtos():
    produtos = service.ProdutoService.listar_produtos()
    categorias = service.CategoriaService.listar_categorias()
    return render_template('produtos.html', produtos=produtos, categorias=categorias)

@app.route('/produtos/create', methods=['POST'])
def criar_produto():
    name = request.form['name']
    price = request.form['price']
    description = request.form['description']
    category_id = request.form['category_id']
    service.ProdutoService.criar_produto(name, price, description, category_id)
    return redirect('/produtos')

@app.route('/produtos/update/<int:id>', methods=['POST'])
def atualizar_produto(id):
    name = request.form['name']
    price = request.form['price']
    description = request.form['description']
    category_id = request.form['category_id']
    service.ProdutoService.atualizar_produto(id, name, price, description, category_id)
    return redirect('/produtos')

@app.route('/produtos/delete/<int:id>', methods=['POST'])
def deletar_produto(id):
    service.ProdutoService.deletar_produto(id)
    return redirect('/produtos')

# ---------- MAIN ----------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
