import math
valor = int(input('Escolha o valor: '))

def tabuada(valor):
  print('-'*15)
for i in range(1,11):
    result = valor*i
   
    print(f"{valor} x {i} = {result}")
    print('-'*15)

