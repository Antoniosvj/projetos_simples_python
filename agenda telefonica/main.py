import json
import os

contatos = []

def salvar_contatos():
    with open('contatos.json', 'w') as arquivo:
        json.dump(contatos, arquivo)
        
def carregar_contatos():
    arquivo_contatos = './contatos.json'
    if os.path.exists(arquivo_contatos):
        with open(arquivo_contatos, 'r') as arquivo:
            return json.load(arquivo) 
    else:
        print('Arquivo de contatos não encontrado.')
        return []

def cadastro_contato():
    print('\n'+'#' * 5 + ' Cadastro Contato ' + '#'*5)

    while True:
        nome = input('Nome: ')
        telefone = input('Telefone: ')

        contato = {'nome': nome, 'telefone': telefone}
        contatos.append(contato)
        salvar_contatos()

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
    contatos = carregar_contatos()
    agenda_telefonica()