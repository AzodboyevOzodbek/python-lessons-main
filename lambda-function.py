# lambda funktion - anonymous(maxfiy,nomsiz) function
# square = lambda x: x**2
# print(square(5))

# import math
# uzunluk = lambda pi , r: 2 * pi * r
# print(uzunluk(math.pi, 5))

# def daraja(n):
#     return lambda x: x ** n
# kvadrat = daraja(2)
# kub = daraja(3)
# print(kvadrat(5))

# from math import sqrt
# sonlar = list(range(11))
# ildizlar = list(map(sqrt,sonlar))
# print(ildizlar)

# numbers = list(map(int, input().split()))
# print('hello world'.split())
# print('0 1 2 3 4 5'.split())
sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati

# def daraja2(x):
#     """Berilgan sonning kvadratini qaytaruvchi funksiya"""
#     return x*x

# print(list(map(daraja2,sonlar)))

# kvadratlar = list(map(lambda x:x*x,sonlar))
# print(kvadratlar)

# map() bolmaganda
# kvadratlar = []
# for son in sonlar:
#     kvadratlar.append(son*son)
# print(kvadratlar)

# a = [4, 5, 6]
# b = [7, 8, 9]
# a_plus_b = list(map(lambda x,y:x+y,a,b))
# print(a_plus_b)

