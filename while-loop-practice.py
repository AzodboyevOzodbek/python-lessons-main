# 2.
# savol = "Yoshingizni kiriting: "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         print('Dastur toxtadi')
#         break
#     yosh = int(qiymat)
    
#     if yosh<7:
#         print('sizga 2000 som')
#     elif 7<=yosh<18:
#         print('siga 3000 som')
#     elif 18<=yosh<65:
#         print('sizga 10000 som')
#     else:
#         print('sizga bepul')
# 3.
# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     elif float(qiymat)<0:
#         continue # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")