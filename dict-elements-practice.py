# Amaliyot
# 1.
gap = {
    "integer": "Butun son",
    "float": "O'nlik son",
    "boolean": "Mantiqiy qiymat",
    "for": "Biror amalni qayta-qayta bajarish tsikli",
    "if": "Shartlarni tekshirish operatori",
}

for key, value in sorted(gap.items()):
    print(f"{key.title()} - {value}")

# 2.
davlatlar = {
    "o'zbekiston": "toshkent",
    "aqsh": "washington d.c.",
    "rossiya": "moskva",
    "tojikiston": "dushanbe",
    "qirg'iziston": "bishkek",
    "qozog'iston": "nursulton",
    "malayziya": "kuala-lumpur",
    "singapur": "sungapur",
    "italiya": "rim",
}
print("Davlatlar:")
for davlat in sorted(davlatlar.keys()):
    print(davlat)

print("Poytaxtlar")
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt)

3.
country = input("Qaysi davlatning poytaxtini bilishni istaysiz?:").lower()
capital = davlatlar.get(country)
if capital == None:
    print("Kechirasiz, bizda bu haqida ma'lumot yo'q")
else:
    print(f"{country.upper()}ning poytaxti {capital.title()} shahri")
