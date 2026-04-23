class Passaro:
    def voar(self):
        print(" Voando . . .")

class Pardal(Passaro):
    def voar(self):
        print(f" {self.__class__.__name__}:", end='')
        {super().voar()}

class Avestruz(Passaro):
    def voar(self):
        print(f" {self.__class__.__name__}:", end='')
        print(" não pode voar!")

def tentar_voar(objeto):
    objeto.voar()


obj_01 = Pardal()
obj_02 = Avestruz()


tentar_voar(obj_01)
tentar_voar(obj_02)

