#	1. Используя функцию map() переписать функцию
from numpy import number

# squared = []
# for i in items:
#     squared.append(i**2)

def square_item(item):
    return item ** 2
items = [1, 2, 3, 4, 5]
squared = list(map(square_item, items))
print(squared)

# 2. Используйте функцию reduce() и перепишите код
# product = 1
# list = [1, 2, 3, 4]
# for num in list:
#     product = product * num

from functools import reduce
list2 = [1, 2, 3, 4]
product = 1
multiply = reduce(lambda product, y: product * y, list2)
print(multiply)

# 3. Используйте функцию map() и перепишите код
# numbers = [1, 2, 3, 4, 5]
# squared = []
# for num in numbers:
#        squared.append(num ** 2)
# print(squared)

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

# 4. Объедините списки x = [1, 2, 3] и y = [4, 5, 6] с помощью функции zip()

x = [1, 2, 3]
y = [4, 5, 6]

result = list(zip(x, y))
print(result)

# 5.Используйте функцию zip() чтобы преобразовать код:
#
name_hero = [
    'Hulk',
    'Mr. Fantastic',
    'Invisible Woman',
    'Doctor Strange',
    'Doctor Octopus',
    'Spider-Man',
]
#
name_real = [
    'Bruce Banner',
    'Reed Richards',
    'Sue Storm',
    'Stephen Strange',
    'Otto Octavius',
    'Peter Parker',
]
#
# for i in range(len(name_hero)):
#     print(name_hero[i], '-', name_real[i])

result2 = list(map(": ".join, zip(name_hero, name_real)))
print(result2)

#6.	С помощью функции filter() переместите из списка numbers = [1, 2, 4, 5, 7, 8, 10, 11] нечетные элементы
# в новый список.

numbers = [1, 2, 4, 5, 7, 8, 10, 11]
result3 = list(filter(lambda x: x % 2 != 0, numbers))
print(result3)