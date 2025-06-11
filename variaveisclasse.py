class MinhaClasse:
    
    estatico = "Lhama"
    
    def __init__(self, estado):
        self.estado = estado
        
    
    def print_varaivel(self):
        print(self.estatico)
        
    
    @classmethod # Decorador para mexer com a classe
    def alteracao_da_varaivel(cls):
        cls.estatico = "alguma coisa"
       #MinhaClasse.estatico = "alguma coisa"
        
        
obj1 = MinhaClasse(True)
obj2 = MinhaClasse(True)

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)

obj1.alteracao_da_varaivel()

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)