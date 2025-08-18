import repositories as repo

class ProdutoService:
    @staticmethod
    def listar_produtos():
        return repo.ProdutoRepository.get_all()

    @staticmethod
    def buscar_por_id(produto_id):
        return repo.ProdutoRepository.get_by_id(produto_id)

    @staticmethod
    def criar_produto(name, price, description, category_id):
        repo.ProdutoRepository.add(name, price, description, category_id)

    @staticmethod
    def atualizar_produto(produto_id, name, price, description, category_id):
        repo.ProdutoRepository.update(produto_id, name, price, description, category_id)

    @staticmethod
    def deletar_produto(produto_id):
        repo.ProdutoRepository.delete(produto_id)
