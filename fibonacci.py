"""
BY ISMAILOV SARVARBEK N47 GROUP
"""


# Fibonacci raqamlarini yaratish uchun iterator klassi yaratamiz.
class FibonacciIterator:
    def __init__(self, max_value=None):
        self.a, self.b = 0, 1
        self.max_value = max_value

    def __iter__(self):  # Iterator ob'ektining o'zini qaytaradi.
        return self

    def __next__(self):  # Fibonacci raqamlarini ketma-ketlikda qaytaradi.
        if self.max_value is not None and self.a > self.max_value:
            raise StopIteration
        ret = self.a
        self.a, self.b = self.b, self.a + self.b
        return ret


# Fibonacci raqamlarini chop etish.
fibonacci = FibonacciIterator(100)  # Iteratorni 100 gacha bo'lgan qiymatda olish. Qiymat ixtiyoriy kiritilishi mumkin.
for num in fibonacci:
    print(num)
