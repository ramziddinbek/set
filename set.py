# Set => bitta o'zgaruvchida bir nechta qiymat saqlash uchun foydalaniladi.
# Set {} qavs orqali yozib olinadi.


xona={"Doska", "Proektor", "Stol", "Stul"}

# List => o'zgartirib bo'ladigan (changeable), tartiblab bo'ladigan (ordered), elementlarni takrorlab bo'ladigan (allow duplicate)
# Tuple => o'zgartirib bo'lmaydigan(unchangeable), tartiblab bo'ladigan(ordered), elementlarni takrorlab bo'ladigan (allow duplicate)
# Set => o'zgartirib bo'lmaydigan(unchangeable), tariblab bo'lmidigan(unordered), elementlarni takrorlab bo'lmidigan(not allow duplicate)
# Ammo setni elementlarini o'chirsa bo'ladi va yangi element qo'shsa bo'ladi. 





# len()  => element uzunligini tekshirib olish uchun foydalaniladi.

telefon={"Xiaomi", "Apple", "Samsung"}
print(len(telefon))


# type() => qanaqa ma'lumot turlaridan tashkil topganligini ko'rsatib beradi


qismlar={"Klaviatura", "Monitor", "Sistema blok", "Sichqoncha"}
print(type(qismlar))


# set() => Set yaratib olish uchun konstruktor
mevalar=set(("Olma", "Anor", "Banan", "Gilos"))
print(type(mevalar))


# for loop orqali elementlarni olish

sonlar={10,20,5,-9,55}

for i in sonlar:
    print(i)
    
    
# add() => setga yangi element qo'shish uchun ishlatiladi

ranglar={"Qizil", "Qora", "Yashil", "Kulrang"}
ranglar.add("Ko'k")
print(ranglar)


# update() => bir setdagi elementlarni boshqa bir setga qo'shish uchun foydalaniladi. Setda ayni bir tur bo'lishi kerak emas

football={"Real Madrid", "Atletiko"}
football2={"Barselona", "Valensiya"}
football3=["Liverpool", "Arsenal"]

football.update(football2,football3)
print(football)

# remove() yoki discard() => setdagi elementlarni o'chirish uchun ishlatiladi

laptop={"Acer", "Lenovo", "Apple", "Hp"}
laptop.remove("Acer")
laptop.discard("Lenovo")
print(laptop)


# Elementni olib tashlash uchun pop() usulidan ham foydalanishingiz mumkin, ammo bu usul oxirgi elementni olib tashlaydi. Esda tutingki, to'plamlar tartibsiz, shuning uchun qaysi element olib tashlanishini bilmay qolasiz.

raqamlar={0,1,3,5,7,8,9}
raqamlar.pop()
print(raqamlar)


# clear() => setni to'laligicha o'chirib beradi.

boolean={True,False}
boolean.clear()
print(boolean)



# del => setni to'laligicha o'chirib beradi. Setni xam o'chirib yuboradi.

tillar={"python", "java", "php", "C++"}
del tillar
print(tillar)


# for loop orqali setdagi elementlarni chiqarish

pul_birligi={"So'm", "Dollar", "Yevro"}

for i in pul_birligi:
    print(i)
    
    
# union() => usuli ikkala to'plamdagi barcha elementlar bilan yangi to'plamni qaytaradi

set1={"SSD", "HDD"}
set2={"Videokarta", "Operativ xotira"}

set3=set1.union(set2)
print(set3)



# Intersection_update() => usuli faqat ikkala to'plamda mavjud bo'lgan elementlarni saqlaydi.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)


# Intersection() =>  usuli faqat ikkala to'plamda mavjud bo'lgan elementlarni o'z ichiga olgan yangi to'plamni qaytaradi.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)



# Symmetric_difference_update() => usuli faqat ikkala to'plamda YO'Q elementlarni saqlaydi.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)



# Symmetric_difference() usuli yangi to'plamni qaytaradi, u faqat ikkala to'plamda YO'Q elementlarni o'z ichiga oladi.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)



 # Python da , frozenset to'plam bilan bir xil, faqat frozensesetlar o'zgarmasdir, ya'ni frozenseset elementlarini yaratilgandan keyin qo'shish yoki olib tashlash mumkin emas. 
 # Bu funktsiya ma'lumotlarni har qanday takrorlanadigan ob'ekt sifatida qabul qiladi va ularni o'zgarmas ob'ektga aylantiradi. Elementlarning tartibi saqlanishi kafolatlanmaydi.
 
nu = (1, 2, 3, 4, 5, 6, 7, 8, 9)
fnum = frozenset(nu)
print("frozenset Object is : ", fnum)