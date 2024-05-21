nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

notas = [nota1,nota2]
media = sum(notas) / len(notas)
print('a media é:{}' .format(media))