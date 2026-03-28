# Amaliyot 
# 1.
# def tygulgan_yilni_hisobla(ism, yosh):
#     print(f"{ism.title()} {2026-yosh} da tug'ilgan")

# ism = input("Ismingizni kiriting: ")
# yosh = int(input("Yoshingizni kiriting: "))
# tygulgan_yilni_hisobla(ism, yosh)

# 2.
# def sonni_kvadratini_va_kubini_hisobla(son):
#     print(f"{son} ning kvadrati {son**2} ga teng")
#     print(f"{son} ning kubi {son**3} ga teng")

# son = int(input("Son kiriting: "))
# sonni_kvadratini_va_kubini_hisobla(son)

# 3.
# def sonni_juft_yoki_toq_ekanligini_hisobla(son):
#     if son % 2 == 0:
#         print(f"{son} juft son")
#     else:
#         print(f"{son} toq son")

# son = int(input("Son kiriting: "))
# print(sonni_juft_yoki_toq_ekanligini_hisobla(son))

# 4.
# def sonni_katta_kichik_hisobla(son1, son2):
#     if son1 > son2:
#         print(son1)
#     elif son1 < son2:
#         print(son2)
#     else:
#         print("Sonlar teng")
# son1 = int(input("1-sonni kiriting: "))
# son2 = int(input("2-sonni kiriting: "))
# print(sonni_katta_kichik_hisobla(son1, son2))

# 5 , 6.
# import math
# def x_va_y(x, y = 2):
#     print(math.pow(x, y))

# x = int(input("x ni kiriting: "))
# y = int(input("y ni kiriting: "))
# print(x_va_y(x, y))

# 7.
def bolinishni_tekshir(n):
    for i in range(2, 11):
        if n % i == 0:
            print(f"{n} soni {i} ga qoldiqsiz bo'linadi")

son = int(input("Son kiriting: "))
print(bolinishni_tekshir(son))