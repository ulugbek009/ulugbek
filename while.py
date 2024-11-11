# # # # # """while thame"""
# # # # # for i in range(100):
# # # # #     print(f"{i+1} teng")

# # # # # while True :
# # # # #     son = int(input("son kiriting :" )) 
# # # # #     print(f"{son}ning kvadrati {son**2} ga teng")
# # # # #     savol = input("Davom etamizmi (yes/no) ?").lower()
# # # # #     if savol == "yes" :
# # # # #         continue
# # # # #     elif savol == "no" :
# # # # #         print("Dastur tugadi!")
# # # # #         break    
# # # # #     else :
# # # # #         print("error")

# # # # while True :
# # # #     son = int(input("yoshingizni kiriting:" ))
# # # #     print(f"2024-{son}") 
# # # #     s =int (input("Davom etamizmi (save/exit) ?"))
# # # #     if s == "save" :
# # # #         continue
# # # #     elif s == "exit" :
# # # #         print("")
# # # #         break    
# # # #     else :
# # # #         print("error")


# # # # cod = 12345678
# # # # print(cod)

# # # # for i in range(3):
# # # #     a = int(input("parol kiriting"))
# # # #     if a == cod :
# # # #         print("Togri javob")
# # # #         break
# # # #     elif a != cod :
# # # #         while 1 :
# # # #             print("xato")

        







     
# # # password = 111
# # # print(password)
# # # urinish = 0
# # # while 1 :
# # #     new_password =int(input("parol kiriting:"))
# # #     if new_password == password :
# # #         print("Tizimga xush kelibsiz !")
# # #         break
# # #     elif new_password != password  :
# # #         urinish += 1
# # #         print(f"{3 -urinish} shuncha urinishingiz qoldi")
# # #         if urinish == 3 :
# # #             while 1 :
# # #                 print("siz parolni 3-marta kiritingiz")




# # while True :
# #     son = input("son kiriting?(chiqish uchun exit)  ")
     
# #     if son.isdigit():
# #         print(f"{son} bu soning kvadrati {int(son)**2} ga teng")
# #     elif son == "exit":
# #         print("Dastur tugadi !")
# #     break


       
# while 1 :
#      yosh = input("yoshingizni kiriting ")
#      if yosh.isdigit():
#           a = {int(yosh)} 
#     elif a == 7:
        
print()

"""11-11-2024"""
from math import sqrt
while 1 :
    son  = input("son kiriting").lower()
    if son .isdigit():
        print(f"siz kiritigan son {son} uning ildzi {sqrt(int(son))}")
    elif son == "exit":
        print("Dastur tugai !")
        break



while True :
    son = int(input("Son kiriting"))
    print(f"siz kiritgan son{son} ning ildiz {sqrt(son)}")


    savol = input("Chqishni hohlaysizmi (yes/no)").lower()
    if savol == "yes":
        print("dastur tugadi !")
        break
    elif savol == 'no' :
        continue
        