'''idade = 37
nome = "Monique"
dado = 1
print(type(dado)) # tipo de dado

dado = False
print(f"O meu nome é {nome} e minha idade é {idade}") # comando de saída de dados


idade = input("Digite a sua idade: ")

print(f'Olá, a idade digitada é: {idade}')


Conversão de dados
prova1 = int("10")
prova2 = int("6")
somatoria = prova1 + prova2
print(somatoria)

prova1 = int(input("Digite a nota da prova1: "))
prova2 = int(input("Digite a nota da prova2: "))
somatoria = prova1 + prova2
print(somatoria)

Operadores Matemáticos (+ - * ** / // %) precedência ** > * / // % > + -

prova1 = 10
prova2 = 5
soma = prova1 + prova2
subtracao = prova1 - prova2
multiplicacao = prova1 * prova2
divisao = prova1 / prova2
exponenciacao = prova1 ** prova2
divisaoporinteiro = prova1 // prova2
modulo = prova1 % prova2
print(soma, subtracao, multiplicacao, divisao, exponenciacao, modulo)

prova1 = 10
prova2 = 5
media = (prova1 + prova2) / 2
print(f"A média é: {media}")


Operadores relacionais (== > < >= <= !=)

prova1 = 10
prova2 = 5
igual = prova1 == prova2
maior = prova1 > prova2
menor = prova1 < prova2
menor_igual = prova1 <= prova2
maior_igual = prova1 >= prova2
diferente = prova1 != prova2
print(igual, maior, menor, menor_igual, maior_igual, diferente)

Operadores lógicos [and or not]

prova1 = 10
prova2 = 5

E = True and True
E = True and False
Ou = True or True
Ou = True or False
Nao = not True
Nao = not False
print(E, Ou, Nao)

prova1 = int(input("Digite a nota da prova1: "))
prova2 = int(input("Digite a nota da prova2: "))
media_do_aluno = (prova1 + prova2) / 2
resultado = media_do_aluno < 6 and media_do_aluno >= 4
print(resultado)'''

