class ClasseQualquer:
    def fazer(self) -> None: # Essa linha é a assinatura do metodo
        print('Estou fazendo algo')
        
        
class OutraCoisa(ClasseQualquer):
    def preparar(self) -> None: # Essa linha é a assinatura do metodo
        print('Estou preparando algo')
   
    #def fazer(self) -> None: # Ele tem a mesma assinatura mas faz outra coisa.
    #    print('Estou fazendo outra coisa')  
        
        
def fazer_func() -> None: # Essa linha é a assinatura da função
    print('Estou fazendo outra coisa')  
    
    
obj1 = ClasseQualquer()
obj2 = OutraCoisa()

obj2.fazer = fazer_func

obj1.fazer()
obj2.fazer()