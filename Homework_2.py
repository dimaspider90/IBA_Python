import random
# Задание 1. Задачи на одномерные списки

# Вариант 4
# Найдите произведение элементов списка с нечетными номерами.
# Найдите наибольший элемент списка, затем удалите его и выведите новый список.
print("======= Задание 1. Вариант 4. Задачи на одномерные списки =======")

list = [random.randint(1, 30) for i in range(10)]
oddMultiply = 1;
maxNum = 0
for i in range(len(list)):
    if i % 2 != 0:
        oddMultiply *= list[i]
        print(oddMultiply)
    if list[i] > maxNum:
        maxNum = list[i]
print(f"Исходный список для первого задания такой {list}\n")
print(f"Произведение значений нечетных элементов равно {oddMultiply}\n")
list.remove(maxNum)
print(f"Максимальное значение элемента равно {maxNum}\n")
print(f"Модифицированный список для первого задания теперь такой {list}\n")

# Вариант 2
# Введите одномерный целочисленный список. Найдите наибольший нечетный элемент.
# Найдите минимальный по модулю элемент списка.
print("======= Задание 1. Вариант 2. Задачи на одномерные списки =======\n")
list2 = [random.randint(-10, 10) for i in range(10)]
oddMaxNumber = -10;
minNumber = 10;
for i in range(len(list2)):
    if i % 2 != 0:
        if list2[i] > oddMaxNumber:
            oddMaxNumber = list2[i]
    if abs(list2[i]) < minNumber:
        minNumber = abs(list2[i])
print(f"Исходный список для второго задания такой {list2}\n")
print(f"Наибольший нечетный элемент равен {oddMaxNumber}\n")
print(f"Минимальный по модулю элемент списка равен {minNumber}\n")
print("======= Конец выполнения Задания 1 =======\n")

#Задание 2. Задачи на многомерные списки
print("======= Задание 2. Задачи на многомерные списки =======\n")
#В матрице найти номер строки, сумма чисел в которой максимальна.
rows, cols = 3, 4
randomMatrix = [[random.randint(0, 100) for i in range(cols)] for j in range(rows)]
for i in range(len(randomMatrix)):
    print(randomMatrix[i], end="\n")

# matrix = [[100, 2, 3],
#           [7, 8, 9],
#           [11, 2, 16]]
maxRowSum = 0
maxRowIndex = 0
for i in range(len(randomMatrix)):
    rowSum = sum(randomMatrix[i])
    if rowSum > maxRowSum:
        maxRowSum = rowSum;
        maxRowIndex = i
print(f"\nМаксимальная сумма находится в(о) {maxRowIndex} строке и равна {maxRowSum}")
print("======= Конец выполнения Задания 2 =======")