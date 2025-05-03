#Создайте итерируемый объект, возвращающий генератор тридцати пяти чисел трибоначчи и выведите эти числа.
class Tribonacci:
    def __init__(self, count=35):
        self.count = count

    def __iter__(self):
        return self._tribonacci_generator()

    def _tribonacci_generator(self):
        a, b, c = 0, 1, 1
        for _ in range(self.count):
            yield a
            a, b, c = b, c, a + b + c

# Создание итерируемого объекта
tribonacci_sequence = Tribonacci()

# Вывод первых 35 чисел Трибоначчи
for number in tribonacci_sequence:
    print(number)