class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property      # 'Mal uso' do @propety, pois não adiciona 'lógica'. Seria melhor acessar o valor direto do construtor.
    def nome(self):
        return self._nome
    
    @property
    def idade(self):     # 'Bom uso' do @property, pois permite retornar um 'novo atributo' / adiciona lógica ao 'return'
        _ano_atual = 2026
        return _ano_atual - self._ano_nascimento
    

pessoa = Pessoa("Isaac", 2000)
print(f" Nome: {pessoa.nome}\n Idade: {pessoa.idade}")
