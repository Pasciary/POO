class Interruptor:
    def __init__(self, comodo: str) -> None:
       self.comodo = comodo
       
       
    def acender(self):
        print(f'Estou acendendo a luz do comodo: {self.comodo}') 
        
        
    
    def apagar(self) -> None:
        print(f'Estou apagando a luz do comodo: {self.comodo}')
        
        
        
        
class Pessoa:
    
    def acender_luz(self, interruptor: Interruptor):
        interruptor.acender()  # Só aparece por conta da tipagem
        
        
    def apagar_luz(self, interruptor: Interruptor):
        interruptor.apagar()  # Só aparece por conta da tipagem
        
        
        
    def dormir(self):
        print("A pessoa foi dormir.")
        
        

agnaldo = Pessoa()
Interruptor_sala = Interruptor("Sala")

agnaldo.acender_luz(Interruptor_sala)