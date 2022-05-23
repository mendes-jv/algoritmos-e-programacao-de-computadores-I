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

# exercício 3.2

idade_32 = 63
if idade_32 > 62:
    print('Você pode obter benefícios de pensão')

nome_32 = 'Musial'
lista_32 = ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']
if nome_32 in lista_32:
    print('Um dos 5 maiores jogadores de beisebol de todos os tempos!')

golpes_32 = 15
defesa_32 = 0
if (golpes_32 > 15) and (defesa_32 == 0):
    print('Você está morto…')

norte_32 = leste_32 = oeste_32 = False
sul_32 = True
if norte_32 or sul_32 or leste_32 or oeste_32:
    print('Posso escapar.')

# exercício 3.3

ano_33 = 366
if (ano_33 % 4) == 0:
    print('Pode ser um ano bissexto.')
else:
    print('Definitivamente não é um ano bissexto.')

bilhete_33 = 40028922
loteria_33 = 40028922
if bilhete_33 == loteria_33:
    print('Você ganhou!')
else:
    print('Melhor sorte da próxima vez…')

# exercício 3.4

login_usuario_34 = input('Digite o login:')
lista_autenticacao_34 = ['joe', 'sue', ' hani', 'sophie']


def autenticacao(login_34, lista_34):
    if login_34 in lista_34:
        print('Voce entrou!')
    else:
        print('Usuário desconhecido.')
    print('Fim.')


autenticacao(login_usuario_34, lista_autenticacao_34)

# exercício 5.1

peso_real_51 = 92.5
altura_real_51 = 1.83


def meu_imc(peso_51, altura_51):
    imc = peso_51 / (altura_51 ** 2)
    if imc < 18.5:
        print('Abaixo do peso')
    elif 18.5 <= imc < 25:
        print('Normal')
    else:
        print('Sobrepeso')


meu_imc(peso_real_51, altura_real_51)


# exercício 3.8

def average(x_38, y_38):
    """retorna a média de x e y"""
    return (x_38 + y_38) / 2


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

# exercício 3.5

lista_35 = ['pare', 'desktop', 'tio', 'pote']

for item in lista_35:
    print(item)

# exercício 3.6

for numero in range(0, 9):
    print(numero)

for numero in range(0, 1):
    print(numero)

# exercício 3.7

for numero in range(3, 13):
    print(numero)

for numero in range(0, 9, 2):
    print(numero)

for numero in range(0, 24, 3):
    print(numero)

for numero in range(3, 12, 5):
    print(numero)

# exercício 4.1

s_41 = '0123456789'

a_41 = s[2:4]
b_41 = s[7:8]
c_41 = s[1:7]
d_41 = s[0:3]
e_41 = s[7:9]

# exercício 4.2

previsao_42 = 'It will be a sunny day today'

cont_42 = previsao_42.count('day')
clima_42 = previsao_42.find('sunny')
troca_42 = previsao_42.replace('sunny', 'cloudy')
print(previsao_42)

# exercício 5.9

t = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 6]]
s = [[0, 1, 2, 0], [0, 1, 1, 1], [0, 1, 0, 0]]


def soma_2d(lista1_59, lista2_59):
    for i in range(len(lista1_59)):
        for j in range(len(lista1_59[i])):
            lista1_59[i][j] += lista2_59[i][j]
    print(lista1_59)


soma_2d(t, s)
