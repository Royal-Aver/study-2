# Объявите функцию, которая принимает список, находит максимальное, минимальное и сумму значений
# этого списка и выводит результат в виде строки:
# "Min = v_min, max = v_max, sum = v_sum"
# После объявления функции прочитайте (с помощью функции input) список целых чисел,
# записанных в одну строку через пробел, и вызовите функцию с этим списком.
# def find_min_max_sum(list_num):  # 8 11 5 -10 12 0
#     v_min = min(list_num)
#     v_max = max(list_num)
#     v_sum = sum(list_num)
#     print(f"Min = {v_min}, max = {v_max}, sum = {v_sum}")
#
# list_num = list(map(int, input().split()))
# find_min_max_sum(list_num)
import shlex
# Объявите функцию для проверки числа на нечетность (возвращается True,
# если переданное число нечетное и False, если число четное).
# После объявления функции прочитайте (с помощью функции input) список целых значений,
# записанных в одну строку через пробел. И, используя генератор списков и созданную функцию,
# сформируйте список из нечетных значений на основе введенного исходного списка.
# def is_odd(num):
#     return True if num % 2 != 0 else False
#
# lst_num_in = list(map(int, input().split()))
# lst = [num for num in lst_num_in if is_odd(num)]
# print(*lst)

# Объявите функцию, которая принимает строку (в качестве аргумента) и возвращает два значения
# в виде кортежа: переданная строка и ее длина.
# После объявления функции прочитайте (с помощью функции input) список названий городов,
# записанных в одну строку через пробел.
# Затем, используя генератор словарей и созданную функцию, сформируйте словарь d
# def len_str(str):
#     return len(str)
#
#
# city_in = input().split()  #  Воронеж Лондон Тверь Омск Уфа
# d = {x: len_str(x) for x in city_in}
# print(d)

import time
# Быстрый алгоритм Евклида (нахождение наибольшего общего числителя)
# def get_nod(a, b):
#     if a < b:
#         a, b = b, a
#     while b != 0:
#         a, b = b, a % b
#     return a

# print(get_nod(18, 24))


# Объявите функцию с именем get_even, которая принимает произвольное количество чисел
# в качестве аргументов и возвращает список, составленный только из четных переданных значений.
# def get_even(*args):
#     lst = [x for x in args if x % 2 == 0]
#     return lst
#
#
# num_in = list(map(int, input().split()))
# print(*get_even(*num_in))


# Имеется словарь. Дополнительно вводятся еще пункты меню в виде строк.
# Необходимо эту введенную информацию преобразовать в словарь и добавить к словарю menu,
# используя оператор распаковки для словарей. На результирующий словарь должна вести переменная menu.
# menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
# lst_in = ['Города=about-cities', 'Машины=read-of-cars', 'Самолеты=airplanes']
# d = dict([x.split('=') for x in lst_in])
# d_n = {**menu, **d}
# print(d_n)


# В программе задана функция filter_lst, которая отбирает элементы,
# переданного ей итерируемого объекта и возвращает сформированный кортеж значений.
# На вход программы поступает список целых чисел, записанных в одну строчку через пробел.
# Вызовите функцию filter_lst для формирования:
# - кортежа из всех значений входного списка (передается в параметр it);
# - кортежа только из отрицательных чисел;
# - кортежа только из неотрицательных чисел (то есть, включая и 0);
# - кортежа из чисел в диапазоне [3; 5]
# lst - список на возвращенный функцией filter_lst.
# Для отбора нужных значений формальному параметру key следует передавать
# соответствующие определения анонимной функции.
# it = list(map(int, input().split()))  # 5 4 -3 4 5 -24 -6 9 0
#
# def filter_lst(it, key=None):
#     if key == None:
#         return tuple(it)
#     res = ()
#     for x in it:
#         if key(x):
#             res += (x, )
#     return res
#
#
# f1 = None
# f2 = lambda x: x < 0
# f3 = lambda x: x >= 0
# f4 = lambda x: x > 3 and x < 6
#
# for f in [f1, f2, f3, f4]:
#     lst = filter_lst(it, key=f)
#     print(*lst)


