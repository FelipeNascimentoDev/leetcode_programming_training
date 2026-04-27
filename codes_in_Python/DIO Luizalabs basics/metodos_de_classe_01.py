class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    @classmethod    # Pode ser usado para criar uma "fábrica"
    def criar_pessoa_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2026 - ano
        return cls(nome, idade)
    

    @staticmethod   # Não usa instância da calsse!
    def is_maior_de_idade(idade):
        return idade >= 18
    


p = Pessoa.criar_pessoa_apartir_data_nascimento(2000, 10, 11, "Carl")
print(p.nome, p.idade, sep=" - ")

print(Pessoa.is_maior_de_idade(17))
print(Pessoa.is_maior_de_idade(19))
print(f"{p.nome} é maior de idade? {p.is_maior_de_idade(26)}")