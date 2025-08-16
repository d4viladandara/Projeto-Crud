from flask import Blueprint, render_template, request, redirect, url_for
from database.conection import get_connection

bp = Blueprint("main", __name__)

# ------------------ Categorias ------------------
@bp.route("/categorias")
def listar_categorias():
    conn = get_connection()
    categorias = conn.execute("SELECT * FROM categorias").fetchall()
    conn.close()
    return render_template("listar_categorias.html", categorias=categorias)

@bp.route("/categorias/nova", methods=["GET", "POST"])
def nova_categoria():
    if request.method == "POST":
        nome = request.form["nome"]
        descricao = request.form["descricao"]

        conn = get_connection()
        conn.execute("INSERT INTO categorias (nome, descricao) VALUES (?, ?)", (nome, descricao))
        conn.commit()
        conn.close()
        return redirect(url_for("main.listar_categorias"))
    return render_template("editar_categoria.html")

@bp.route("/categorias/<int:id>/editar", methods=["GET", "POST"])
def editar_categoria(id):
    conn = get_connection()
    categoria = conn.execute("SELECT * FROM categorias WHERE id=?", (id,)).fetchone()

    if request.method == "POST":
        nome = request.form["nome"]
        descricao = request.form["descricao"]
        conn.execute("UPDATE categorias SET nome=?, descricao=? WHERE id=?", (nome, descricao, id))
        conn.commit()
        conn.close()
        return redirect(url_for("main.listar_categorias"))

    conn.close()
    return render_template("editar_categoria.html", categoria=categoria)

@bp.route("/categorias/<int:id>/excluir")
def excluir_categoria(id):
    conn = get_connection()
    conn.execute("DELETE FROM categorias WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("main.listar_categorias"))

# ------------------ Produtos ------------------
@bp.route("/produtos")
def listar_produtos():
    conn = get_connection()
    produtos = conn.execute("""
        SELECT p.id, p.nome, p.preco, c.nome as categoria
        FROM produtos p
        LEFT JOIN categorias c ON p.categoria_id = c.id
    """).fetchall()
    conn.close()
    return render_template("listar_produtos.html", produtos=produtos)

@bp.route("/produtos/novo", methods=["GET", "POST"])
def novo_produto():
    conn = get_connection()
    categorias = conn.execute("SELECT * FROM categorias").fetchall()

    if request.method == "POST":
        nome = request.form["nome"]
        preco = request.form["preco"]
        categoria_id = request.form["categoria_id"]

        conn.execute("INSERT INTO produtos (nome, preco, categoria_id) VALUES (?, ?, ?)", 
        (nome, preco, categoria_id))
        conn.commit()
        conn.close()
        return redirect(url_for("main.listar_produtos"))

    conn.close()
    return render_template("editar_produto.html", categorias=categorias)

@bp.route("/produtos/<int:id>/editar", methods=["GET", "POST"])
def editar_produto(id):
    conn = get_connection()
    produto = conn.execute("SELECT * FROM produtos WHERE id=?", (id,)).fetchone()
    categorias = conn.execute("SELECT * FROM categorias").fetchall()

    if request.method == "POST":
        nome = request.form["nome"]
        preco = request.form["preco"]
        categoria_id = request.form["categoria_id"]

        conn.execute("UPDATE produtos SET nome=?, preco=?, categoria_id=? WHERE id=?", 
        (nome, preco, categoria_id, id))
        conn.commit()
        conn.close()
        return redirect(url_for("main.listar_produtos"))

    conn.close()
    return render_template("editar_produto.html", produto=produto, categorias=categorias)

@bp.route("/produtos/<int:id>/excluir")
def excluir_produto(id):
    conn = get_connection()
    conn.execute("DELETE FROM produtos WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("main.listar_produtos"))
