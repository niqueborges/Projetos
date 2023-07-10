'''Crie um programa que lê um valor de início e um valor de fim,
exibindo em tela a contagem dos números dentro desse intervalo.'''

inicio = int(input('Digite o número onde começa a contagem: '))
fim = int(input('Digite o número onde termina a contagem: '))

for i in range(inicio, fim + 1):
    print(i)    