# Dictionary elementari bilan ishlash
phone = {
    'brand' : "Apple",
    'model' : "iphone 17 pro Max",
    'color' : "silver",
    'storage' : "256GB",
    'price' : '$1500'
}

# get() metodi - kalit orqali qiymat olish
# print(phone.get('model'))
# print(phone.get('price'))
# print(phone.get('battery'))
# print(phone.get('battery',"kalit topilmadi"))

# items() metodi - lug'at elementlarini (kalit, qiymat) juftliklar ko'rinishida olish
print(phone.items()) #dict_items([('brand', 'Apple'), ('model', 'iphone 17 pro Max'), ('color', 'silver'), ('storage', '256GB'), ('price', '$1500')])
# for key, value in phone.items():
#     print(f"{key} : {value}")

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }

# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")

# keys() metodi - lug'atning barcha kalitlarini olish
print(phone.keys()) #dict_keys(['brand', 'model', 'color', 'storage', 'price'])
for k in phone.keys():
    print(k)

mahsulotlar = { # Do'kondagi mahsulotlar
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }

print(mahsulotlar.keys())

print("Do'konimizdagi mahsulotlar:")    
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())

# in operatori
# 1. list elementlari orasida qiymatning mavjudligini tekshirish
# 2. kalitlar orasida kalitning mavjudligini tekshirish
bozorlik = ['non', 'anor', 'uzum', 'baliq']
# print('anor' in bozorlik) # True
# print('olma' in bozorlik) # False

# mahsulot = input("Nima sotib olmoqchisiz? ")
# if mahsulot in bozorlik:
#     print(f"{mahsulot.title()} do'konimizda bor.")
# else:
#     print(f"{mahsulot.title()} do'konimizda yo'q.")

# mahsulotlar bu lugat
for mahsulot in mahsulotlar:
    print(mahsulot)

print(sorted(mahsulotlar))

# values() metodi - lug'atdagi qiymatklarni list ko'rinishida olish
print(mahsulotlar.values()) #dict_values([10000, 20000, 40000, 25000, 30000])
print("do'konimizdagi mahsulotlarning narxlari:")
for narx in mahsulotlar.values():
    print(narx)

