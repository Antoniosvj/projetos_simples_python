#Para que o script funcione coloque os arquivos que quiser renomear dentro da pasta arquivos

import os
os.chdir('.\\arquivos')

padrao_nome = input('Qual o padrão de nome de arquivo para usar sem a extensão: ')

for contador, arq in enumerate(os.listdir()):
    if os.path.isfile(arq):
        nome_arq, exten_arq = os.path.splitext(arq)
        nome_arq = padrao_nome + ' ' + str(contador+1)
        
        nome_novo = f'{nome_arq}{exten_arq}'
        os.rename(arq, nome_novo)
        
print('Arquivos renomeados.')