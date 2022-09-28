#AlgoritmoPizzaria
print('                Bem-Vindo a Pizzaria do Rafael Sumita') #identificador pessoal
print('|Código  |Descrição   |Pizza Média - M|Pizza Grande - G(30% mais cara)|')
print('|  21    |Napolitana  |        R$20,00|                        R$26,00|')
print('|  22    |Margherita  |        R$20,00|                        R$26,00|')
print('|  23    |Calabresa   |        R$25,00|                        R$32,50|')
print('|  24    |Toscana     |        R$30,00|                        R$39,00|')
print('|  25    |Portuguesa  |        R$30,00|                        R$39,00|')
#VAR
#tamanho / codigo / resposta
acumulador = 0
#PROCESSAMENTO
while True:
    tamanho = input('Qual tamanho de pizza que deseja (M/G): ')
    if tamanho != 'M' and tamanho != 'G':
        print('Opção inválida')
        continue
    if tamanho == 'M': #usei uma estrutura para cada um dos tamanhos(M/G) pois não consegui usando and ou or fazer com que meu programa funcionasse...
        codigo = input('Entre com o código do sabor desejado: ')
        if codigo == '21':
            print('Você pediu uma pizza Napolitana média')
            acumulador = acumulador + 20
        elif codigo == '22':
            print('Você pediu uma pizza Margherita média')
            acumulador = acumulador + 20
        elif codigo == '23':
            print('Você pediu uma pizza Calabresa média')
            acumulador = acumulador + 25
        elif codigo == '24':
            print('Você pediu uma pizza Toscana média')
            acumulador = acumulador + 30
        elif codigo == '25':
            print('Você pediu uma pizza Portuguesa média')
            acumulador = acumulador + 30
        else:
            print('Opção inválida')
            continue
    if tamanho == 'G':
        codigo = input('Entre com o código do sabor desejado: ')
        if codigo == '21':
            print('Você pediu uma pizza Napolitana grande')
            acumulador = acumulador + 26
        elif codigo == '22':
            print('Você pediu uma pizza Margherita grande')
            acumulador = acumulador + 26
        elif codigo == '23':
            print('Você pediu uma pizza Calabresa grande')
            acumulador = acumulador + 32.50
        elif codigo == '24':
            print('Você pediu uma pizza Toscana grande')
            acumulador = acumulador + 39
        elif codigo == '25':
            print('Você pediu uma pizza Portuguesa grande')
            acumulador = acumulador + 39
        else:
            print('Opção inválida')
            continue
    print('Digite 1 - Sim\nDigite 2 - Não')
    resposta = int(input('Deseja pedir mais alguma coisa?'))
    if resposta == 2:
        print('O total a ser pago é: R${:.2f}' .format(acumulador))
        break
#FimSe



