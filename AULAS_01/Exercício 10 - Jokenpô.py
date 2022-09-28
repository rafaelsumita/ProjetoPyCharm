#EXERCÍCIO 2
#                                                        JOKENPÔ
# >>Crie um jogo de pedra, papel ou tesoura (Jokenpô).
# >>Você deverá jogar contra o computador. Você irá sempre escolher uma das opções: 1- pedra, 2 – papel, 3 – tesoura
# >>O computador irá sempre sortear um número de 1 até 3 para jogar
# >>Armazene todos os resultados em uma lista e no final apresente o vencedor
# >>Encerre o programa ao digitar zero

#                                          (Standard Library)
# >>Precisamos entrar na biblioteca do Python.org para encontrarmos uma função para sortear
# >>dica, na parte Numeric and Mathematical Modules, tem uma biblioteca chamada randon (gera números aletórios)
# >>e lá tem um monte de métodos para gerar números aleatórios, a que vamos utilizar é a
# >> random.randint(a,b) << gera números aleatórios do tipo inteiros em um intervalo que EU definir
import random
#InicioAlgoritmo
#                                 Função de validação de dados básica:
def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

#                                  Função para ver o vencedor
# (condicional de múltipla escolha dentro de condicional de múltipla escolha)
# Olha o tamanho do código... eu preciso de uma multiplica escolha do jogador1, e dentro de cada escolha do jogador1
# Eu tenho uma multipla escolha do jogador2, entenda a lógica!
# >>> ATENÇÃO eu preciso trazer a variável (empate) pra cá, assim como as variáveis de vitória do jogador 1 (v1) e jogador 2 (v2)
# >>>com a instrução global, para que eu possa trabalhar nela nesta função
def vencedor(jogador1, jogador2):
    global empate, v1, v2
    if jogador1 == 1:# Pedra
        if jogador2 == 1:# Pedra
            empate += 1
        elif jogador2 == 2:# Papel
            v2 += 1 # NESTE caso SE o jogador1 jogar Pedra significa que vai ser vitória do jogador2 (papel embrulha pedra)
        elif jogador2 == 3:# Tesoura
            v1 += 1 # Pedra contra Tesoura = vitória do jogador1
    elif jogador1 == 2:# Papel
        if jogador2 == 1:# Pedra
            v1 += 1 # Papel(jogador1) contra Pedra do jogador2 = vitória do jogador1
        elif jogador2 == 2:# Papel
            empate += 1 # Papel contra Papel = empate
        elif jogador2 == 3:# Tesoura
            v2 += 1 # Papel contra Tesoura = vitória do jogador 2
    elif jogador1 == 3:# Tesoura
        if jogador2 == 1:# Pedra
            v2 += 1 # Tesoura do jogador1 contra Pedra do jogador2 = vitória do jogador2
        elif jogador2 == 2:# Papel
            v1 += 1 # Tesoura do jogador1 contra Papel do jogador2 = vitória do jogador1
        elif jogador2 == 3:# Tesoura
            empate += 1 # Tesoura x Tesoura = empate

# ------------------------------------------------ MAXIMA ATENÇÃO AQUI...------------------------------------------------------
    resultados = [v1, v2, empate] #criei uma variável LOCAL (ou seja ela NÃO é a mesma variável global) para receber os dados gerados nesta função
    return resultados # Olhe aqui retornando os resultados e ATENÇÃO a INDENTAÇÃO! observe que está alinhado com o primeiro if, ou seja ele pega TUDO da função
#                  >   E é claro que preciso agora chamar o resultado desta função, lá no programa principal    <

#-----------------------------------------------------MAIN PROGRAM---------------------------------------------------------------
# aqui fica toda a manipulação de resultados
print('+--------------------------------------+')
print('|               JOKENPÔ                |')
print('+--------------------------------------+')
print('|1 - Pedra                             |')
print('|2 - Papel                             |')
print('|3 - Tesoura                           |')
print('|0 - Para sair e mostrar os resultados |')
print('+--------------------------------------+')

resultados = [] # Uma lista para salvarmos os resultados
jogadas = [] # Uma lista para salvarmos os números de jogadas

# acumuladores / variáveis globais:
v1 = 0 #número de vitórias do jogador 1
v2 = 0 #número de vitórias do jogador 2
empate = 0 #número total de empates

while True:
    j1 = valida_int('Escolha sua jogada: ', 0, 3)
    if not j1: #Eu fizer isto é igual eu colocar if j1 == 0
        break
    j2 = random.randint(1,3) #preciso que a jogada do jogador 2 receba um número aleatório (que vai ser gerado no intervalo entre 1 e 3)
    jogadas.append([j1, j2]) # .append para adicionar um item no final da nossa lista, ou seja vamos adicionar as jogadas/ vou salvando todas as jogadas naquela lista ali / jogadas = [] /NUNCA SE ESQUEÇA DOS [] pois estamos salvando estes dados dentro de uma lista
# depois que eu faço o .append, eu vou pegar todos os resultados chamando a FUNÇÃO vencedor() aonde eu passo como parâmetros, as jogadas j1 e j2
    resultados = vencedor(j1, j2) # aqui eu sei quantas vezes o jogador1 ganhou, jogador2 ganhou e quantas vezes deu empate
    print(vencedor(j1,j2))

#                                                    DESCOBRIR AS JOGADAS RANDOMICAS
#   Para descobrirmos as jogadas entre os combates, basta que eu pegue as jogadas(da lista do .append), precisamos fazer uma varredura de dupla indexação
#   pois vamos precisar acessar o dado dentro das jogadas,
#   eu tenho as jogadas E dentro tenho (as jogadas do jogador1 e as jogadas do jogador2) >> lá nós temos uma indexação dupla!
#   ou seja, eu posso acessar utilizando dois laços de repetição

    for jogada in jogadas: # Aqui eu acesso jogadas dentro de jogadas
        for dado in jogada: # Aqui eu faço outro for para acessar o dado dentro da jogada
            print(dado, end=' ') # para imprimir os dois na mesma linha, eu faço o end=' ' com espacinho entre eles
        print() # Print vazio para podermos dar um print entre todas as jogadas

#                                                               FINALIZANDO
print(f'Número de vitórias do jogador 1: {resultados[0]}') # Neste print quero mostrar o indíce ZERO da variavel resultados
#>>> MAS PORQUE mostrar o indice zero da variável resultados? pois bem, esta variável resultados é a da FUNÇÃO def vencedor(): <<<
# e se olharmos lá, vai estar assim: resultados = [v1, v2, empate], ou seja esta variável tem 3 indices(v1, v2, empate) ou seja... (0,1,2)
print(f'Número de vitórias do jogador 2: {resultados[1]}') # Mostrar o índice 1 que equivale as vitórias do jogador2 (v2) na variável
print(f'Número de empates: {resultados[2]}') # Mostrar o índice 2 que equivale os empates (empate) na variável
# Observe que estes prints dos resultados estão após o laço de repetição! PRESTE atenção na Indentação!
#FIM