# Используя замыкания функций, объявите внутреннюю функцию,
# которая увеличивает значение своего аргумента на некоторую величину n - параметр внешней функции
# с сигнатурой:
# Вызовите внешнюю функцию counter_add со значением аргумента 2 и результат присвойте переменной cnt.
# Вызовите внутреннюю функцию через переменную cnt со значением k, введенным с клавиатуры:
# def counter_add(n):
#     def inner_counter(k):
#         nonlocal n
#         n += k
#         return n
#
#     return inner_counter


# k = int(input())
# cnt = counter_add(2)
# print(cnt(k))

# Используя замыкания функций, объявите внутреннюю функцию, которая преобразует строку из
# списка целых чисел, записанных через пробел, либо в список, либо в кортеж.
# Тип коллекции определяется параметром tp внешней функции.
# Если tp = 'list', то используется список, иначе (при другом значении) - кортеж.
# Далее, на вход программы поступают две строки: первая - это значение для параметра tp;
# вторая - список целых чисел, записанных через пробел.
# С помощью реализованного замыкания преобразовать эти данные в соответствующую коллекцию.
# Результат вывести на экран командой (lst - ссылка на коллекцию):
# def type_data(tp):
#     def convert_str_to_list_or_tuple(list_in):
#         if tp == 'list':
#             list_in = list(list_in)
#
#         return list_in
#     return convert_str_to_list_or_tuple
#
#
# tp_in = (input())
# list_num_in = tuple(map(int, input().split()))
#
# res = type_data(tp_in)
# print(res(list_num_in))


# def decorator_func_show(func):
#     def wrapper(width, height):
#         print(f"Площадь прямоугольника: {func(width, height)}")
#
#     return wrapper
#
# def get_sq(width, height):
#     res = width * height
#     return res
#
# get_sq = decorator_func_show(get_sq)
# get_sq(2, 4)

# На вход программы поступают два целых числа a и b (a < b), записанные в одну строчку через пробел.
# Определите генератор, который бы выдавал модули целых чисел из диапазона [a; b].
# В цикле выведите первые пять значений этого генератора.
# Каждое значение с новой строки. (Гарантируется, что пять значений имеются).
# a, b = map(int, input().split())
# gen = list(abs(x) for x in range(a, b))
# print(*gen[:5], sep='\n')



# Используя символы малых букв латинского алфавита (строка ascii_lowercase)
# запишите генератор, который бы возвращал все сочетания из двух букв латинского алфавита.
# Выведите первые 50 сочетаний на экран в строку через пробел.
# from string import ascii_lowercase
# lst = []
# for i in ascii_lowercase:
#     for j in ascii_lowercase:
#         if len(lst) < 50:
#             a = i + j
#             lst.append(a)
# print(*lst)


# n = int(input())
# count = 0
# for i in range(n):
#     n = input()
#     if n.count('11') >= 3:
#         count += 1
# print(count)


#  вход программе подается строка текста. Если в этой строке буква «f» встречается только один раз,
#  выведите её индекс. Если она встречается два и более раза, выведите индексы её первого и
#  последнего вхождения на одной строке, разделенные символом пробела.
#  Если буква «f» в данной строке не встречается, следует вывести «NO».
# s = input()
# if s.count('f') == 1:
#     print(s.index('f'))
# elif s.count('f') > 1:
#     print(s.find('f'), s.rfind('f'))
# else:
#     print('NO')


# На вход программе подается строка текста, в которой буква «h» встречается минимум два раза.
# Напишите программу, которая удаляет из этой
# строки первое и последнее вхождение буквы «h», а также все символы, находящиеся между ними.
# s = input()
# if s == 'hh':
#     s = ''
# else:
#     start_h = s.find('h')
#     end_h = s.rfind('h')
#     s = s[:start_h ] + s[end_h + 1:]
# print(s)


# Напишите функцию, принимающую в качестве аргумента натуральное число и возвращающую
# список всех делителей данного числа.
# def get_factors(num):
#     lst = [x for x in range(1, num + 1) if num % x == 0]
#     return len(lst)
#
# n = int(input())
# print(get_factors(n))


