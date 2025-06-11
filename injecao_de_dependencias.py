class Celular:
    
    def __init__(self, modelo: str) -> None:
        self.modelo = modelo
    
    def enviar_mensagem(self, mensagem) -> None:
        print(f'enviando mensagem: {mensagem}')
        
    def abrir_emails(self) -> None:
        print('Abrindo os emails...')
        
        
    def abrir_youtube(self) -> None:
        print('Abrindo o Youtube...')
        


class Pessoa:
    
    def __init__(self, celular: Celular) -> None:
        self.__celular = celular
      
      
    def pedir_pizza(self) -> None:
        print('buscando o celular...')
        print('escolhendo o sabor...')
        self.__celular.enviar_mensagem('Quero uma pizza de calabreza')
        print('Aguardando chegada')
        
        
    def estudar(self) -> None:
        print('Abrindo o computador...')
        self.__celular.abrir_youtube()
        print('Fazendo anotações')
        
        
android = Celular('samsung')
ios = Celular('iphone')


reginaldo = Pessoa(android)
marlene = Pessoa(ios)


reginaldo.pedir_pizza()
print()
marlene.estudar()