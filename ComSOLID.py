class SistemaCadastral:
    
    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__validar_cadastro(nome, idade):
            self.__registra_user(nome, idade)
        else:
            self.__tratamento_erro()
            
            
    def __validar_cadastro(self, nome: str, idade: int) -> bool:
        return isinstance(nome, str) and isinstance(idade, int)
    
    
    def __registra_user(self, nome: str, idade:int) -> None:
        print("Acessando o banco de dados...")
        print(f'Cadastrar usuário {nome}, e sua idade {idade}')
    
    
    def __tratamento_erro(self) -> None:
        print("dados invalidos.")
    

sistema = SistemaCadastral()

sistema.cadastrar("João Pachere", "23")

sistema.cadastrar("João Pachere", 23)