#EXERCÍCIO 2

# Suponha que você é um colecionar de jogos  de videogame.
# Escreva um algoritmo que  permita cadastrar esses jogos informando o nome e a qual videogame ele pertence
# Para isso, crie um menu de opções contendo: cadastrar novo item, listar tudo que foi cadastrado e sair

# Para resolver esse exercício, crie pelo menos uma função para cada item do menu
# Além disso, armazene todos os dados em um arquivo de texto que deve ser salvo em disco e manter os dados cadastrados

def valida_int(pergunta, min, max): #Para validar um dado, é uma ótima função para se validar dados
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+') #W de escrita e T de .txt, esse + CRIA o arquivo caso ele não exista
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print(f'Arquivo {nomeArquivo} foi criado com sucesso!\n')

def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt') # R é que eu vou TENTAR abrir o arquivo, e o t se o arquivo é .txt
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt') #quero apenas fazer uma leitura
    except:
        print('Erro ao ler o arquivo')
    else:
        print(a.read()) #função/método de ler o arquivo, e o print para mostrar na tela de todos os dados do nosso arquivo
    finally: #ATENÇÃO, caso dê sucesso ou não, vamos ter que FECHAR o arquivo independente do que aconteça
        a.close()

def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, 'at') #Vou abrir ele para escrita, MAS preserva o conteúdo se ele já existir
    except:
        print('Erro ao abrir o arquivo:')
    else:
        a.write(f'{nomeJogo} ;{nomeVideogame}\n') #função/método .writte para escrever no arquivo
    finally:                                      #Quebra de linha para listar cada ''item'' um abaixo do outro
        a.close() #independente do que acontecer... função/método .close para fechar

#MAIN PROGRAM
arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente')
    criaArquivo(arquivo)

while True:
    print('MENU')
    print('1 - Cadastrar um novo item')
    print('2 - Listar cadastros')
    print('3 - Sair')

    op = valida_int('Escolha a opção desejada: ', 1, 3)
    if op == 1:
        print('Opção de cadastrar novo item selecionado:\n')
        nomeJogo = input('Nome do jogo:')
        nomeVideogame = input('Nome do videogame:')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)
    elif op == 2:
        print('Opação de listar selecionada:\n')
        listarArquivo(arquivo)
    elif op == 3:
        print('Encerrando o programa...')
        break
#FimSe