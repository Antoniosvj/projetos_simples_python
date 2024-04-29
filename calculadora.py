def calculadora():
    calcular = 's'
    while calcular == 's':
        a = float(input('Digite o primeiro número: '))
        b = float(input('Digite o segundo número: '))
        operacao = input('''Qual operação você deseja fazer: 
                        [+]somar
                        [-]diminuir
                        [*]multiplicar
                        [/]dividir
                        [**]exponenciar
                        [//]divisão arredondada\n
                        ''')

        if operacao == '+':
            print(a+b)
        elif operacao == '-':
            print(a-b)
        elif operacao == '*':
            print(a*b)
        elif operacao == '/':
            print(a/b)
        elif operacao =='**':
            print(a**b)
        elif operacao == '//':
            print(a//b)
        else:
            print('opção invalida!')
            operacao = input('''Qual operação você deseja fazer: 
                            [+]somar
                            [-]diminuir
                            [*]multiplicar
                            [/]dividir
                            [**]exponenciar
                            [//]divisão arredondada
                            ''')
        
        calcular = input('Deseja calcular novamente: [s]sim ou [n]não\n')

calculadora()