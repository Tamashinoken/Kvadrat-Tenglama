'''
| a*x^2 + b*x + c = 0 ko`rinishidagi
| kvadrat tenglamaning ildizlarini diskriminant usulida topuvchi dastur!|
| Muallif: Ashurov Sindor                                               |
| Versiya: 1.0.0.                                                       |
'''

import cmath as cm   #Kompleks sonlar ustida amallar bajarish uchun


#Kvadrat tenglamaning koeffitsiyentlari
a = int(input("Kvadrat tenglamaning birinchi hadini kiriting: "))
b = int(input("Kvadrat tenglamaning ikkinchi hadini kiriting: "))
c = int(input("Kvadrat tenglamaning ozod hadini kiriting: "))

D = b**2 - 4*a*c  #Diskriminantni hisoblaymiz

# Agar D < 0 bo`lsa, tenglamaning haqiqiy ildizlari mavjud bo`lmaydi
# U holda ildizlar kompleks sonlar to`plamiga tegishli bo`ladi
# Ya'ni a + b*j ko`rinishiga ega bo`ladi.
if D < 0:
    print("Tenglama haqiqiy ildizlarga ega emas!")
    x1 = (-b + cm.sqrt(D))/(2*a)
    x2 = (-b - cm.sqrt(D))/(2*a)
    print('Tenglamaning kompleks ildizlari: ','\n', x1,x2)
    
# Agar D = 0 bo`lsa, tenglamaning faqat bitta haqiqiy ildizi mavjud bo`ladi    
elif D == 0:
    print("Tenglama bitta haqiqiy ildizga ega.")
    x = -b/(2*a)
    print(x)
    
# D > 0 bo`lganda tenglama ikkita haqiqiy ildizlarga ega bo`ladi    
else:
    print("Tenglama ikkita haqiqiy ildizga ega.")
    x_1 = (-b + D**(1/2))/(2*a)
    x_2 = (-b - D**(1/2))/(2*a)
    print(x_1, x_2)


