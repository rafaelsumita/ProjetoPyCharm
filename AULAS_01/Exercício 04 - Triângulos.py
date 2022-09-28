# EXERCÍCIO 1

# Faça um algoritmo que receba  três valores, representando os lados de um triângulo fornecidos pelo usuário.
# Verefique se os valores formam um triângulo e os classifique como:

# a) Equilátero (três lados iguais) <<<
# b) Isósceles  (dois lados iguais) <<<
# c) Escaleno   (três lados diferentes) <<<

# (Lembre-se de que, para formar um triângulo, nenhum dos lados pode ser igual a zero, e um lado não pode ser
#  maior do que a soma dos outros dois (exercício da apostila - aula 3))

#Ínicio Algoritmo
#VAR
A = int(input('Digite o 1º lado do triângulo:'))
B = int(input('Digite o 2º lado do triângulo:'))
C = int(input('Digite o 3º lado do triângulo:'))
#PROCESSAMENTO
if (A > 0) and (B > 0) and (C > 0):#Dica para usar os parenteses. E, caso esta primeira condição dê VERDADEIRA: continue
    if (A + B > C) and (A + C > B) and (B + C > A): #Esta condição SÓ será executada, caso a primeira condição dê VERDADEIRA
    #Se esta condição TAMBÉM der VERDADEIRA, é porque o triângulo é válido!
        if (A != B) and (A != C) and (B != C):# este (B != C) nem precisária, pois se A != B e A também é != C, por consequência B vai ser diferente de C
            print('Triângulo Escaleno!')
        else:
            if (A == B) and (A == C) and (B == C): #novamente... se A = B e A = C, por consequência B = C
                print('Triângulo Equilátero!')
            else:
                print('Triângulo Isósceles!')#Se não é escaleno todos os lados diferentes) se não é equilatero(todos os lados iguais) só pode ser Isósceles
    else:
        print('Ao menos um dos valores indicados não servem para formar um triângulo')
else:
    print('Ao menos um dos valores indicados não servem para formar um triângulo')
#Fim-Se