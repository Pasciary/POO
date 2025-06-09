class MinhaClasse:
    
    def __init__(self, info, elem): # metodo construtor, construir os atributos.
        print("Estou no construtor")
        self.atributo1 = "Meu atributo"
        self.atributo2 = [1, 2, "a"]
        self.atributo3 = elem
        self.atributo_novo = info
        print(self.atributo_novo)
    
    
    
    def metodo1(self):
        print("Minha ação 1")
        print(self.atributo3)
        return "Olá mundo!"
    
    
    def metodo2(self,numero):
        print(self.atributo2[1] + numero)
    
        
#objeto         #classe -> instanciamos um objeto
minha_classe = MinhaClasse("Info aqui no construtor", 2020)


response = minha_classe.metodo1()

print(response)

minha_classe.metodo2(3)