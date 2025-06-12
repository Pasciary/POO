class ConectorBancoDeDados:
    def __init__(self) -> None:
        self.connection = None
        
    
    def conectar_ao_banco(self) -> None:
        self.connection = True
        
        

class RepositorioDeBanco:
    def __init__(self, conexao: ConectorBancoDeDados) -> None:
        self.__conexao = conexao
        
    def busca_dados(self) -> list:
        if self.__conexao.connection:
            return [1, 2, 3, 4, 5]
        
        return None
    
    
class RegraNegocio:
    def __init__(self, repo: RepositorioDeBanco) -> None:
        self.__repo = repo
            
            
    def calcular_resultado(self):
        dados = self.__repo.busca_dados()
        if not dados:
            print('Dados nao encontrados. Verifique sua conexao com o banco de dados')
            
        else:
            resposta = 0
            for dado in dados:
                resposta += dado
            print(f'o resultado é: {resposta}')
            
            
            
            
con = ConectorBancoDeDados() # Criando instancia do Banco
con.conectar_ao_banco() # Conectando ao Banco

repo = RepositorioDeBanco(con) # Colocando o banco no repositorio
regra = RegraNegocio(repo) # Colocando o repositorio dentro da regra

regra.calcular_resultado() # Calculando resultado