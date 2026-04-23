# Entrada 1:    cafe leite pao leite pao pao    SAÍDA: pao
# -------------------------------------------------------
# Entrada 2:    arroz feijao arroz feijao       SAÍDA: arroz
# -------------------------------------------------------
# Lê a linha de entrada e separa os produtos em uma lista
produtos = input().strip().split()

mais_frequente = None
maior_contagem = -1

# TODO: Crie uma estrutura para contar quantas vezes cada produto aparece na lista
# TODO: Obtenha a contagem do produto atual e atualize mais_frequente se necessário


for produto in produtos: 
  counter = produtos.count(produto)
  if counter > maior_contagem:      # Usa operador 'maior que' para dar mais peso para o 1° valor
    mais_frequente = produto        # Define o produto mais frequente como o com maior aparições
    maior_contagem = counter        # Atualiza a qtde de quem apareceu mais vezes
    

# Imprima o produto mais frequente
print(mais_frequente)
