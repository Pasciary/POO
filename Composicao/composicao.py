class Select:
    def by_id(self) -> any:
        print("Selecionando um elemento no DB.")


class Insert:
    def inser_value(self) -> None:
        print("Inserindo um valor no banco de dados.")
        

class Repositorio:
    def __init__(self): # Composição, chama diretamente a Classe
        self.__select = Select()
        self.__insert = Insert()
        
    def select_by_id(self, id: int) -> any:
        self.__select.by_id()
        
        
repo = Repositorio()
repo.select_by_id(45)