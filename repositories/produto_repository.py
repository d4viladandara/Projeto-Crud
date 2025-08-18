from models import db, Produto

class ProdutoRepository:
    @staticmethod
    def get_all():
        return Produto.query.all()

    @staticmethod
    def get_by_id(produto_id):
        return Produto.query.get(produto_id)

    @staticmethod
    def add(name, price, description, category_id):
        novo = Produto(name=name, price=price, description=description, category_id=category_id)
        db.session.add(novo)
        db.session.commit()

    @staticmethod
    def update(produto_id, name, price, description, category_id):
        produto = Produto.query.get(produto_id)
        if produto:
            produto.name = name
            produto.price = price
            produto.description = description
            produto.category_id = category_id
            db.session.commit()

    @staticmethod
    def delete(produto_id):
        produto = Produto.query.get(produto_id)
        if produto:
            db.session.delete(produto)
            db.session.commit()
