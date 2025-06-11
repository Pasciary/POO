class Loja:
    
    taxa: float = 1.15
    
    def __init__(self, valor: float):
        self.valor_produto_bruto = valor
        
        
    def consultar_valor(self):
        valor = self.valor_produto_bruto * self.taxa
        print(f'O valor do seu produto é {valor:.4f}')
        
    
    @classmethod
    def editar_taxa_produto(cls, valor:float):
        cls.taxa = valor
    
    
loja_praia = Loja(30.50)
loja_shopping = Loja(10.39)
loja_rua = Loja(20.33)


loja_praia.consultar_valor()
loja_shopping.consultar_valor()
loja_shopping.consultar_valor()


loja_shopping.editar_taxa_produto(1.35)


loja_praia.consultar_valor()
loja_shopping.consultar_valor()
loja_shopping.consultar_valor()