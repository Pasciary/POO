# Não usa 100% do SOLID, single, essa classe cria o artista e controla o circo.
class Circo:
    
    def __init__(self, pessoa: str):
        self.pessoa = pessoa
    
    def apresentar(self) ->None:
        print(f'O {self.pessoa} esta apresentando seu show')

        
        
        
show_magico = Circo("Magico")
show_palhaço = Circo("palhaço")
show_malabarista = Circo("malabarista")



show_magico.apresentar()
show_malabarista.apresentar()
show_palhaço.apresentar()