class Pessoa:
    def __init__(self, altura, idade):
        self.altura = altura
        self.idade = idade
        
    
    def comer(self):
        print("Estou comendo")
        
        
    def correr(self):
        print("Estou correndo")
        

joao = Pessoa(170, 23)

joao.comer()

joao.correr()