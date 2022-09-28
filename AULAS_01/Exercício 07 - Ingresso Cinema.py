#EXERCÍCIO 3

# Um cinema cobra preços diferentes para os ingressos de acordo com a idade de uma pessoa. Se a pessoa tiver menos de 3 anos
# de idade, o ingresso será gratuito, se tiver entre 3 e 12 anos, o ingresso custará R$ 15, se tiver mais de 12 anos, custará R$ 30

#> Escreva um laço em que você pergunte a idade aos usuários e, então, informe-lhes o preço do ingresso do cinema
#> Encerre o laço usando um break quando o usuário digitar sair
#> Após encerrar o laço, apresente na tela o total de pessoas que compraram ingressos,
# o total de dinheiro arrecadado e a média de idade das pessoas

#InicioAlgoritmo
print('+--------------------------------------+')
print('|     COMPRA DE INGRESSO CINEMARK      |')
print('+--------------------------------------+')
print('|      Digite sair para continuar      |')
#Enunciado pediu para utilizarmos break, portanto obrigatóriamente while True:

total = 0 #variável ACUMULADOR total pois vou somar as idades / sempre que houver somas, é extremamente importante o ACUMULADOR
#>>>SE eu colocar o acumulador dentro do laço, o programa NÃO irá funcionar<<<
# mas porquê? porque toda vez que o laço reiniciar ou seja, entrar no loop, ele vai zerar o valor da variavel total,
# e a variavel total ficara sempre em 0

dinheiro = 0 #variável ACUMULADOR dinheiro para contar os valores de ingressos
while True:
    idade = input('Qual sua idade?')
    if idade == 'sair': #para este comando funcionar, o input terá de vir em forma de string
    #   total += 1 ESTARÁ ERRADO pois se o usuário digitar sair, ele contara este sair como pessoa e somará + 1 (tenho de fazer o encremento depois)
        break
    idade = int(idade)# >>>Para eu transformar um ''número'' string em valor aritmético, basta eu converter usando o int<<<
    total += 1 #Começa em zero, e a cada nova pessoa que eu colocar (nova pessoa), ele somara + 1 do acumulador
    if idade < 3:
        ingresso = 0
    else:
        if idade > 12:
            ingresso = 30
        else:
            ingresso = 15
    dinheiro += ingresso #Observe a indentação, significa que esta variavel está dentro de todos os ifs
#FimSe

media = dinheiro / total
#Criei uma varíavel média, ele vai pegar o total do dinheiro e dividir pelo total de pessoas, chegndo assim... uma média :)
print(f'Total de pessoas: {total}')
print(f'Total arrecadado: R$ {dinheiro}')
print(f'Média arrecadada: R$ {media}')
#Fim
