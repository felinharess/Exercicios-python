'''
Faça um algoritmo para ler o salário de um funcionário e aumentá-lo em
15%. Após o aumento, desconte 8% de impostos. Imprima o salário
inicial, o salário com o aumento e o salário final.
'''
salario = float(input("Por favor, informe o seu salario atual: \n"))
salario += salario * 0.15
salario -= salario * 0.08
print(f"O seu salário ficará {salario}R$")
