# Amaliyot
# 1.
# otam = {'ismi':'Rasulbek', 'tyil':1980,'viloyat':'Xorazm'}
# tyil = otam['tyil']
# vil = otam['viloyat']
# print(f"Otamning ismi {otam['ismi'].title()}, {tyil}-yilda, {vil.title()} viloyatida tug'ilgan")
# # 2.
# taomlar = {
#     'otam':'osh',
#     'onam':'shashlik',
#     'opam':"so'msa",
#     'opam2':"norin"
#     }

# taom = taomlar['opam']
# print(f"Opamning sevimli taomi {taom}")

# 3.
soz = {
    'integer':"Butun son",
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat"
}
# kalit = input("Kalit so'z kiriting:")
# print(soz.get(kalit,"Bunday so'z mavjud emas"))

# 4.
kalit = input("Kalit so'z kiriting:").lower()
print(soz.get(kalit,"Bunday so'z mavjud emas"))

kalit = input("Kalit so'z kiriting:").lower()
tarjima = soz.get(kalit)
if tarjima==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
    