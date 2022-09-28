#EXERCÍCIO 2

# Escreva um algoritmo que leia um valor e que imprima a quantidade de cédulas necessárias para pagar esse mesmo valor.
# Para simplificar, vamos trabalhar apenas com valores inteiros e com cédulas de R$100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 1

#InicioAlgoritmo
#VAR
print('+------------------------------------------------------------+')
print('|                   SAQUE CAIXA ELETRÔNICO                   |')
print('+------------------------------------------------------------+')
print('|Cédulas Disponíveis: '
      'R$100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 1|')
valor = int(input('Digite o valor em R$ '))
#A Lógica que pode ser aplicada aqui... primeiro, pegar o valor e VER quantas vezes ele pode ser dividido por 100
#e pegar apenas a parte inteira dele e repassar o resto, depois ver quantas vezes este resto valor cabe de 50
#depois 20, 10, 5 e finalmente chegar em 1, caso o valor seja menor que um dos valores informados, o programa irá passar para o prox passo
#consequentemente.
#VALOR DE EXEMPLO R$ 522,00
if valor > 100:#cedulas100 será o nosso contador, pode usar qualquer nome, count100, contador100, etc
    cedulas100 = valor // 100#valor dividido por 100, porém pegando apenas a parte inteira, para saber quantas vezes 100 cabe dentro de 522
    valor = valor - cedulas100 * 100#ex: 522, ele vai pegar:( valor = 522 - 500(resultado da parte inteira de quantas vezes 100 cabe em 522)
                                    #e vai armazenar o resultado na variável, no caso do exemplo vai ser 22
    print(f'Cédulas de 100: {cedulas100}')

#>>>ATENÇÃO<<<
#>>>EU NÃO POSSO UTILIZAR CONDICIONAL COMPOSTA OU ALINHADA<<<
#Porque se eu fizer um ifelse/elif por ex: o primeiro if der verdadeiro, ele nem vai tentar fazer os outros
#Por isto é necessário deixar ifs simples para que o programa POSSA TESTAR TODAS as cédulas
while True:
    if valor >= 50:
        cedulas50 = valor // 50
        valor -= cedulas50 * 50
        print(f'Cédulas de 50: {cedulas50}')
        if not valor:#por exemplo, se eu digitar o valor 500, o resto do resultado será 0, e este if dará verdadeiro e entrara neste laço
            break    #E neste laço tem um break, ou seja... se não restar nada ele se encerrará aqui, melhorando um pouco o desempenho do programa
    if valor >= 20:
        cedulas20 = valor // 20
        valor -= cedulas20 * 20 #Operador especial de atribuição lembra? += / -= / *= etc
        print(f'Cédulas de 20: {cedulas20}')
        if not valor:
            break
    if valor >= 10:
        cedulas10 = valor // 10
        valor -= cedulas10 * 10
        print(f'Cédulas de 10: {cedulas10}')
        if not valor:
            break
    if valor >= 5:
        cedulas5 = valor // 5
        valor -= cedulas5 * 5
        print(f'Cédulas de 5: {cedulas5}')
        if not valor:
            break
    if valor:# pois ae ele vai tentar com 4 reais, 3 reais, 2 reais, 1 real, se não sobrou nada ae ele nem tenta
        cedulas1 = valor#recebe simplesmente o valor, não precisando fazer nenhum calculo, porque o que sobrar
                        #serão cédulas de 1, ou sobrara 2 ou 3 ou 4
        print(f'Cédulas de 1: {cedulas1}')

    print('Encerrando o Programa.')
    break
#FimSe

