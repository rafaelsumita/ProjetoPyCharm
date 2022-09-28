#EXERCÍCIO 1

# Escreva uma função que calcule o fatorial de um número recebido como parâmetro e retorne o seu resultado
# Faça uma validação dos dados por meio de uma outra função, permitindo que somente valores positivos sejam aceitos
# Crie o help da sua função

#InicioAlgoritmo
def valida_int(pergunta, min, max): #PARA validar um dado, é uma ótima função para se validar dados
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def fatorial(num):
    '''
    Calcula a fatorial
    :param num:
    :return:
    '''
    fat = 1#O menor valor de fatorial possível que existe é 1 (não existe fatorial negativo, e fatorial de zero é 1)
    if num == 0:#Se o usuário digitar zero, eu vou automaticamente retornar o fat... pois ele vale 1, e vou considerar 1
        return fat #Ou este vai acontecer
    for i in range(1, num+1, 1):#Pode ser também como pensamos em fatorial... (num+1, 1, -1) para andar da direita para esquerda tem de ser -1
        fat *= i #mesma coisa que: fat = fat * i
    return fat #Este aqui SÓ acontece, caso o número do usuário não for zero / #PRESTA ATENÇÃO NA INDENTAÇÃO!

#MAIN PROGRAM
x = valida_int('Digite um valor para calcular a fatorial:', 0, 99999)
print(f'{x}! = {fatorial(x)}')
help(fatorial)
#Fim