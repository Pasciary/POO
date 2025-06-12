from abc import ABC, abstractclassmethod
# Elementos abstrados, ABC é uma classe criadora de classes abstratas

class Pessoa(ABC): # Classe abstrata não possui objetos - só pode ser mae da herança.
    def correr(self):
        print('A pessoa esta correndo de manha')
        
    @classmethod # Chama os metodos da classe
    @abstractclassmethod # Classe filha DEVE criar um metodo trabalhar.
    def trabalhar(cls):
        pass
    
    
class Professor(Pessoa):
    def trabalhar(self):
        print('O professor esta dando aula.')


class Cozinheiro(Pessoa):
    def trabalhar(self):
        print('O professor esta dando aula.')


p1 = Professor() # Daria erro
p1.correr()