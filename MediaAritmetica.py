# Programar em Python, um programa capaz de perguntaro o nome do aluno, ler o nome do aluno, 
# perguntar a 1º nota e a 2º nota do aluno, verificar se a média do aluno é maior ou igual a 7,
# caso seja, escrever aluno aprovado, senão escrever aluno reprovado na tela.

# Perguntar Nome do Aluno
# Ler Nome do Aluno
# Perguntar 1º Nota do Aluno e a 2º Nota do Aluno
# Calcular a Média aritmética das notas do aluno
# Verificar se a média do aluno é maior ou igual a 7, escrever aluno aprovado, 
# Senão escrever aluno reprovado na tela.

print("Digite o nome do aluno: ")
varNome = str(input())
print("Digite a 1º nota do aluno: ")
varNota1 = float(input())
print("Digite a 2º nota do aluno: ")
varNota2 = float(input())
varMedia = ((varNota1 + varNota2) / 2)
if (varMedia >= 7):
    print("Aluno aprovado! Sua média é: ", varMedia)
else:
    print("Aluno reprovado! Sua média é: ", varMedia)