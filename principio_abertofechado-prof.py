class Artista:
    def __init__(self, pessoa: str):
        self.pessoa = pessoa
    
    def apresentar_show(self) ->None:
        print(f'O {self.pessoa} esta apresentando seu show')


class Circo:
    def apresentar(self, artista: Artista):
        print("O circo esta abrindo")
        artista.apresentar_show()
        print("O publico aplaude!!")
        
        
        
circo = Circo()
palhaço = Artista('Palhaço')
malabarista = Artista('Malabarista')
magico = Artista('Magico')


circo.apresentar(magico)