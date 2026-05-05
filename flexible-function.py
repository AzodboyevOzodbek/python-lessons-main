# return function
# def sum_list(lst):
#     s = 0
#     for n in lst:
#         s += n
#     return s

# print(sum_list([15,3,62,56,25,-54]))

# flexible(moslashuvchan) function
# def summa(*sonlar):
#     s = 0
#     for n in sonlar:
#         s += n
#     return s

# def avto_info(kompaniya,model, **malumotlar):
#     malumotlar['kompaniya'] = kompaniya
#     malumotlar['model'] = model
#     return malumotlar
# print(avto_info('GM', 'Malibu', rang='qora', yil=2024, narh=35000))
# print(avto_info('Tesla', 'Model S', rang='oq', yil=2026, narh=90000, batareya='100 kWh'))

def my_function(**kwargs):
    print("His last name is " + kwargs["lname"])
my_function(fname="John", lname="Doe")

# AMALIYOTLAR
# 1.
def kopaytma(*sonlar):
    natija = 1
    for n in sonlar:
        natija *= n
    return natija
print(kopaytma(2, 3, 4))
# 2.
def talabalar(ism,familiya, **malumotlar):
    malumotlar['ism'] = ism
    malumotlar['familiya'] = familiya
    return malumotlar
print(talabalar('Ali', 'Valiyev', yosh=20, fakultet='Informatika'))
# 3.
def find_max(*sonlar):
    if len(sonlar) == 0:
        return None
    max_son = sonlar[0]
    for n in sonlar:
        if n > max_son:
            max_son = n
    return max_son
print(find_max(5, 10, 3, 8, 2))