# Crie um programa que exiba em tela a tabuada de um determinado número fornecido pelo usuário.

x = int(input('Digite um número: '))

for num in range(1, 11):
    print(f'{x} X {num} = {x * num}')