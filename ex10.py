"""A empresa Hipotheticus paga R$10,00 por
 hora normal trabalhada, e R$15,00 por
hora extra. Faça um algoritmo para calcular e imprimir
o salário bruto e o salário
líquido de um determinado funcionário. Considere que o salário
 líquido é igual ao
salário bruto descontando-se 10% de impostos.
"""
cargaHoraria = int(input("Quantas horas você trabalha?"))
horaExtra = int(input("Quantas horas extras você fez?"))

salarioBruto = (cargaHoraria*10) + (horaExtra*15)
salarioLiquido = salarioBruto - salarioBruto * 0.10

print(f"O seu salario bruto é: {salarioBruto}")
print(f"O seu salario liquido é: {salarioLiquido}")
