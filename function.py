# Function - ma'lum bir vazifani bajaruvchi kod bloklari
# ularni qayta ishlatish mumkin va ular dastur tuzilishini yaxshilaydi
# def salom_ber():
#     print("Assalomu alaykum!")

# salom_ber()  # Funksiyani chaqirish

# 2. Funksiyaga qiymat uzatish
# def salom_ber(ism):
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")

# salom_ber('hasan')

# 3. default qiymat berish
# def yosh_hisobla(ism = "Olim", tugilgan_yil = 1967):
#     print(f"{ism.title()} {2026-tugilgan_yil} yoshda")

# yosh_hisobla('hasan', 1990)
# yosh_hisobla()

# n1
# def yosh_hisobla(tugilgan_yil, joriy_yil=2020):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
# tyil = input("Tug'ilgan yilingizni kiriting: ")
# yosh_hisobla(int(tyil))

# n2
# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")

# salom_ber('hasan')

# n3
# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
 
# toliq_ism('olim', 'hakimov')