from elementos.Interfaces.elemento_interface import ElementoInterface
from elementos.elemento import Elemento

class Principal:
    def __init__(self, elem: ElementoInterface) -> None:
        self.__elem = elem

    def run(self) -> None:
        self.__elem.executar()
        print('Estou finalizando na classe principal')
        
    
el = Elemento()    
        
cl1 = Principal(el)
cl1.run()