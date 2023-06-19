from classe import *

conexao = abrirBancoDados('localhost', 'root', 'root', 'ouvidoria')

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

    elif opcao == 2:
        consulta = 'select count(*) from manifestacao'
        manifestacao = listarBancoDados(conexao, consulta)
        quantidade = manifestacao[0][0]
        
        if quantidade == 0:
            print('Não existem manifestações cadastradas!')
        else:
            classe = int(input('Qual tipo de manifestação deseja exibir?'
                               '\n1)Elogio \n2)Reclamação \n3)Sugestão \n4)Voltar \nDigite: '))
            if classe == 1:
                consulta = 'select * from manifestacao where tipo = "Elogio" '
                elogio = listarBancoDados(conexao, consulta)
                print('-----------Elogios-----------')
                for i in elogio:
                    print('Código', i[0], '-', i[1], '-', i[4], '-', 'Data:',i[5],'/',i[6],'/',i[7])
            elif classe == 2:
                consulta = 'select * from manifestacao where tipo = "Reclamação" '
                reclamacao = listarBancoDados(conexao, consulta)
                print('-----------Reclamações-----------')
                for i in reclamacao:
                    print('Código', i[0], '-', i[1], '-', i[4], '-', 'Data:',i[5],'/',i[6],'/',i[7])
            elif classe == 3:
                consulta = 'select * from manifestacao where tipo = "Sugestão" '
                sugestao = listarBancoDados(conexao, consulta)
                print('-----------Sugestões-----------')
                for i in sugestao:
                    print('Código', i[0], '-', i[1], '-', i[4], '-', 'Data:',i[5],'/',i[6],'/',i[7])
            elif classe == 4:
                print('Voltar')
            else:
                print('Opção inválida!')
    elif opcao == 5:
        codigo = input('Digite o código da manifestação que deseja exibir: ')
        consulta = 'select * from manifestacao where codigo = ' + codigo
        pesquisa = listarBancoDados(conexao, consulta)

        if len(pesquisa) == 0:
            print('Manifestação não encontrada!')
        else:
            for i in pesquisa:
                print('Código', i[0], '-', i[1], '-', i[4],
                      '-', i[3], '-', 'Descrição:', i[2], '-', 'Data:', i[5], '/', i[6], '/', i[7])
    elif opcao == 6:
        consulta = 'select count(*) from manifestacao'
        manifestacao = listarBancoDados(conexao, consulta)
        quantidade = manifestacao[0][0]
        
        if quantidade == 0:
            print('Não existem manifestações cadastradas!')
        else:
            listar = 'select * from manifestacao'
            manifestacao = listarBancoDados(conexao, listar)
            for i in manifestacao:
                print('Código', i[0], '-', i[1], '-', i[4], '-', i[3])
            
            codigo = input('Informe o código da manifestação que deseja alterar o título e descrição \nDigite: ')
            consulta = 'select * from manifestacao where codigo = ' +codigo
            resultado = listarBancoDados(conexao, consulta)
            
            if len(resultado) == 0:
                print('Manifestação não encontrada!')
            else:
                novoTitulo = input('Digite o novo título: ')
                novaDescricao = input('Digite a nova descrição: ')
                sqlAtualizar = 'update manifestacao set titulo = %s, descricao = %s  where codigo = %s '
                valores = [novoTitulo,novaDescricao, codigo]
                atualizarBancoDados(conexao, sqlAtualizar, valores)
                print('Manifestação editada com sucesso!')
    
    elif opcao == 8:
        print('Sair')
        
        else:
            print('Opção inválida!')
