class Circo:
    def apresentar(self, command: int) ->None:
        if command == 1:
            self.__show_palhaco()
        if command == 2:
            self.__show_malabarista()
            
            
    def __show_palhaco(self):
        print("O Palhaço esta apresentando sue show")
        
        
        
    def __show_malabarista(self):
        print("O Malabarista esta apresentando sue show")
        
        
        
circo = Circo()

command = 1
circo.apresentar(command)