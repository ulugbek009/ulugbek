# # # # # # # 9B001
# # # # # # """1-mashq"""
# # # # # # ism  = "ulugbek"
# # # # # # familiya  = "azimjanov"
# # # # # # yosh = 16
# # # # # # kitoblar = [] 
# # # # # # print(type(ism))
# # # # # # print(type(familiya))
# # # # # # print(type(yosh))
# # # # # # print(type(kitoblar))
# # # # # # """2-mashq"""

# # # # # # from math import sqrt
# # # # # # a = (4364+1233)
# # # # # # b = (sqrt(a))
# # # # # # print(range(b,2))
# # # # # """3-mashq"""
# # # # # son  = int(input("son kiriting"))
# # # # # son1  = int(input("son kiriting"))
# # # # # print(son**2/23)
# # # # # print(son1**2/23)
# # # # # """4-mashq"""
# # # # # s = int(input("butun son kiriting"))
# # # # # print(s)
# # # # # print(type(s))
# # # # # s = float 
# # # # # print(s)
# # # # # print(type(s))
# # # # # # """5-mashq"""
# # # # # kitob = []
# # # # # for k in range(5):
# # # # #     k = input("biror kitob kiriting")
# # # # #     kitob.append(k)
# # # # # print(kitob)
# # # # # """6-mashq"""
# # # # # student = ["ali","maruf","bahrom"]
# # # # # student.append("ulugbek")
# # # # # student.insert(3,"muhammad yusuf")
# # # # # student.insert(-1,"shodiyor")
# # # # # student[1] = "jamshid"
# # # # # student[-1] = "bilol"
# # # # # 9B002
# # # # # """1-mashq"""
# # # # # import random
# # # # # a = int(input("biror son kiriting"))
# # # # # b = int(input("biror son kiriting"))
# # # # # print(random.randrange(a,b))
# # # # # """2-mashq"""
# # # # # kitobhon = []
# # # # # ism = input("brat ismingizni kiriitng")
# # # # # for o in range(5):
# # # # #     oqigan = input("oqigan kitoblaringizni kiriting")
# # # # #     kitob.append(oqigan)
# # # # #print(kitobhon)
# # # # # del kitobhon[1]
# # # # # kitobhon.insert(2,"alisher")
# # # # # kitobhon.insert(3,"xoji") 


# # # # # """3-mashq"""
# # # # fanlar = ['matematika','ingiliz tili']
# # # # fanlar.append('russ tili')
# # # # fanlar.insert(-1,"geografiya")
# # # # fanlar[2]='texnologiya'
# # # # fanlar[-1]="fizika"
# # # # print(fanlar)
# # # # del fanlar[-1]
# # # # fanlar.pop()
# # # # fanlar.remove("matematika")

# # # # """4-mashq"""
# # # # # familiya = []
# # # # # swom = int(input("oilangizda nichi kishi sila:"))
# # # # # for s in range(swom) :
# # # # #     s =input("oilangizni azolarini ismini kiriting:")
# # # # #     familiya.append(s)
# # # # # print(familiya)
# # # # """5-mashq"""
# # # car = ['malibu','monza','treker','onix','bmw','mers',]
# # # print(len(car))
# # # print(sorted(car))
# # # car.sort(reversed=True)
# # # car.reverse()
# # # print(car)
# # # print(len(car))
# # # print(sorted(car))
# # # 9B004
# # """1-mashq"""
# # # sonlar = [45,-96,0,63.2,1257,-6752.2,42,3,542]
# # # print(sorted(sonlar))
# # # sonlar.sort(reversed=True)
# # # sonlar.reverse()
# # """2-mashq"""
# # mevalar = ['olma','orik','shaftoli','apelsin','malina','xormo']
# # for meva in mevalar:
# #     if meva == "olma" or  meva== "malina":
# #         print(meva.upper())
# #     else:
# #         print(meva.title())
# # """3-mashq"""
# # boks = {
# #     "eng qimati":"qizil kitob",
# #     "zori":"zangor kitob"

# # }
# # boks["ali"]='5 bohodir'
# # boks["yusup"]=input("yusupni kitobini ?")
# # print(boks)

# # boks.update({"muhamadyusuf":"3 bohodir"})
# # print(boks)
# # boks["zori"]='molhona'
# # print(boks)

# # boks.update({"eng qimati:skazki"})
# # print(boks)
# # del boks ["zori"]
# # print(boks)

# # boks.pop("eng qimati")
# # print(boks)

# # boks.popitem()
# # print(boks)
# # """4-mashq"""
# # from math import sqrt
# # for s in range(102,2020):
# #     if s < 1000 :
# #         print(s**3)
# #     elif s > 1500:
# #         print(s-4)
# #     if s %7 == 0:
# #         print(sqrt(s))
# """5-mashq"""
# urin = int(input("nechinchi urini oldingiz otgan imtihonda:"))
# foiz = int(input("necha foiz bilan:"))
# if foiz <= 0 and foiz >= 64:
#     print("imtihondan ota olmadingiz")
# elif foiz >= 65 or foiz <= 85 :
#     print("imtihondan otdingiz")
# if urin == 1 and foiz >=85 :
#     print("100%  grandsiz")
# elif urin == 2 and foiz >= 85:
#     print("75% grand siz")
# elif urin == 3 and foiz >= 85:
#     print("50% grand")
# elif urin == 4 and foiz >= 85:
#     print("25% grand")
# # else:
#     print("Togri son kiriting")
# # 9B005
# """1-mashq"""
soz = input("biror soz kiriting:")
language =  {
    "olma":"apple",
    "moshina":"car",
    "qulupnay":"strawbery",
    "joy" : "accomadition",
    "hech qachon":"never"
}
if language in soz  : 
    print(f"{language} mana tarjimasi")
elif language not in soz :
    print("bizda bunday son mavjud emas")







