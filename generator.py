# def fibonacci(n: int):
#     index = 0
#     a, b = 0, 1
#     while index < n:
#         yield a
#         index += 1
#         a, b = b, a + b
#
#
# fibo = fibonacci(25)
# for i in fibo:
#     print(i)

# def fibonacci(n: int):
#     a, b = 0, 1
#     while a < n:
#         yield a
#         a, b = b, a + b
#
#
# fibo = fibonacci(14)
# for i in fibo:
#     print(i)

# def square(n):
#     for i in range(1, n + 1):
#         yield i ** 2
#
#
# a = square(5)
# for i in a:
#     print(i)


# import logging
# from abc import ABCMeta, abstractmethod
# from typing import Generator
#
#
# class Helper(metaclass=ABCMeta):
#     @abstractmethod
#     def help(self) -> None:
#         raise NotImplementedError
#
#
# class HelperBoom(Helper):
#     def help(self) -> None:
#         assert False
#
#
# def _application_logic() -> Generator[Helper, None, int]:
#     helper = HelperBoom()
#     yield helper
#     return 0
#
#
# def do_something1():
#     gen = _application_logic()
#     try:
#         while True:
#             helper = next(gen)
#             helper.help()
#     except StopIteration as e:
#         return e.value
#
#
# def do_something2():
#     gen = _application_logic()
#     try:
#         while True:
#             helper = next(gen)
#             try:
#                 helper.help()
#             except Exception as e:
#                 gen.throw(e)
#     except StopIteration as e:
#         return e.value
#
#
# try:
#     do_something1()
# except Exception:
#     logging.exception('do_something1 failed:')
# try:
#     do_something2()
# except Exception:
#     logging.exception('do_something2 failed:')


