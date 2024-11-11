# # name = " AnToNy "
# # print(name.rstrip())
# # print(name.lstrip())
# # print(name.lower())
# # print(name.upper())
# # print(name.title())
# # """2-mashq"""
# # ismlar = ["ali","bobur","ravshan","olim","husan","ulugbek"]
# # print(len(ismlar))
# # ismlar.sort(reverse=True)
# # print(ismlar.remove("ali"))
# # print(ismlar.insert(1,"bobur"))
# # print(ismlar.insert(2,"ravshan"))
# # """3-mashq"""
# # from math import sqrt
# # for s in range(101,700,2):
# #     if s < 200 :
# #         print(s**2)
# #     elif s >300 or s < 400 :
# #         print(sqrt(s))
# #     elif s >500 or s <=700 :
# #         print(s**4)
# """4-mashq"""
# yosh = int(input("yoshingizni kiriing:"))
# if  7<= yosh <18 :
#     print("nechinchi sinifda oqiysiz:")
# if yosh < 0 :
#     print("notogri son kiritingiz")
# elif yosh > 101 :
#     print("notogri son kiritingiz")

"""5-mashq"""
dav =  {
    "qazaqistan":"astana",
    "qirgiz":"bishkek",
    "uzb" : "toshkent",
    "russ":"moskva",
    "ukr":"kiyev",
    "tjk":"dushanbe"
}
q = input("biror davlat yoki poytaht kiriting:").upper()
for d,s in dav.items() :
    if q == d :
        print(s)
    elif q == s :
        print(d)
if q not in dav.keys() and q not in  dav.values():
    print("Bizda bundy malumot yoq !")
    