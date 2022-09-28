# EXERCÍCIO 3

# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
# Pergunte a quantidade de kWh consumida e o tipo de instalação:
# R para residências, I para indústrias e C para comércios
# Calcule o preço de acordo com a tabela a seguir:

# |    Preço por tipo e faixa de consumo   |
# | Tipo        | Faixa (kWh0  | Preço (R$)|
# |-------------|--------------|-----------|
# | Residencial | Até 500      | 0.40      |
# |             | Acima de 500 | 0.65      |
# | Comercial   | Até 1000     | 0.55      |
# |             | Acima de 1000| 0.60      |
# | Industrial  | Até 5000     | 0.55      |
# |             | Acima de 5000| 0.60      |
# |-------------|--------------|-----------|

#VAR
kwh = float(input('Quantos kWh?'))
tipo = input('Qual o tipo de instalação (R, C ou I):')

if (tipo == 'R'):
    if kwh <= 500:
        preco = 0.4
    else:
        preco = 0.65
elif (tipo == 'C'):
    if kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.60
elif (tipo == 'I'):
    if kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.6
else:
    print('Instalação inválida!')

print(f'Total a pagar: R${kwh*preco:.2f}')
#Fim