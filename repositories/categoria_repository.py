from models import db, Categoria

class CategoriaRepository:
    @staticmethod
    def get_all():
        return Categoria.query.all()

    @staticmethod
    def get_by_id(categoria_id):
        return Categoria.query.get(categoria_id)

    @staticmethod
    def add(name, description):
        nova = Categoria(name=name, description=description)
        db.session.add(nova)
        db.session.commit()

    @staticmethod
    def update(categoria_id, description):
        categoria = Categoria.query.get(categoria_id)
        if categoria:
            categoria.description = description
            db.session.commit()

    @staticmethod
    def delete(categoria_id):
        categoria = Categoria.query.get(categoria_id)
        if categoria:
            db.session.delete(categoria)
            db.session.commit()
