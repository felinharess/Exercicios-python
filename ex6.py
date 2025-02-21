'''
Entrar com o dia e o mês de uma data e informar quantos dias se
passaram desde o início do ano.
Esqueça a questão dos anos bissextos e considere sempre que um mês
possui 30 dias.
'''
mes = int(input("Informe o mes atual: (em numero ex: setembro == 9)\n"))
dia = int(input("Informe o dia de hj: (numero)\n"))

qtdDias = mes * 30
qtdDias += dia
print(f"Ja se passaram {qtdDias} dias esse ano")
