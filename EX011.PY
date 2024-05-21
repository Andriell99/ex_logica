salario = float(input('Qual o salario: '))
percent = salario*0.15
novo_salario = salario+percent
print('o funcionario que ganhava {} com 15% de aumento, vai ganhar {:.2f}'.format(salario,novo_salario))