from abc import ABC, abstractclassmethod


class Trabalhador(ABC): # Interface
    
    @classmethod
    @abstractclassmethod
    def trabalhar(self) -> None: pass
    
    @classmethod
    @abstractclassmethod
    def ir_para_casa(self) -> None: pass

    @classmethod
    @abstractclassmethod
    def consultar_beneficios(self) -> None: pass
    
    
class TrabalhadorTemporario(ABC): # Interface
    
    @classmethod
    @abstractclassmethod
    def trabalhar(self) -> None: pass
    
    @classmethod
    @abstractclassmethod
    def ir_para_casa(self) -> None: pass

     
class Professor(Trabalhador):

    def trabalhar(self) -> None:
        print('O Professor esta trabalhando')

    def ir_para_casa(self) -> None:
        print('O Professor esta indo para casa')

    def consultar_beneficios(self) -> None:
        print('Consultando beneficios da CLT')
    
    
class ProfessorSubstituto(TrabalhadorTemporario):

    def trabalhar(self) -> None:
        print('O Professor esta trabalhando')

    def ir_para_casa(self) -> None:
        raise Exception('O Professor Substituto não tem beneficios')


p2 = ProfessorSubstituto()