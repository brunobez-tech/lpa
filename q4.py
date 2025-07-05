print("Bem-vindos à empresa do Bruno Bezerra!")           # EXIGÊNCIA DE CÓDIGO 1 DE 7
listafuncionarios = []                                   # LISTA PARA ARMAZENAR FUNCIONÁRIOS
idglobal = 1234567                                       # NÚMERO DE IDENTIFICAÇÃO GLOBAL

def cadastrofuncionario(id):
    nome  = input('Informe o nome do funcionário: ')
    setor = input('Informe o setor do funcionário: ')

    while True:  # garante salário numérico
        try:
            salario = float(input('Informe o salário do funcionário: '))
            break
        except ValueError:
            print('Valor inválido! Digite apenas números (use ponto como separador decimal).')

    funcionario = {
        'id': id,
        'nome': nome,
        'setor': setor,
        'salario': salario
    }
    listafuncionarios.append(funcionario.copy())
    print(f'Funcionário {nome} cadastrado com sucesso!')

def consultafuncionarios():
    while True:
        opcao = input('\nQual opção deseja?\n''\t1 - Consultar todos\n''\t2 - Consultar por ID\n''\t3 - Consultar por setor\n''\t4 - Voltar ao menu inicial\n')
        if opcao == '1': # consulta geral
            if listafuncionarios:
                for func in listafuncionarios:
                    print(func)
            else:
                print('Nenhum funcionário cadastrado.')
        elif opcao == '2':                                  # consulta por id
            try:
                idconsulta = int(input('Informe o ID do funcionário: '))
            except ValueError:
                print('ID inválido!')
                continue
            encontrado = False
            for func in listafuncionarios:
                if func['id'] == idconsulta:
                    print(func)
                    encontrado = True
                    break
            if not encontrado:
                print('Funcionário não encontrado.')
        elif opcao == '3':                                  # por setor
            setorconsulta = input('Informe o setor: ')
            encontrados = [f for f in listafuncionarios if f['setor'] == setorconsulta]
            if encontrados:
                for func in encontrados:
                    print(func)
            else:
                print('Nenhum funcionário está nesse setor.')
        elif opcao == '4':
            return
        else:
            print('Opção inválida!')

def removerfuncionarios():
    while True:
        try:
            idremover = int(input('Informe o ID do funcionário a ser removido: '))
        except ValueError:
            print('ID inválido!')
            continue
        for func in listafuncionarios:
            if func['id'] == idremover:
                listafuncionarios.remove(func)
                print(f'Funcionário com ID {idremover} removido com sucesso.')
                return
        print('ID não encontrado.')                         

# MENU PRINCIPAL
while True:
    opcao = input('\nMENU PRINCIPAL\n''\t1 - Cadastrar funcionário\n''\t2 - Consultar funcionário\n''\t3 - Remover funcionário\n''\t4 - Sair\n')
    if opcao == '1':
        idglobal += 1
        cadastrofuncionario(idglobal)
    elif opcao == '2':
        consultafuncionarios()
    elif opcao == '3':
        removerfuncionarios()
    elif opcao == '4':
        print('Encerrando o programa.')
        break
    else:
        print('Opção inválida!')
    
#CADASTRO DE TRÊS (3) FUNCIONÁRIOS
print("Bem-vindos à empresa do Bruno Bezerra!")
print("\n\t Cadastro de 3 funcionários")
idglobal+=1
cadastrofuncionario(idglobal)
idglobal+=1
cadastrofuncionario(idglobal)
idglobal+=1
cadastrofuncionario(idglobal)

#CONSULTA DE TODOS OS FUNCIONÁRIOS
print('\n Consulta de todos os funcionários:')
consultafuncionarios()

#CONSULTA POR ID 
print('\n Consulta de funcionário por ID:')
consultafuncionarios()

#CONSULTA POR SETOR, ONDE 2 FUNCIONÁRIOS SEJAM DO MESMO SETOR
print('\n Consulta por setor no qual 2 funcionários sejam do mesmo setor')
consultafuncionarios()

#REMOÇÃO DE UM DOS FUNCIONÁRIOS, SEGUIDA DE CONSULTA DE TODOS OS FUNCIONÁRIOS
print('\n Remoção de um dos funcionários seguida de consulta de todos os funcionários:')
removerfuncionarios()
consultafuncionarios()