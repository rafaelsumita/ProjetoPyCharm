# EXERCÍCIO 2
# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$ 60 por dia e R$ 0,15 por km rodado

#Algoritmo Aluguel de carro Km
#VAR
km = int(input('Quantos Km foram percorridos?'))
dias = int(input('Por quantos dias ele foi alugado?'))

preco = (60 * dias) + 0.15 * km
#Para fazer este calculo basta eu multiplicar o preço da diária x dias alugados
#Somar(+) o resultado dos Kms percorridos que é: Km informado x o preçodo km 0.15

print(f'Km = {km}. Dias: {dias}')
print(f'Valor a ser pago: R${preco}')
#Fim