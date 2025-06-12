class Mamifero:
    def __init__(self, localizacao: str) -> None:
        self.localizacao = localizacao
        
        
    def andar(self) -> None:
        print(f'O Animal esta andando pelo {self.localizacao}')
        
   
class Cachorro(Mamifero): # Tendo a relação de Herança de mamiferos.
    
    def __init__(self, localizacao): # Construtor de Cachorro
        super().__init__(localizacao) # Se refere ao construtor da classe superior
    
    def latir(self) -> None:
        print('O cachoro esta latindo')
        self.andar()
        
        
pug = Cachorro("Brazil")
pug.andar()