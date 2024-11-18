from datetime import datetime
from itertools import count
from random import random
import random

# Задание 1

# Вариант 11
#Даны три числа a, b, c. Значение наибольшего из них присвоить переменной d.
print("======= Задание 1. Вариант 11 =======")
a = int(input("Введите число a:\n"))
b = int(input("Введите число b:\n"))
c = int(input("Введите число c:\n"))

d = max(a, b, c)

print(f"Максимальное число равно {d}\n")

# Задание 2

# Вариант 3
# В каждом учащемся класса известны его пол, год рождения, рост и вес.
# Определить, сколько в классе мальчиков и сколько девочек. Найти средний возраст мальчиков и девочек.
# Определить, верно ли, что самый высокий мальчик весит больше всех в классе,
# а самая маленькая девочка является самой юной среди девочек.

# Данные об учениках: пол, год рождения, рост , вес
print("======= Задание 2. Вариант 3 =======")
students = [
    {"sex": "male", "birthYear": 2010, "height": 160, "weight": 70},
    {"sex": "male", "birthYear": 2011, "height": 175, "weight": 60},
    {"sex": "male", "birthYear": 2009, "height": 168, "weight": 65},
    {"sex": "female", "birthYear": 2012, "height": 145, "weight": 46},
    {"sex": "female", "birthYear": 2011, "height": 150, "weight": 48},
    {"sex": "female", "birthYear": 2009, "height": 148, "weight": 54},
]

boysCount = 0
girlsCount = 0
boysAgeSum = 0
girlsAgeSum = 0
# float('inf') используется для инициализации переменной значением, которое представляет бесконечность.
# Это делается для того, чтобы гарантировать, что любое реальное значение возраста, которое мы сравниваем
# с этой переменной, будет меньше, чем бесконечность.
youngestGirlAge = float('inf')
youngestGirlHeight = float('inf')
highestBoyWeight = 0
highestBoyHeight = 0
currentYear = datetime.now().year
highestBoyWeightIsHeaviest = False
yungestGirlIsSmalliest = False

for student in students:
    if student["sex"] == "male":
        boysCount += 1
        boysAgeSum += currentYear - student["birthYear"]
        if student["height"] > highestBoyHeight:
            highestBoyHeight = student["height"]
            highestBoyWeight = student["weight"]
    elif student["sex"] == "female":
        girlsCount += 1
        girlsAgeSum += currentYear - student["birthYear"]
        if student["height"] < youngestGirlHeight:
            youngestGirlHeight = student["height"]
            youngestGirlAge = currentYear - student["birthYear"]
print(f"{highestBoyHeight} и {highestBoyWeight}")
print(f"{youngestGirlHeight} и {youngestGirlAge}")

#Проверка условий
listStudentsWieght = []
for student in students:
    print(f"{student["weight"]}")
    listStudentsWieght.append(student["weight"])
    #print(f"{max(listWieght)}")
    if highestBoyWeight > max(listStudentsWieght):
        highestBoyWeightIsHeaviest = True
# !!!!! Нашел вариант короче в исплнении, надо спросить преподавателя !!!!!
#highestBoyWeightIsHeaviest = highestBoyWeight > max(student["weight"] for student in students)
listGirlsAge = []
for student in students:
    if student["sex"] == "female":
        print(f"{student["birthYear"]}")
        listGirlsAge.append(currentYear - student["birthYear"])
        if youngestGirlAge <= min(listGirlsAge):
            yungestGirlIsSmalliest = True
print(f"{min(listGirlsAge)}")
# !!!!! Нашел вариант короче в исплнении, надо спросить преподавателя !!!!!
# yungestGirlIsSmalliest = youngestGirlAge == min(currentYear - student["birthYear"] for student in students
#                                                  if student["sex"] == "female")

print(f"Количество мальчиков в классе равно {boysCount}. Количество девочек в классе равно {girlsCount}\n")
print(f"Средний возраст мальчиков в классе равев {boysAgeSum/boysCount: .2f}."
      f" Средний возраст девочек в классе равен {girlsAgeSum/girlsCount: .2f}\n")
print(f"Самый высокий мальчик весит больше всех в классе: {highestBoyWeightIsHeaviest}\n")
print(f"Самая низкая девочка является самой юной среди девочек: {yungestGirlIsSmalliest}\n")

# Задание 3

# Сформировать одномерный список целых чисел A, используя генератор случайных чисел (диапазон от 0 до 99).
# Размер списка n ввести с клавиатуры. В соответствии со своим вариантом написать программу по условию,
# представленному в таблице ниже

# Вариант 11
# Удалить пять первых нечетных по значению элементов списка.
print("======= Задание 3. Вариант 11 =======")
rangeList3 = int(input("Введите размерность списка:\n"))
list3 = [random.randint(0, 99) for i in range(rangeList3)]
count = 0
print(f"Исходный список такой {list3}\n")
for i in range(len(list3)):
    try:
        if i % 2 != 0:
            list3.remove(list3[i])
            count += 1
        if count == 5:
            break
    except:
        print(f"В списке не достаточно нечетных элементов для удаления\n")
        continue
print(f"Модифицированный список после удаления элементов такой {list3}\n")