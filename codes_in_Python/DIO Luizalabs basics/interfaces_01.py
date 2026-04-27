from abc import ABC, abstractmethod     #Permite criar métodos abstratos e fazer INTERFACES

class ControleRemoto(ABC):

    @abstractmethod     # Ter métodos abstratos em uma Classe, ela não pode mais ser instanciada
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    def marca(self):
        pass


class ControleDeTV(ControleRemoto):
    def ligar(self):
        print(f"Ligando a TV....")
        print(f"\nLIGADA!\n")

    def desligar(self):
        print(f"Desligando a TV...")
        print(f"\nDESLIGADA!\n")

    @property
    def marca(self):
        return "Samsung"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        pass

    def desligar(self):
        pass

    def marca(self):
        return "LG"


controle_de_tv = ControleDeTV()
controle_de_tv.ligar()
controle_de_tv.desligar()
print(controle_de_tv.marca)
