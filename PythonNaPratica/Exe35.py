'''Crie um programa que pede que o usuário digite um nome ou uma frase, verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em tela esse resultado.'''

frase = str(input('Digite uma palavra ou frase: ')).strip().upper()
palavras = frase.split()
caracteres = ".join(palavras)fraseinvertida= "

for i in range(len(caracteres)-1, -1, -1): fraseinvertida += caracteres[i]

print(caracteres, fraseinvertida)
    

