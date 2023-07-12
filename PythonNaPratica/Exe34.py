'''Crie um programa que pede ao usuário que o mesmo digite um número qualquer,
em seguida retorne se esse número é primo ou não, caso não,
retorne também quantas vezes esse número é divisível.'''

numero = int(input('Digite um número: '))
divisoes = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        divisoes += 1
        
if divisoes == 2:
    print(f'{numero} é primo!!!')
    print(f'{numero} é divisível por 1 ou por {numero}.')
else:
    print(f'{numero} não é primo!!!')
    print(f'{numero} é divisível {divisoes} vezes...')