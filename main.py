# Exercícios de matéria de Algoritmos e Programação de Computadores I

import math

# exercício 2.1

a1 = 1 + 2 + 3 + 4 + 5
print(a1)

b1 = (23 + 19 + 32) / 3
print(b1)

c1 = 403 // 73
print(c1)

d1 = 403 % 73
print(d1)

e1 = 2 ** 10
print(e1)

f1 = abs(54 - 57)
print(f1)

g1 = min(34.99, 29.95, 31.5)
print(g1)

# exercício 2.2

a2 = (2 + 2) < 4
print(a2)

b2 = (7 // 3) == (1 + 1)
print(b2)

c2 = (3 ** 2 + 4 ** 2) == 25
print(c2)

d2 = (2 + 4 + 6) > 12
print(d2)

e2 = (1387 % 19) == 0
print(e2)

f2 = (31 % 2) == 0
print(f2)

g2 = min(34.99, 29.95, 31.5) < 30.0
print(g2)

# exercício 2.3

a = 3
b = 4
c = (a * a) + (b * b)
print(c)

# exercício 2.4

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

print(s1 + " " + s2 + " " + s1)
print(((s1 + " ") * 9) + s1)
print(s1 + " " + ((s2 + " ") * 2) + ((s3 + " ") * 2) + s3)
print(((s1 + " " + s2 + " ") * 7) + s1 + " " + s2)
print(((((s2 * 2) + s3) + " ") * 4) + ((s2 * 2) + s3))

# exercício 2.5

s = '0123456789'

print(s[0], s[1], s[6], s[8], s[9], sep="\n")

# exercício 2.6

palavras = ['taco', 'bola', 'celeiro', 'cesta', 'peteca']

palavras.sort()
print(palavras[0], palavras[-1], sep="\n")

# exercício 2.7

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

notas.count(7)
notas[-1] = 4
max(notas)
notas.sort()
sum(notas) / len(notas)

# exercício 2.8

lista_28 = [0, 1]
variavel_a_28 = 5

print(2 + 3 == 4 or variavel_a_28 >= 5)
print(lista_28[1] * -3 < -10 == 0)
print((lista_28[1] * -3 < -10) in [0, True])
print(2 * 3 ** 2)
print(4 / 2 in [1, 2, 3])

print(False in [0, True])

# exercício 2.9

print(type(False + False))
print(type(2 * 3 ** 2.0))
print(type(4 // 2 + 4 % 2))
print(type(2 + 3 == 4 or 5 >= 5))

# exercício 2.10

lado_a_210 = 4
lado_b_210 = 3
hipotenusa_210 = int(math.sqrt((4 ** 2) + (3 ** 2)))

observador_hipotenusa_210 = hipotenusa_210 >= 5

raio_teste_210 = 15
area_do_circulo_210 = math.pi * (raio_teste_210 ** 2)

coordenadas_circulo_210 = [raio_teste_210, raio_teste_210]
coordenada = [15, 16]

verificador_de_coordenada_x = (coordenada[0] <= coordenadas_circulo_210[0])
verificador_de_coordenada_y = (coordenada[1] <= coordenadas_circulo_210[1])
verificador_de_coordenada = (verificador_de_coordenada_x and verificador_de_coordenada_y)
print(verificador_de_coordenada)

# exercício 3.1

fahrenheit_31 = eval(input('Digite a temperatura em celsius que deseja converter para fahrenheit:'))
celsius_31 = (5 / 9) * (fahrenheit_31 - 32)
print('A temperatura em graus Celsius é', celsius_31)


# exercício 3.8

def average(x, y):
    """retorna a média de x e y"""
    return (x + y) / 2


print(average(2, 3.5))


# exercício 3.9

def perimetro(raio_39):
    if raio_39 > 0:
        area_39 = 2 * math.pi * raio_39
        return area_39
    else:
        pass


print(perimetro(1))


# exercício 3.10

def negativos(lista_310):
    """exibe os números negativos contidos na lista lista_310"""
    for item in lista_310:
        if item < 0:
            print(item)


negativos([4, 0, -1, -3, 6, -9])

# exercício 3.11

help(negativos)
help(average)

# exercício 3.13

time_313 = ['Ava', 'Eleanor', 'Clare', 'Sarah']
time_313[0], time_313[-1] = time_313[-1], time_313[0]

print(time_313)

# exercício 3.14

ingredientes_314 = ['farinha', 'açúcar', 'manteiga', 'maçãs']


def troca_p_u(lista_314):
    lista_314[0], lista_314[-1] = lista_314[-1], lista_314[0]


troca_p_u(ingredientes_314)

print(ingredientes_314)
