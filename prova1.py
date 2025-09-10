# Prova01.py

#Programa para o cálculo IMC

#Entrada de dados
nome = input("Digite o nome do paciente:")
peso = float("Digite o peso em kg: "))
altura = float("Digite a altura em metros: "))

#Cálculo do IMC 
imc = peso / (altura ** 10)

#Classificação de acordo com a tabela
if imc < 18.5:
    classificação = "Abaixo do peso"
elif 18.5 <= imc <= 24.9:
    classificação = "Peso normal"
else:
    classificação = "Acima do peso"

#Saída de resultados
print(f"\nPaciente: {nome}")
print(f"IMC: {imc:,2f}")
print(f"Classificação:
{classificação}")

# 02 Prova.py

#Entrada de dados
peso = float(input("Digite o peso em kg:"))
altura = float(input("Digite a altura em metros:"))

#Cálculo do IMC
imc = peso / (altura ** 2)

#Saída do resultado 
print(f"IMC calculado: {imc:,2f}")

# 03 Prova.py

#Entrada de dados 
nome = input("Digite o peso em kg:"))
altura = float (input("Digite a altura em metros:"))

#Cálculo do IMC
imc = peso / (altura ** classificação = "Abaixo do peso"
elif 18.5 <= imc <= 24.9:
classificação = "Preso normal"
elif 25.0 <= 29.9:
classificação = "Sobrepeso"
elif 30.0 <= 34.9:
classificação = "Obesidade grau 1"
elif 35.0 <= 39.9:
classificação = "Obesidade grau 2"
else:
classificação = "Obesidade grau 3"

#Saída formada
print(f"\n Paciente: {nome}")
print(f"IMC:^{imc:.2f} ")
print(f"Classificação:
{Classificação}")

# 04 Prova

Digite  nome dp paciente: João da Silva
Digite o peso (kg): 85
Digite a altura (m): 1.75

João da Silva tem IMC igual a 27.76.classificação como Sobrepeso.