# Напишите программу, которая выводит индекс второго вхождения буквы «f».
# Если буква «f» встречается только один раз, выведите число −1,
# а если не встречается ни разу, выведите число −2.
# s = 'fffffffffffffff'
# first_f_index = s.find('f')
# if first_f_index == -1:
#     print(-2)
# else:
#     second_f_index = s.find('f', first_f_index + 1)
#     if second_f_index == -1:
#         print(-1)
#     else:
#         print(second_f_index)


# def two_lst_to_dict(*args, **kwargs):
#     def wrapper(*args, **kwargs):
#         lst1, lst2 = str_to_lst(str1, str2)
#         return dict(zip(lst1, lst2))
#
#     return wrapper
#
# @two_lst_to_dict
# def str_to_lst(str1, str2):
#     return str1.split(), str2.split()
#
# str1 = input()
# str2 = input()
#
# lst = str_to_lst(str1, str2)  # house river tree car
# # lst2 = str_to_lst(str2)           # дом река дерево машина
# print(lst)


# Вводятся названия городов в одну строчку через пробел. Необходимо определить функцию filter,
# которая бы возвращала только названия длиной более 5 символов.
# Извлеките первые три полученных значения с помощью функции next и
# отобразите их на экране в одну строчку через пробел. (Полагается, что минимум три значения имеются).


# Вводится строка. Необходимо в ней заменить кириллические символы на соответствующие
# латинские обозначения (без учета регистра букв), а все остальные символы - на символ дефиса (-).
# Для этого в программе определен словарь. фрагменты в строке должны идти друг за другом без пробелов.
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya', ' ': '-'}
#
# lst_in = input().lower()
#
# l = ''.join([t[_] for _ in lst_in if _ in t])
#
# print(l)


# Вводится список предметов в виде списка:
# С помощью функции map, необходимо сначала преобразовать этот список строк в список списков:
# (('название_1', 'вес_1'), ..., ('название_N', 'вес_N'))
# А, затем, отфильтровать (исключить) все предметы с весом менее 500, используя функцию filter.
# Вывести на экран список оставшихся предметов (только их названия) в одну строчку через пробел.
# lst_in = ['зонт=1000', 'палатка=10000', 'спички=22', 'котелок=543']
#
# t = list(map(lambda x: x.split('='), lst_in))
# f = filter(lambda x: int(x[1]) > 500, t)
# for x in f:
#     print(x[0], end=' ')


# Вводится список целых чисел в одну строчку через пробел.
# Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. Результат отобразить на экране
# в виде последовательности оставшихся чисел в одну строчку через пробел.
# lst_in = list(map(int, input().split()))  # 8 11 0 -23 140 1
#
# res = filter(lambda x: 9 < abs(x) < 100, lst_in)
# print(*res)


#  Вводится список email-адресов в одну строчку через пробел.
#  Среди них нужно оставить только корректно записанные адреса. Будем полагать,
#  что к таким относятся те, что используют латинские буквы, цифры и символ подчеркивания.
#  А также в адресе должен быть символ "@",
#  а после него символ точки "." (между ними, конечно же, могут быть и другие символы).
# Результат отобразить в виде строки email-адресов, записанных через пробел.
# import re
# lst1 = input().split()
# pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
#
# def check_correct_email(email):
#     return re.match(pattern, email)
#
#
# res = filter(check_correct_email, lst1)
# print(*res)


# ООП
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name,
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name, self.cuisine_type)

    def open_restaurant(self):
        print(f'Restaurant is {self.cuisine_type}')


restaurant = Restaurant('Pizza', 'closed')


class User():
    def __init__(self, first_name, last_name, password, country):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.country = country


    def describe_user(self):
        print(f'Its {self.first_name} {self.last_name}, where live in {self.country}. Password we not say!!!')


    def greet_user(self):
        print(f'Hello {self.first_name}!')


arina = User('Arina', 'Stakchieva', 123456, 'USA')
jura = User('Jura', 'Aver', 1234567, 'Russia')

arina.greet_user()
arina.describe_user()

jura.greet_user()
jura.describe_user()