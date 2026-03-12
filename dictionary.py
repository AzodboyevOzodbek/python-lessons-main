# data types (malumot turlari)
#string, int, float, list, bool, dictionary
car = {
    "brand" : "ford",
    "model": "Mustang",
    "year" : 1964,
    'book' : ['bmw', 'mers',]
}
print(car)

print(car["brand"])
print(car["model"])

for book in car["book"]:
    print(book)

#2. yangi key-value qo'shish
car['is_married'] = False
print(car)

# 3. Valuelarni ozgartirish
car["year"] = 2000
print(car)
 
# 5 key-valueni ochirish
talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
print(talaba_0)
del talaba_0['yosh'] # yosh degan kalit so'z (va qiymatni) o'chiramiz
print(talaba_0)

# 6.get() metodi
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }
phone = telefonlar['ali']
print(f"Alining telefoni {phone}")
print(telefonlar.get('vali')) # ga;acy s9
print(telefonlar.get('akmal')) #None