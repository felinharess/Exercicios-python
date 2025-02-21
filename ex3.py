'''
Escreva um algoritmo para ler o nome e a idade de uma pessoa, e exibir
quantos dias de vida ela possui.
Considere sempre anos completos, e que um ano possui 365 dias. Ex:
uma pessoa com 19 anos possui 6935 dias de vida; veja um exemplo de
saída: MARIA, VOCÊ JÁ VIVEU 6935 DIAS.
'''
idade = int(input("Digite abaixo quantos anos de vida voce tem:"))

meses = idade * 12
dias = idade * 365

print("---------------")
print(f"Voce tem :\n{meses} meses de vida\n{dias} dias de vida")
print("---------------")