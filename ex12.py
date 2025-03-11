"""Três amigos, Carlos, André e Felipe. decidiram rachar igualmente a conta de
um bar.
Faça um algoritmo para ler o valor total da conta e imprimir quanto cada um
deve pagar, mas faça com que Carlos e André não paguem centavos. Ex:
uma conta de R$101,53 resulta em R$33,00 para Carlos, R$33,00 para
André e R$35,53 para Felipe.
"""
precoConta = float(input("Digite abaixo o valor da conta: \n"))

valorU = precoConta / 3
carlos = int(valorU)
felipe = round(valorU, 2)
andre = int(valorU)

soma = carlos + felipe + andre

if soma != precoConta:
    cents = precoConta - soma
    felipe += cents
print(f"Felipe vai pagar: {felipe:.2f}")
print(f"Andre vai pagar: {andre}")
print(f"Carlos vai pagar: {carlos}")
