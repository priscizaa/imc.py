# Faça um algoritmo que calcule o IMC e exiba na tela. (CARLA PRISCILA)
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura ** 2)

# CATEGORIAS DO IMC

if imc < 18.5:
   categoria = "abaixo do peso"
elif 18.5 <= imc < 24.9:
   categoria = "peso normal"
elif 25.0 <= imc < 29.9:
   categoria = "sobrepeso"
elif 30.0 <= imc < 39.9:
   categoria = "obesidade"
else:
   categoria = "obesidade grave"

imc = peso, altura

# EXIBIR RESULTADOS
print("seu imc é: ", imc)
print("categoria: ", categoria)
