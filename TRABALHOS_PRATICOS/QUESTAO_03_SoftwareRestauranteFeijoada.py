#QUESTÃO_03
#             REGRA >> total = (volume * opção) + adicional(is) <<

#-----------COMEÇO DA FUNÇÃO VOLUMEFEIJOADA------------
def volumeFeijoada():
    while True:
        volumeA = float(input('|Menu Volume Feijoada|\n|Entre com a quantidade que deseja(ml): '))
        if 300 <= volumeA <= 5000: #se volume não é menor que 300 e não é maior que 5000 então retorna
            return volumeA * 0.08
        else:
            print('Não aceitamos porções menores que 300ml ou maiores 5l. Tente novamente!')
            continue
#----------FIM DA FUNÇÃO VOLUMEFEIJOADA----------------

#----------COMEÇO DA FUNÇÃO OPCAOFEIJOADA--------------
def opcaoFeijoada():
    while True:
        opcaoA = input('|------------------------------Menu Opção Feijoada----------------------------------------|\n'
                 '|b - Básica(Feijão + paiol + costelinha)                                                  |\n'
                 '|p - Premium (Feijão + paiol + costelinha + partes de porco)                              |\n'
                 '|s - Suprema (Feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon)|\n'
                 '|Entre com a opção de Feijoada: ')
        if opcaoA == 'b':
            return  1.00
        elif opcaoA == 'p':
            return  1.25
        elif opcaoA == 's':
            return  1.50
        else:
            print('Você não digitou uma opção válida')
            continue
#---------FIM DA FUNÇÃO OPCAOFEIJOADA-------------------

#---------COMEÇO DA FUNÇÃO ACOMPANHAMENTOFEIJOADA-------
def acompanhamentoFeijoada():
    acumulador = 0
    while True:
            try:
                acompA = int(input('|-----------------ACOMPANHAMENTOS---------------------|\n'
                                   '|0 - não desejo mais acompanhamentos (encerrar pedido)|\n'
                                   '|1 - 200g de arroz                                    |\n'
                                   '|2 - 150g de farofa especial                          |\n'
                                   '|3 - 100g de couve cozida                             |\n'
                                   '|4 -  1   larana descascada                           |\n'
                                   ' >>Deseja mais algum acompanhamento: '))
                if acompA == 0:
                    return acumulador
                elif acompA == 1:
                     acumulador = acumulador * acompA + 5.00
                elif acompA == 2:
                     acumulador = acumulador * acompA + 6.00
                elif acompA == 3:
                     acumulador = acumulador * acompA + 7.00
                elif acompA == 4:
                     acumulador = acumulador * acompA + 3.00
                else:
                    print('Opção inválida. Tente novamente')
                    continue
            except ValueError:
                    print('Opção inválida. Tente novamente')
                    continue
#---------FIM DA FUNÇÃO ACOMPANHAMENTOFEIJOADA----------

#START MAIN PROGRAM
print('                  +-----------------------------------------------+')
print('                  |Bem-Vindo ao Programa de Feijoada Rafael Sumita|')
print('                  +-----------------------------------------------+')
volume_feijoada = volumeFeijoada()
opcao_feijoada = opcaoFeijoada()
acompanhamento_feijoada = acompanhamentoFeijoada()
total = volume_feijoada * opcao_feijoada + acompanhamento_feijoada
print(f'O valor a ser pago é (R$):{total:.2f} (volume = {volume_feijoada} * opção ={opcao_feijoada} + acompanhamento ={acompanhamento_feijoada:.2f})')
#END MAIN PROGRAM
#FIM