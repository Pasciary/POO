class Mamifero:
    def __init__(self, localizacao: str) -> None:
        self.localizacao = localizacao
        self._tamanho = 1.23
        
        
    def andar(self) -> None:
        print(f'O Animal esta andando pelo {self.localizacao}')
    
    
    def _dormir(self) -> None: # Metodo protegido utiliza um unico underline
        print('O animal esta dormindo')
   
class Cachorro(Mamifero): # Tendo a relação de Herança de mamiferos.
    
    def __init__(self, localizacao): # Construtor de Cachorro
        super().__init__(localizacao) # Se refere ao construtor da classe superior
    
    def latir(self) -> None:
        print('O cachoro esta latindo')
        self.andar()
        self._dormir()
        
        
pug = Cachorro("Brazil")
pug.latir()
pug._dormir() # Não deveria funcionar, em outras linguas não funcionaria, é uma convenção.
print(pug._tamanho)