from time import sleep
from math import sqrt
while True:
    print('-=' * 20)
    print(''' Calculadora Simples
[1] Soma
[2] Subtração
[3] Multiplicação
[4] Divisão
[5] Raiz
[6] Sair''')
    print('-=' * 20)

    opção = int(input('Qual função deseja -_-: '))
    if opção == 6:
        print("Calculadora encerrando...")
        sleep(2)
        break
    if opção in [1,2,3,4]:
        num_1 = int(input('Digite o primeiro número:'))
        num_2 = int(input('Digite o segundo número: '))

    if opção == 1:
        soma = num_1 + num_2
        print(f'{num_1} + {num_2} = {soma}')
    elif opção == 2:
        subtração = num_1 - num_2
        print(f'{num_1} - {num_2} = {subtração}')
    elif opção == 3:
        multiplicação = num_1 * num_2
        print(f'{num_1} x {num_2} = {multiplicação}')
    elif opção == 4:
        divisão = num_1 / num_2
        print(f'{num_1} / {num_2} = {divisão}')
    
    elif opção == 5:
        num_1 = int(input('Digite o número desejado: '))
        print(f'A raiz de {num_1} = {sqrt(num_1)}')
    else:
        print('Opção Invalida')
