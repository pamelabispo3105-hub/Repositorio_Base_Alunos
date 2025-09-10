# Atividades While Lição 2

nota = -1 #valor inicial inválido

while nota < 0 or nota > 10:
    nota = float(input("Digite uma nota entre 0 e 10:"))

print (f" Voce digitou uma nota valida: {nota}")