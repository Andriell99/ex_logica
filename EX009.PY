largura = float(input('Largura da parede: '))
altura = float(input('altura da parede: '))
area = largura*altura
total_tinta = area/2
print('Sua parede tem a dimensao de {}x{} e a area total de {}m²'.format(largura,altura,area))
print('para a pintura serao necessarios {}lts de tinta'.format(total_tinta))
