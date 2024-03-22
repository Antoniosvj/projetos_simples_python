contatos = []
def cadastro_contato():
    print('\n#' * 5 + ' Cadastro Contato ' + '#'*5)

    while True:
        nome = input('Nome: ')
        telefone = input('Telefone: ')

        contato = {'nome': nome, 'telefone': telefone}
        contatos.append(contato)

        continua = input('Adicionar outro contato: sim/nao: ')
        if continua.lower() != 'sim':
            break
    agenda_telefonica()

def ver_contatos():
    print('\nContatos')
    for contato in contatos:
        print(f'Nome: {contato["nome"]} - Telefone: {contato["telefone"]}')

    agenda_telefonica()
def agenda_telefonica():
    print('\n'+'#'* 5 + ' Agenda Telefonica ' + '#'*5)
    opcao = input('''
    [1] Cadastrar Contatos
    [2] Ver Contatos
    Digite uma opção: 
    ''')
    if opcao == '1':
        cadastro_contato()
    elif opcao == '2':
        ver_contatos()
    else:
        print('Opção invalida, Digite uma opção valida.')
        agenda_telefonica()


if __name__ == '__main__':
    agenda_telefonica()