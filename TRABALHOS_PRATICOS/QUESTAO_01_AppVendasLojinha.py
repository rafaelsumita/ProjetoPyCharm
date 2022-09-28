#ALGORITMO_LOJA_SUMITA
print('+-------------------------------------+')
print('|    Bem Vindo a Loja Rafael  Sumita  |') #identificador pessoal
print('+-------------------------------------+')
#VAR
produto = float(input('Entre com o valor do produto:R$'))
qtd = int(input('Entre com o valor da quantidade: '))
valor_total = (produto * qtd)
desconto1 = (valor_total - valor_total * 0.03)
desconto2 = (valor_total - valor_total * 0.06)
desconto3 = (valor_total - valor_total * 0.10)
#PROCESSAMENTO
if qtd <= 4:
    print('O valor total foi de: R$ {}' .format(valor_total))
elif (qtd >= 5) and (qtd < 20): #usei and para verificar as condições
    print(f'O valor sem desconto foi: R$ {valor_total:.2f}')
    print(f'O valor com desconto foi: R$ {desconto1:.2f} (desconto 3%)') #usei uma outra forma de .format para deixar o código mais limpo e fácil
elif (qtd >= 20) and (qtd < 100):
    print(f'O valor sem desconto foi: R$ {valor_total:.2f}')
    print(f'O valor com desconto foi: R$ {desconto2:.2f} (desconto 6%)')
else:
    qtd >= 100
    print(f'O valor sem desconto foi: R$ {valor_total:.2f}')
    print(f'O valor com desconto foi: R$ {desconto3:.2f} (desconto 10%)')
#Fim