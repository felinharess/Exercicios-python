"""A fábrica de refrigerantes Meia-Cola vende
seu produto em três formatos: lata de
350 ml, garrafa de 600 ml e garrafa de 2 litros. Se um comerciante compra uma
determinada quantidade de cada formato, faça um algoritmo para calcular quantos
litros de refrigerante ele comprou.
"""
latas = int(input("Quantas latas de refri você deseja comprar: \n"))
garrafa1 = int(input("Quantas garafas 600ml de refri você deseja comprar: \n"))
garrafa2 = int(input("Quantas garrafas de2 de refri você deseja comprar: \n"))

litrosTotal = (latas * 0.350) + (garrafa1 * 0.600) + (garrafa2 * 2)

print(f"Voce comprou {latas} latas de 350 ml")
print(f"Voce comprou {garrafa1} garrafas de 600 ml")
print(f"Voce comprou {garrafa2} garrafas de 2 litros")
print(f"Você pegou um total de ${litrosTotal} litros")
