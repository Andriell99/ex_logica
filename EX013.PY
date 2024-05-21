dias = int(input('Quantos dias ficou com o carro?: '))
kms = float(input('Quantos Kms rodou com o carro?: '))
custo_dia = 60
custo_km = 0.15
custo_efetivo = (custo_dia*dias) + (custo_km*kms)
print('voce ficou {} dias com o carro e rodou {} kms'.format(dias,kms))
print('o custo por dia foi de {}, o custo por km foi de {}, e o custo total foi de {}'.format(custo_dia*dias,(custo_km*kms),(custo_efetivo)))
