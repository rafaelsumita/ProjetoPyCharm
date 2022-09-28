# EXERCÍCIO 1
# Desenvolva um algoritmo que solicite ao usuário o preço de um produto
# e um percentual de desconto a ser aplicado a ele.
# Calcule e exiba o valor de desconto e o preço final do produto

#Algoritmoinicio
#VAR
preco = float(input('Digite o preço do produto: ')) #o resultado da saída de um input é SEMPRE uma string, portanto preciso usar o float
percentual = float(input('Digite o percentual de desconto (0-100%): '))

desconto = preco * (percentual / 100)
final = preco - desconto # ps: outra forma para se calcular porcentagem é a seguinte equação: x.porcentagem / 100 ou seja,

print(f'O Preço do produto: R${preco}. Desconto de {percentual}%.')
print(f'Valor calculado de desconto: R${desconto}. Valor final do produto: R${final}')
#Fim


