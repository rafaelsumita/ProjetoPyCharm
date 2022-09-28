#While True (Loop infinito proposital) enquanto não tiver um break

#InicioAlgoritmo
print('+--------------------------------+')
print('|           CALCULADORA          |')
print('+--------------------------------+')
print('| + Adição                       |')
print('| - Subtração                    |')
print('| * Multiplicação                |')
print('| / Divisão                      |')
print('|Pressione tecla s para SAIR     |')
print('+--------------------------------+')
#PROCESSAMENTO
#É interessante manter a operação dentro do laço do While, sendo não ser necessário ter 2 códigos iguais do mesmo comando etc.
while True:
    op = input('Qual operação deseja fazer?')
    if (op == '+') or (op == '-') or (op == '*') or (op == '/'):
        x = float(input('Digite o 1º valor:'))
        y = float(input('Digite o 2º valor:'))

        if (op == '+'):
            res = (x + y)
            print(f'Resultado: {x} + {y} = {res}')
            continue #para voltar lá no começo do laço
        elif (op == '-'):
            res = (x - y)
            print(f'Resultado: {x} - {y} = {res}')
            continue
        elif (op == '*'):
            res = (x * y)
            print(f'Resultado: {x} * {y} = {res}')
            continue
        elif (op == '/'):
            res = (x / y)
            print(f'Resultado: {x} / {y} = {res}')
            continue
        else:
            print('Operação inválida.')
    # CUIDADO com a INDENTAÇÃO! observe que este elif está indentado junto com o op(qual operação deseja fazer),
    # se ele estivesse dentro das operações, ele NUNCA poderia ser acionado, pois dentro das operações não tem inputs
    elif (op == 's'):
        break #Break quebra o laço

print('Encerrando o programa...')
#FimSe