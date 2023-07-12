'''Crie um programa que realiza a contagem de 1 até 100, usando apenas de números ímpares.
Ao final do processo exiba em tela quantos números ímpares foram encontrados nesse intervalo,
assim como a soma dos mesmos.'''

contador = 0
soma = 0

for i in range(1, 101):
    if i % 3 == 0:
        soma += i
        contador += 1
        
print(f'Foram encontrados {contador} números ímpares. ')
print(f'A soma destes números é {soma}!!!')
