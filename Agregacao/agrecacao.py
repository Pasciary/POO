class Produto:
    def __init__(self, nome: str, valor: int):
        self.__nome = nome
        self.__valor = valor
        
    def informacoes_produto(self) -> None:
        print(f'Produto: {self.__nome} - Valor: {self.__valor}')
        


class CarrinhoCompras:
    def __init__(self) -> None:
        self.__produtos = [] # Corrigido: Agora __produtos é uma lista vazia de verdade.
        
    def adicionar_produto(self, produto: Produto) -> None:
        self.__produtos.append(produto)
        
        
    def finalizar_compra(self) -> None:
        print('Compra Finalizada!')
        print('          Produtos:')
        for prod in self.__produtos:
            prod.informacoes_produto()
            
            
            
            
banana = Produto('Banana', 3)
peira = Produto('Peira', 2)
uva = Produto('Uva', 5)

carrinho = CarrinhoCompras()

carrinho.adicionar_produto(banana)
carrinho.adicionar_produto(peira)
carrinho.adicionar_produto(uva)

carrinho.finalizar_compra()