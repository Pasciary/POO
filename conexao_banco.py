class ConnectionDB:
    def conectar(self):
        print('Conectando ao Banco')
        
        
class SqlRepository(ConnectionDB):
    def select(self):
        print('Buscando dados no banco no SQL')
        
                
class NoSqlRepository(ConnectionDB):
    def select(self):
        print('Buscando dados no banco no NoSQL')
        

        
class DBHandler(): # Vai dar erro se colocar o NoSQL ficar como classe pois da erro, não tem essa herança
    def altertable(self):
        print('Alterando na tabela em SQL')
        
        