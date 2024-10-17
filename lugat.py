# # # taomlar = {
# # # 'ali':'osh',
# # # 'vali': 'shashlik',
# # # 'yusup':'chuchvara',
# # # 'olim' : 'banan'
# # # }
# # # print(taomlar['ali'])
# # # print(f"alining sevimli taomui {taomlar['ali']}")



# # # buyumlar = {
# # # "ism":"ali",
# # # "yosh":"15",
# # # "student":True,
# # # "oila":["ota","ona","oka"],
# # # "Fanlar":{
# # #     "matematika":50,
# # #     "ingiliz_tili":45
# # # }
# # # }

# # # print(buyumlar)


# # # """qiymat qoshish"""
# # # taomlar["ali"]='norin'
# # # taomlar["yusup"]=input("yusupni taomi ?")
# # # print(taomlar)

# # # taomlar.update({"muhamadyusuf":"manti"})
# # # print(taomlar)
# # # """qiymat ozgartirish / update"""
# # # taomlar["hasan"]='qozon kabob'
# # # print(taomlar)

# # # taomlar.update({"olim:manti"})
# # # print(taomlar)

# # # """qiymat ochirish"""
# # # del taomlar ["olim"]
# # # print(taomlar)

# # # taomlar.pop("hasan")
# # # print(taomlar)

# # # taomlar.popitem()#royhatni ohirgi elementini ochiradi
# # # print(taomlar)

# # # """royhatni tozalash"""
# # # taomlar.clear()
# # # print(taomlar)


# # onam = {
# #     "onam":"Umida",
# #     "yil" :1976,
# #     "manzil":"namangan"
# # }
# # print(f"Bu mening onam uning ismi {onam['onam']} u {onam['yil']} tugilgan biz {onam['manzil']} yashaymiz")




# # otam = {
# #     "otam":"Ahadhon",
# #     "yili" :1974,
# #     "manzili":"namangan"
# # }
# # print(f"Bu mening otam uning ismi {otam['otam']}u {otam['yili']} tugilgan biz {otam['manzili']} yashaymiz")


# # opam = {
# #     "opam":"maftuna",
# #     "tugilgan" :2008,
# #     "yashash":"namangan"
# # }
# # print(f"Bu mening opam uning ismi {opam['opam']}u {opam['tugilgan']} tugilgan biz {opam['yashash']} yashaymiz")



# """2-mashq"""
# # phyton = {
# #     "if":"agar",
# #     "else":"aks holda",
# #     "for" : "uchun",
# #     "bool" :"mating qiymat",
# #     "elif" : "yoki",
# #     "update": "yangilash",
# #     "claer" : "tozalamoq",
# #     "del" : "ochirmoq",
# #     "true": "togri",
# #     "false" : "notogri"
# # }

# """3-mashq"""
# fan = {
#     "men":"matematika",
#     "bilol":"algebra",
#     "giyos":"ingiliz_tili"

# }
# fan ["said akbar"] = "geometriya"
# fan["yusup"]=input("yusupni fani? ")

# fan["saidakbar"]='informatika'
# fan.update({"men:russ_tili"})

# del fan ["bilol"]
# fan.pop("said akbar")
# fan.popitem()

# """royhatda nusxa olish"""
# taomlar= ["mastava"]
# meals = taomlar.copy()
# print(meals)


# meals = dict(taomlar)
# print(meals)


# """get - metodi"""
# ismlar = {
#     "axror":"5",
#     "mansur":"4"
# }
# print(f"salom , {ismlar['ali']}")
# print(f"salom , {ismlar.get("ali", "55")}")


# """items()"""
# print(taomlar)
# print(taomlar.items())

# for key , value in taomlar.items:
#     print(f"{key.title()}ning sevimli taomi {value.title()}")