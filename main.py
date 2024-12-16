# 1 misol
# def darajaga_kotarish(number):
#     return number ** 2
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# res = map(darajaga_kotarish,numbers)
# print(list(res))


#  2 misol
# def chekker(hariflar: str):
#     return hariflar.isupper()
#
#
# a = ["A", "a", "B", "b", "C", "c", "D", "d"]
# res = filter(chekker,a)
# print(list(res))

# 3  misol
# def check_number(a: str):
#      if a.startswith ("+998"):
#         return f" uzb -->{a}"
#
#      elif a.startswith ("+7"):
#          return f"RU  -->{a}"
#      elif a.startswith  ("+14"):
#          return f"peru-->{a} "
#      else:
#          "bilmadim"
#
#
# phone_numbers = ["+998991234567", "+79454874459", "+14385001031"]
# res = map(check_number,phone_numbers)
# print(list(res))


# 4 misol
# def capitaliz(a:str):
#     return a.capitalize()
#
# names = ['alfred', 'tabitha', 'william', 'arla']
# res = map(capitaliz,names)
# print(list(res))
#

#  5 misol
# def integer(a: int):
#     if a > 75:
#         return a
#
# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = filter(integer,scores)
# print(list(res))


#  6 misol
# BU Lyambda MAVZUSINI OTMAGNMIZ USTOZ SHUNGA BAJARA OLMADIM OTGAN DARSDA ULGURMAGAN EDIK KORGANI


#  7 misol
# def uzunlik(a:str):
#     return len(a)
#
# b= ['apple', 'banana', 'cherry']
# res = map(uzunlik,b)
# print(list(res))
#

#  8 misol
# def birlashtirish(a, b):
#     birlashgan_royxat = []
#     for i in range(len(a)):
#         birlashgan_royxat.append(a[i] + b[i])
#     return birlashgan_royxat
#
# a1 = ['apple', 'banana', 'cherry']
# b1 = ['orange', 'lemon', 'pineapple']
#
# natija = birlashtirish(a1, b1)
# print(natija)


#  9 misol
# a=['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# b=["Sobir", "Bakir", "Jalil", "Toxir"]
# c= a + b
# print(c)

#  10 misol
# def counter(lst, element):
#     count = lst.count(element)
#     return count
# lis = [1, 2, 3, 4, 2, 2, 5, 1]
# a = 2
# print(f"{a} elementi ro'yxatda {counter(lis, a)} marta takrorlangan.")

#  11 misol
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# common_elements = list(set(a) & set(b))
# print("Umumiy elementlar:", common_elements)

#  12 misol
# programming_languages = ['Python', 'C', 'C++', 'C#', 'Java', 'Basic', 'Kotlin', 'Pascal', 'JavaScript', 'Go', 'Dart',
#                          'Assambler', 'Ruby', 'Rust', 'Mojo', 'Swift', 'Php']
#
# print(programming_languages[0::2])

#  13 misol
# programming_languages = ['Python', 'C', 'C++', 'C#', 'Java', 'Basic', 'Kotlin', 'Pascal', 'JavaScript', 'Go', 'Dart', 'Assambler', 'Ruby', 'Rust', 'Mojo', 'Swift', 'Php']
# print(programming_languages[5::])

#  14 misol
# from collections import namedtuple
# Talaba = namedtuple('Talaba', ['ismi', 'guruh', 'baho'])
#
# talabalar = [
#     Talaba('Toxir', 'fn24', 89.5),
#     Talaba('Sobir', 'fn25', 92.0),
#     Talaba('Bakir', 'fn26', 85.3),
#     Talaba('Jalil', 'fn27', 95.7),
#     Talaba('Abdulla', 'fn28', 90.4),
# ]
#
# eng_yuqori_baho_talaba = max(talabalar, key=lambda t: t.baho)
#
# print("Eng yuqori o'rtacha bahoga ega talaba:")
# print(f"Ismi: {eng_yuqori_baho_talaba.ismi}")
#
# print(f"O'rtacha baho: {eng_yuqori_baho_talaba.baho}")



# 15 misol
# def generator():
#     for i in range(1, 21):
#         yield i ** 2
# for i in generator():
#     print(i)


#  16 misol
# def lengh():
#     def olchash(matn):
#         return len(matn)
#     return olchash
# uzunlik = lengh()
# matn = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
# print(f"Berilgan matn uzunligi: {uzunlik(matn)}")


#  17 misol
# def salomlashuvchi():
#     def salom(ism):
#         return f"Salom, {ism}!"
#     return salom
# salom_funksiya = salomlashuvchi()
# ism = input("ismingizni kiriitng: ")
# print(salom_funksiya(ism))