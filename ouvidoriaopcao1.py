'''
Nome dos integrantes: Carlos Daniel de Lima Souza, Gabriel Leite Oliveira Da Silva, 
Hugo Yan Capozzoli Costa e João Victor Pinheiro Rodrigues.
'''
from operacoesbd import *

conexao = abrirBancoDados('localhost', 'root', 'helloworld', 'ouvidoria1')

opcao = 1

print('-------------Seja Bem-vindo(a)-------------')

while opcao != 8:
    print()
    print('1)Listar todas manifestações\n')
    print('2)Listar manifestações por tipo\n')
    print('3)Criar nova manifestação\n')
    print('4)Exibir quantidade de manifestações\n')
    print('5)Pesquisar manifestação por código\n')
    print('6)Alterar o Título e Descrição de uma manifestação\n')
    print('7)Excluir uma manifestação por código\n')
    print('8)Sair do sistema\n')
    print()

    opcao = int(input('Digite uma opção: '))

    if opcao == 1:
        consulta = 'select count(*) from manifestacao'
        manifestacao = listarBancoDados(conexao, consulta)
        quantidade = manifestacao[0][0]

        if quantidade == 0:
            print('Não existem manifestações cadastradas!')
        else:
            listar = 'select * from manifestacao'
            manifestacao = listarBancoDados(conexao, listar)
            for i in manifestacao:
                print('Código', i[0], '-', i[1], '-', i[4], '-', i[3], '-', 'Data:',i[5],'/',i[6],'/',i[7])