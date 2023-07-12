'''Crie um programa que realiza a Progressão Aritmética de 20 elementos,
com primeiro termo e razão definidos pelo usuário.'''

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
pa = termo + (20 - 1) * razao

for i in range(termo, pa + razao, razao):
    print(i)