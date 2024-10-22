# # """or-va -and"""
# # sonlar= [1,2,34,5,6,78,9]
# # for son in sonlar:
# #     if son <5 or son > 5 :
# #         print(f"{son} 5ga teng emas")

# yusup =True

# # son =int(input("son kiriting :"))
# # # if son > 0 :
# # #     print(f"{son} musbat")
# # #     if son%2 == 0:
# # #         print(f"{son} juft")
# # #     else :
# # #         print(f"{son}-toq")
# # # elif son < 0 :
# # #     print(f"{son}  manfiy")








# # # """2-mashq"""
# # # from math import sqrt
# # # sonlar  = list(range(100,500,2))
# # # for son in sonlar :
# # #     if son < 300:
# # #         print(f"{son}  {son**4}")
# # #     elif son > 350 and son <=400 :
# # #         print(f"{sqrt(son)}  ")
# # #         print(round(son,3))
# # #     elif son > 420 and son <=480 :
# # #         print(f"{son/3.5}")
# # #     elif son > 480 and son <=500 :
# # #         print(f"{son**6}")



# # """3-mashq"""
# # baho  = int(input("otgan hafta necha ball olgansiz:"))
# # if baho>=0 and baho<=40 :
# #     print("sizning natijangiz juda yomon:")
# # elif baho>=41 and baho<=60 :
# #     print("sizning natijangiz qoniqarli:")
# # elif baho>=61 and baho<=80 :
# #     print("sizning natijangiz yaxshi:")
# # elif baho>=81 and baho<=99 :
# #     print("sizning natijangiz a'lo:")
# # elif baho == 100 :
# #     print("tabriklaymiz siz 100 ball oldingiz")
# # else :
# #     print("hato")

# # """4-mashq"""
# # baho  = int(input("otgan hafta necha ball olgansiz:"))
# # if baho>=0 and baho<=20 :
# #     print("sizning natijangiz juda yomon:")
# # elif baho>=21 and baho<=35 :
# #     print("sizning natijangiz qoniqarli:")
# # elif baho>=36 and baho<=45 :
# #     print("sizning natijangiz yaxshi:")
# # elif baho>=46 and baho<=49 :
# #     print("sizning natijangiz a'lo:")
# # elif baho == 50 :
# #     print("tabriklaymiz siz 100 foizlik natija")
# # else :
# #     print("hato")
# # """5-mashq"""
# # mahsulotlar = ['olma','banan','qulupnay','anor','non','qaymoq']
# # xarid = []
# # yoq = []
# # print("Assalomu aleykum dokonimizga hush kelibsiz! :")
# # print("bizda quydagi mahsulotlar bor", end = '')
# # for mahsulot in mahsulotlar :
# #     print(f"{mahsulot}",end = '')
# # savol = int(input("nechta mahsulot olmoqchisiz:"))





# # """hayvonot bog'i"""
# # baho  = int(input("yoshingizni kiriting:")) 
# # if baho>=1 and baho<=7:
# #     print("marhamat sizga bepul kiravering:")
# # elif baho>=70 and baho<=100 :
# #     print("marhamat sizga bepul kiravering:")
# # elif baho>=8 and baho<=18 :
# #     print("sizga kirish narhi 5ming som:")
# # elif baho>=19 and baho<=69 :
# #     print("sizga kirish narxi 10ming som:")
# # elif baho < 0 :
# #     print("musbat son kiriting")
# # else :
# #     print("bizda faqat 100 yosh gacha")
# # """1-mashq"""
# # cars = ['toyota','mazda','hyunday','gm','kia']
# # for s in cars :
# #     if s == 'gm':
# #         print(s.upper())
# #     else :
# #          print(s.capitalize())

 

# # """2-mashq"""
# # son  = int(input("son kiriting :"))
# # from math import sqrt
# # if son > 0:
# #     print(sqrt(son))
# # elif son < 0 :
# #     print("musbat son kiriting")
# # else:
# #     print("hato")
# """3-mashq"""

# def parol_tasdiqlash():
#     while True:
#         parol = input("Iltimos, 8 ta belgidan iborat parol kiriting: ")
#         if len(parol) == 8:
#             print("Parol muvaffaqiyatli kiritildi!")
#             break
#         else:
#             print("Xato! Parol 8 ta belgidan iborat bo'lishi kerak.")

# parol_tasdiqlash()


# # """6-mashq"""
ism = input("assalomu aleykum ismingizni kiriting")
yosh = int(input("yoshingizni kiriting"))
pol = input("og'ilbola misi yoki qiz bola")

if pol == "og'il bola" and yosh == 15:
    print(f"assalomu aleykum 9-blue sinfiga kirishiz mumkin {ism.title()}")
elif  pol == "qiz bola" and yosh == 15:
    print(f"assalomu aleykum 9-green sinifiga kirishiz mumkin {ism.title()}")
else:
    print("Bizda faqat 15 yoshdagilar kerak")


ism = input(" ismingizni  kiriting :")
if ism :
    print("Rahmat!")
else :
    print("siz hech narsa kiritmadingiz!") 




restoran = {
"yusuf":"5teks"

}
