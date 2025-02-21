'''
A padaria Hotpão vende uma certa quantidade de pães franceses e uma
quantidade de broas a cada dia. Cada pãozinho custa R$ 0,12 e a broa
custa R$ 1,50. Ao final do dia, o dono quer saber quanto arrecadou com
a venda dos pães e broas (juntos), e quanto deve guardar numa conta
de poupança (10% do total arrecadado). Você foi contratado para fazer
os cálculos para o dono. Com base nestes fatos, faça um algoritmo para
ler as quantidades de pães e de broas, e depois calcular os dados
solicitados.
'''
qtdPao = int(input("Quantos paes você vendeu hoje? "))
qtdBroa = int(input("Quantas broas você vendeu hoje? "))

valorPao = qtdPao * 0.12
valorBroa = qtdBroa * 1.50
totalArrecadado = valorBroa + valorPao
poupanca = totalArrecadado * 0.10

print('---------------------')
print(f"Voce vendeu um total de:\n{qtdPao} pães\n{qtdBroa} broas")
print(f"Fazendo com que voce faturasse {totalArrecadado} reais!!!\nO valor para guardar na poupanca é: {poupanca} reais")
print('---------------------')