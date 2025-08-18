import repositories as repo

class CategoriaService:
    @staticmethod
    def listar_categorias():
        return repo.CategoriaRepository.get_all()

    @staticmethod
    def buscar_por_id(categoria_id):
        return repo.CategoriaRepository.get_by_id(categoria_id)

    @staticmethod
    def criar_categoria(name, description):
        repo.CategoriaRepository.add(name, description)

    @staticmethod
    def atualizar_categoria(categoria_id, description):
        repo.CategoriaRepository.update(categoria_id, description)

    @staticmethod
    def deletar_categoria(categoria_id):
        repo.CategoriaRepository.delete(categoria_id)
