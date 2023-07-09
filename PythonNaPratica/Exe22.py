'''Crie duas variáveis com dois valores numéricos inteiros digitados pelo usuário,
caso o valor do primeiro número seja maior que o segundo,
exiba em tela uma mensagem de acordo, caso contrário,
exiba em tela uma mensagem dizendo que o primeiro valor digitado é menor que o segundo.'''

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print('O primeiro número digitado é o maior!')
else:
    print('O segundo número digitado é o maior!')