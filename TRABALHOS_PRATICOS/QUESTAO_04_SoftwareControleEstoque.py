#QUESTAO 04
listaProdutos = []
#---------- COMEÇO cadastrarProduto ---------------
def cadastrarProduto(cad):
    print('Você Selecionou a Opção de Cadastrar Produto')
    print(f'Código do Produto: {cad}')
    produto = input('Por favor entre com o NOME do Produto: ')
    fabricante = input('Por favor entre com o FABRICANTE do Produto: ')
    valor = input('Por favor entre com o VALOR(R$) do Produto: ')
    dicionarioProduto = {'codigo'    :cad,
                         'nome'      :produto,
                         'fabricante':fabricante,
                         'valor'     :valor}
    listaProdutos.append(dicionarioProduto.copy())
#---------- FIM cadastrarProduto ------------------


#---------- COMEÇO consultarProduto ---------------
def consultarProduto():
    while True:
        try:
            print('Você Selecionou a Opção de Consultar Produto')
            opConsultar = int(input('Escolha a opção desejada:\n'
                                    '1-Consultar Todos os Produtos\n'
                                    '2-Consultar Produtos por Código\n'
                                    '3-Consultar Produtos por Fabricante\n'
                                    '4-Retornar\n'
                                    '>>'))
            if opConsultar == 1:
                print('Bem-vindo a consultar TODOS')
                for produto in listaProdutos: #selecionar cada dicionario da minha lista (cada produto da lista de produtos)
                    for key, value in produto.items(): #selecionar cada conjunto chave:valor do dicionario
                        print(f'{key} : {value}')
            elif opConsultar == 2:
                print('Bem-vindo a consultar por CÓDIGO')
                entrada = int(input('Digite o CÓDIGO do Produto: '))
                for produto in listaProdutos:
                    if(produto['codigo'] == entrada):
                        for key, value in produto.items():
                            print(f'{key} : {value}')
            elif opConsultar == 3:
                print('Bem-vindo a consultar por FABRICANTE')
                entrada = input('Digite o FABRICANTE do(s) Produto(s): ')
                for produto in listaProdutos:
                    if (produto['fabricante'] == entrada):
                        for key, value in produto.items():
                            print(f'{key} : {value}')
            elif opConsultar == 4:
                return
            else:
                print('Opção Inválida.')
                continue
        except ValueError:
            print('Opção Inválida.')
#---------- FIM consultarProduto ------------------


#---------- COMEÇO removerProduto -----------------
def removerProduto():
    print('Você Selecionou a Opção de Remover Produto')
    entrada = int(input('Digite o codigo do produto a ser REMOVIDO: '))
    for produto in listaProdutos:
        if (produto['codigo'] == entrada):
            listaProdutos.remove(produto)
#---------- FIM removerProduto --------------------


#---------- START MAIN PROGRAM --------------------
print('+--------------------------------------------------------------+')
print('|Bem Vindo ao Controle de Estoque da Marcearia do Rafael Sumita|')
print('+--------------------------------------------------------------+')
registroProduto = 0 #variavel acumulador
while True:
    try:
        opcao = int(input('Escolha a opção desejada:\n1-Cadastrar Produto\n2-Consultar Produto\n3-Remover Produto\n4-SAIR\n>>'))
        if opcao == 1:
            registroProduto = registroProduto + 1
            cadastrarProduto(registroProduto)
        elif opcao == 2:
            consultarProduto()
        elif opcao == 3:
            removerProduto()
        elif opcao == 4:
            print('Encerrando o Programa.')
            break
        else:
            print('Opção Inválida!')
            continue
    except ValueError:
        print('Opção Inválida.')
#---------- END MAIN PROGRAM ----------------------
#Fim