# Задача на рекурсию
#
# Реализуйте рекурсивную функцию нарезания прямоугольника с заданными пользователем сторонами a и b на квадраты
# с наибольшей возможной на каждом этапе стороной. Выведите длины ребер получаемых квадратов и кол-во полученных
# квадратов.

# 1. На каждом этапе мы определяем сторону квадрата, равную меньшей из двух сторон прямоугольника.
# 2. Затем мы вычисляем, сколько таких квадратов можно вырезать из прямоугольника.
# 3. После этого мы уменьшаем одну из сторон прямоугольника и рекурсивно вызываем функцию для оставшейся части.

def factorial(n):
    if n == 0:  # Базовый случай
        return 1
    else:
        return n * factorial(n - 1)  # Рекурсивный вызов

# Пример использования
print(factorial(5))  # Вывод: 120


def cut_rectangle(a, b, squares = []):

    # Если одна из сторон становится нулевой, завершаем рекурсию
    if a == 0 or b == 0:
        return squares

    # Определяем сторону квадрата
    square_side = min(a, b) # вводим сторы прямоугольника. Например 5 и 3. мин. 3

    # Количество квадратов, которые можно вырезать
    count = max(a, b) // square_side # количество квадратов 5 // 3 = 1

    if count == 2:
        squares.extend([square_side] * count)
        #squares.append(1)
        #squares.append(1)
    else:
        #squares.append(square_side)
    # Добавляем длину стороны квадрата в список
        squares.extend([square_side] * count) # добавляем 3 в список

    # Рекурсивно вызываем функцию для оставшейся части

    if a > b:
        return cut_rectangle(a - count * square_side, b, squares)
    else:
        return cut_rectangle(a, b - count * square_side, squares)


# Пример использования
a = int(input("Введите длину стороны a: "))
b = int(input("Введите длину стороны b: "))

squares = cut_rectangle(a, b)
print("Длины сторон полученных квадратов:", squares)
print("Количество полученных квадратов:", len(squares))
