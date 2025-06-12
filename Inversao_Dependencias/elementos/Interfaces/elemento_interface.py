from abc import ABC, abstractclassmethod

class ElementoInterface(ABC):
    
    @classmethod
    @abstractclassmethod
    def executar(self) -> None: pass
       