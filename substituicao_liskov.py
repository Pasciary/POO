class Animal:
    def alimentar(self):
        print('O animal esta se alimentando')
        
        
class Cachorro(Animal):
    def latir(self):
        print('O cachorro esta latindo')
        

class Peixe(Cachorro):
    def nadar(self):
        print('O peixe esta nadando')
        
    def latir(self): # Comportamento diferente da classe mãe para filha
        raise Exception('Peixe não late')
    
    
def verificar_animal(animal: any):
    animal.latir()



obj1 = Animal()
obj2 = Cachorro()
obj3 = Peixe()

verificar_animal(obj3)