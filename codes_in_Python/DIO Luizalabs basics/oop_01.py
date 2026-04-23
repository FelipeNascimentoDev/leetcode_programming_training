class Bicicleta:
    def __init__(self, cor:str, modelo:str, ano:int, valor:float, velocidade:int = 0):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.velocidade = velocidade

    def buzinar(self):
        print("plim... plim...")

    def parar(self):
        print("Parando a bicicleta...")
        self.velocidade = 0
        print(f"Bicicleta parada! Velocidade: {self.velocidade}Km/h \t")

    def acelerar(self):
        self.velocidade += 2
        print(f"Acelerando! Velocidade: {self.velocidade}Km/h \t")


    # Jeito ruim de fazer
    # def __str__(self):
    #     return f"Bicicleta: 'cor --> {self.cor}' | 'modelo --> {self.modelo} | 'ano --> {self.ano}' | 'valor --> {self.valor}' "


    # Jeito BOM de fazer
    def __str__(self):
        return f"Nome da Classe: {self.__class__.__name__}. Dados da Classe: \n{', \n'.join([f"{chave.title()} = {valor}" for chave, valor in self.__dict__.items()])}"


Bike01 = Bicicleta("Vermelha", "Caloi", 2019, 639.90)

Bike01.buzinar()
Bike01.acelerar()
Bike01.acelerar()
Bike01.parar()


print(Bike01)


print("\n . . . E N D . . . \n")
