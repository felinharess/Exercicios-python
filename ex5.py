'''
O restaurante a quilo Bem-Bão cobra R$12,00 por cada quilo de
refeição. Escreva um algoritmo que leia o peso do prato montado pelo
cliente (em quilos) e imprima o valor a pagar. Assuma que a balança já
desconte o peso do prato.
'''
peso = float(input("Informe o peso do seu prato(em quilos):\n"))
precoKilo = 12.00
precoFinal = precoKilo * peso
print(f"O seu prato ficou no total de: {precoFinal}R$")