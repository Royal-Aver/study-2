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
# class Restaurant():
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print(self.restaurant_name, self.cuisine_type)
#
#     def open_restaurant(self):
#         print(f'Restaurant is {self.cuisine_type}')
#
#     def set_number_served(self):
#         print(self.number_served)
#
#     def update_number_served(self, amount):
#         self.number_served = amount
#
#
# restaurant = Restaurant('Pizza', 'closed')
# restaurant.update_number_served(23)
# restaurant.set_number_served()
#
# class User():
#     def __init__(self, first_name, last_name, password, country):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.password = password
#         self.country = country
#
#
#     def describe_user(self):
#         print(f'Its {self.first_name} {self.last_name}, where live in {self.country}. Password we not say!!!')
#
#
#     def greet_user(self):
#         print(f'Hello {self.first_name}!')
#
#
# arina = User('Arina', 'Stakchieva', 123456, 'USA')
# jura = User('Jura', 'Aver', 1234567, 'Russia')


# На вход программы поступает список целых чисел, записанных в одну строчку через пробел.
# Необходимо выбрать из них четыре наибольших уникальных значения.
# Результат вывести на экран в порядке их убывания в одну строчку через пробел.
# num_in = list(map(int, input().split()))  # 10 5 4 -3 2 0 5 10 3
# res = sorted(list(set(num_in)), reverse=True)
# print(res[:4])


# На вход программы поступает список товаров:
# Необходимо преобразовать этот список в словарь, ключами которого выступают цены (целые числа),
# а значениями - соответствующие названия товаров. Необходимо написать функцию,
# которая бы принимала на входе словарь и возвращала список из наименований трех наиболее дешевых товаров.
# Вызовите эту функцию и отобразите на экране полученный список в порядке возрастания цены в одну строчку через пробел.
# def convert_to_dict(lst):
#     products_dict = {}
#     for item in lst:
#         name, price = item.split(':')
#         products_dict[int(price)] = name
#     return products_dict
#
# def find_cheapest_goods(products_dict):
#     sorted_products = sorted(products_dict.items())
#     cheapest_goods = [product for price, product in sorted_products[:3]]
#     return cheapest_goods
#
#
# lst_in = ['смартфон:120000', 'яблоко:2', 'сумка:560', 'брюки:2500', 'линейка:10', 'бумага:500']
#
# products = convert_to_dict(lst_in)
#
# print(*find_cheapest_goods(products))


# На вход программе подается строка текста из натуральных чисел. Из неё формируется список чисел.
# Напишите программу подсчета количества чисел, которые больше предшествующего им в этом списке числа.

# def count_num_greater_than_preceding_num(num_list: list) -> int:  # 5 4 3 2 1
#     count = 0
#     for i, el in enumerate(num_list):
#         if i == 0:
#             continue
#         elif el > num_list[i - 1]:
#             count += 1
#     return count
#
# num_in = list(map(int, input().split()))
#
# print(count_num_greater_than_preceding_num(num_in))


# вход программе подается число n. Напишите программу, которая создает и выводит построчно список, состоящий из
# n списков [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].
# n = int(input())
#
# elem = [i for i in range(1, n + 1)]
# for _ in range(n):
#     print(elem)


# алгоритм сортировки пузырьком - bubble sort - Сложность алгоритма O(n**2):
# arr = [64, 34, 25, 12, 22, 11, 90]
#
# n = len(arr)
#
# for i in range(n):
#     flag = False
#     for j in range(n - i - 1):
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
#             flag = True
#     if not flag:
#         break
#
# print(arr)


# Напишите программу, выводящую следующий список: ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
# lst_in = 'abcdefghijklmnopqrstuvwxyz'
# lst = []
#
# for i, el in enumerate(lst_in):
#     lst.append(el * (i + 1))
#
# print(lst)

# На вход программе подается натуральное число n и n строк, а затем число k. Напишите программу, которая выводит
#  k-ую букву из введенных строк на одной строке без пробелов.
# num_in = input().split() # abcdef bcdefg cdefgh defghi efghij
#
# k = int(input())
# res_str = ''
#
# for _ in num_in:
#     if k > len(_):
#         continue
#     else:
#         res_str += _[k - 1]
#
# print(res_str)


# Уравнение параболы имеет вид y = ax ** 2 + bx +c. Напишите программу, которая по введенным значениям
# a,b,c определяет и выводит вершину параболы.
# def calculate_vert_parabola(a: int,
#                             b: int,
#                             c: int) -> tuple:
#     x = -(b / (2 * a))
#     y = ((4 * a * c) - (b ** 2)) / (4 * a)
#     return x, y
#
# a, b, c = map(int, input().split())
# print(calculate_vert_parabola(a, b, c))


# Дополните приведенный код, чтобы он вывел имена всех пользователей (в алфавитном порядке),
# чей номер оканчивается на 8.
# Примечание. Имена необходимо вывести на одной строке, разделяя символом пробела.
# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

# lst = []
#
# for i in users:
#     num = i['phone']
#     if num[-1] == '8':
#         lst.append(i['name'])
# print(*sorted(lst))


# Дополните приведенный код так,
# чтобы он вывел сумму минимального и максимального элементов множества numbers.
# numbers = {1.414, 12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324, 2.718, 1.324}
#
# max_num = max(numbers)
# min_num = min(numbers)
# print(sum((max_num, min_num)))


# Напишите программу для вывода общего количества уникальных символов
# во всех считанных словах без учета регистра.
# num_in = int(input())
# res = set()
# for i in range(num_in):
#     str_in = set(input().lower())
#     res = res.union(str_in)
# print(len(res))


# Дополните приведенный код так, чтобы он объединил содержимое двух словарей dict1 и dict2:
# если ключ есть в обоих словарях, добавьте его в результирующий словарь со значением,
# равным сумме соответствующих значений из первого и второго словаря;
# если ключ есть только в одном из словарей, добавьте его в результирующий словарь с его текущим значением.
# Результирующий словарь необходимо присвоить переменной result.
# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
#
# result = dict2.copy()
# for i in dict1:
#     if i in result:
#         result[i] += dict1[i]
#     else:
#         result[i] = dict1[i]
# print(result)


# Дополните приведенный код, чтобы он вывел наиболее часто встречающееся слово строки s.
# Если таких слов несколько, должно быть выведено то, что меньше в лексикографическом порядке.
# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
# s = s.split()
# d = {}
# for i in s:
#     d[i] = d.get(i, 0) + 1
#
# n_l = []
# max_v = max(d.values())
# for k, v in d.items():
#     if v == max_v:
#         n_l.append(k)
# print(sorted(n_l)[0])


# Вам доступен список pets, содержащий информацию о собаках и их владельцах.
# Каждый элемент списка – это кортеж вида (кличка собаки, имя владельца, фамилия владельца, возраст владельца).
#
# Дополните приведенный код так, чтобы в переменной result хранился словарь,
# в котором для каждого владельца будут перечислены его собаки.
# Ключом словаря должен быть кортеж (имя, фамилия, возраст владельца),
# а значением – список кличек собак (сохранив исходный порядок следования).

# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
#
# result = {}
#
# for pet in pets:
#     owner_key = (pet[1], pet[2], pet[3])
#     if owner_key not in result:
#         result[owner_key] = [pet[0]]
#     else:
#         result[owner_key].append(pet[0])
#
# print(result)

# Напишите программу, которая с помощью модуля random моделирует броски монеты.
# Программа принимает на вход количество попыток и выводит результаты бросков:
# Орел или Решка (каждое на отдельной строке).
# import random
#
# n = int(input())
# for _ in range(n):
#     print('Орел') if random.randint(0, 1) else print('Решка')


# Напишите программу, которая с помощью модуля random генерирует случайный пароль.
# Программа принимает на вход длину пароля и выводит случайный пароль,
# содержащий только символы английского алфавита a..z, A..Z (в нижнем и верхнем регистре).
# import random as r
#
# length = int(input())
# passw = ''
# for _ in range(length):
#     char = r.choice([r.randint(65, 90), r.randint(97, 122)])
#     passw += chr(char)
#
# print(passw)


# Decimal числа, разделенные символом пробела, хранятся в строковой переменной s.
# Дополните приведенный код, чтобы он вывел на первой строке сумму всех чисел, а на второй строке
# 5 самых больших чисел в порядке убывания, разделенных символом пробела.
# import decimal
# s = '0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.23 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50'
#
# nums_lst = [decimal.Decimal(x) for x in s.split()]
# sum_nums = sum(nums_lst)
# biggest_5_nums = sorted(nums_lst, reverse=True)[:5]
#
# print(sum_nums)
# print(*biggest_5_nums)


# def greet(name, *args):
#     name = name.split()
#     name.extend(list(args))
#     s = ' and '.join(name)
#     return f'Hello, {s}!'
#
#
# res = greet('Timur', 'Roman')
# print(res)


# Напишите функцию print_products(), которая принимает произвольное количество аргументов и выводит
# список продуктов (любая непустая строка) по образцу: <номер продукта>) <название продукта>
# (нумерация продуктов начинается с единицы). Если среди переданных аргументов нет ни одного продукта,
# необходимо вывести текст Нет продуктов.
# def print_products(*args):
#     lst = [prod for prod in args if type(prod) == str and len(prod) > 0]
#     if len(lst) == 0:
#         print('Нет продуктов')
#     for i, prod in enumerate(lst):
#         print(f'{i + 1}) {prod}')
#
#
# res = print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)


# Длина большой полуоси пруда будет 2.5 метра, а малой полуоси — 1.75 метра.
# Запланированная глубина — 0.35 метра.
# Для оценки стоимости работ необходимо вычислить площадь и объём пруда.

# Из модуля decimal импортируйте тип данных Decimal и параметр getcontext.
# Из модуля math импортируйте константу "пи".
# from decimal import Decimal, getcontext
# from math import pi
# # Приведите константу "пи" к типу Decimal.
# # Помните, что Decimal() принимает строку, а константа "пи" - это число.
# pi = Decimal(str(pi))
# # Установите необходимую точность для вычислений.
# getcontext().prec = 10
#
# # Объявите функцию ellipse_area() с двумя параметрами.
# def ellipse_area(ellipse_minor_axis_length, ellipse_axis_length):
#     return ellipse_minor_axis_length * ellipse_axis_length * pi
#
# # Объявите три переменные типа Decimal -
# # они должны хранить длины полуосей эллипса и глубину пруда.
# ellipse_minor_axis_length = Decimal('1.75')
# ellipse_axis_length = Decimal('2.5')
# depth = Decimal('0.35')
#
# # Вызовите функцию ellipse_area(), в аргументах передайте длины полуосей эллипса.
# area = ellipse_area(ellipse_minor_axis_length, ellipse_axis_length)
#
# # Вычислите объём пруда: площадь * глубина.
# pond_volume = area * depth
# print(f'Площадь эллипса: {area} кв.м.')
# print(f'Объем воды для наполнения пруда: {pond_volume} куб.м.')



# В таинственной деревне кото-самураев, каждое послание несет в себе особое значение.
# Кото-самурай Кэндзи нашел на пути старинный свиток с посланием, в котором заключена важная информация.
# Свиток содержит строку s, состоящую из английских букв в нижнем регистре.
# Чтобы раскрыть секрет, Кэндзи должен найти в строке последний неповторяющийся символ.
# Ваша задача — помочь Кэндзи определить последний уникальный символ в строке s.
# Если такого символа нет, нужно вернуть число -1.
# Формат ввода
# Одна строка, содержащая s — строку, состоящую из строчных английских букв.
# Длина строки не превышает 10^5 символов.
# Формат вывода
# Выведите последний неповторяющийся символ в строке. Если такого символа нет, верните -1.
# def last_unique_char(s):
#     char_count = {}
#
#     # создаю dict, в котором ключи - символы, а значения - количество ключей в строке
#     for char in s:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
#
#     # пробегаюсь по исходной строке с конца и возвращаю первый элемент == 1
#     for char in reversed(s):
#         if char_count[char] == 1:
#             return char
#
#     return -1
#
#
# # Пример использования
# s = "abacabad"
# result = last_unique_char(s)
# print(result)  # Выведет: 'd'


# В деревне цифровых самураев-котов, каждый воин имеет свой уникальный адрес электронной почты
# для получения важных сообщений и заданий.
#
# Каждый валидный адрес электронной почты состоит из локального имени и имени домена, разделенных знаком «@».
# Помимо строчных букв, электронное письмо может содержать один или несколько символов «.». или «+». Например,
# в «samurai@ninja.com» «samurai» — это локальное имя, а «ninja.com» — это имя домена.
#
# Если вы добавите точки '.' в локальном имени адреса, при отправке эта точка будет проигнорирована.
# Это правило не распространяется на доменные имена. Например,
# «samurai.cat@ninja.com» и «samuraicat@ninja.com» пересылают на один и тот же адрес электронной почты.
#
# Если вы добавите «+» в локальное имя, все, что находится после первого знака «+», будет игнорироваться,
# что позволяет фильтровать определенные электронные письма. Это правило не распространяется на
# доменные имена. Например, «samurai+mouse@ninja.com» будет перенаправлено на «samurai@ninja.com».
# def normalize_email(email):
#     # Шаблон адреса на который будет отправляться почта
#     local_name, domain_name = email.split('@')
#     local_name = local_name.split('+')[0]
#     local_name = local_name.replace('.', '')
#     return local_name + '@' + domain_name
#
# def count_unique_emails(emails):
#     unique_emails = set()
#     for email in emails:
#         normalized_email = normalize_email(email)
#         unique_emails.add(normalized_email)
#     return len(unique_emails)
#
# # Пример использования
# n = int(input("Введите количество адресов электронной почты: "))
# emails = []
# for _ in range(n):
#     email = input()
#     emails.append(email)
#
# print(count_unique_emails(emails))

# samurai.cat@ninja.com
# samu.rai.cat@ninja.com
# samurai.cat+warrior@ninja.com


# Дан список numbers, содержащий кортежи чисел. Напишите программу, которая сортирует
# и выводит список numbers в соответствии с суммой минимального и максимального элемента кортежа.
# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100),
#            (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
#
# def comparator(item):
#     return max(item) + min(item)
#
#
# numbers.sort(key=comparator)
# print(numbers)


# При регистрации на портале каждый эмо бой обязан придумать себе никнейм.
# Никнейм должен быть не короче восьми символов, содержать в себе хотя бы одну цифру,
# и хотя бы по одной заглавной и прописной английской букве.

# Вводится никнейм — последовательность букв и цифр без пробелов. Длина строки не превосходит 100 символов.

# Выведите «YES», если ник подходит для эмо боя, и «NO» — в противном случае.


# def check_nickname(nickname: str) -> str:
#     if len(nickname) < 8:
#         return 'NO'
#
#     check_num = False
#     check_upper_letter = False
#     check_lower_letter = False
#
#     for char in nickname:
#         if char.isdigit():
#             check_num = True
#         elif char.islower():
#             check_upper_letter = True
#         elif char.isupper():
#             check_lower_letter = True
#
#     return 'YES' if check_num and check_upper_letter and check_lower_letter else 'NO'
#
# nickname_in = input('Enter your username: ')
# print(check_nickname(nickname_in))


# Напишите программу для определения, является ли число произведением двух чисел из данного набора.
# Программа должна выводить результат в виде ответа «ДА» или «НЕТ».
# num_nums = int(input())
#
# lst_nums = []
# for _ in range(num_nums):
#     lst_nums.append(int(input()))
#
# mult = int(input())
# res = 'НЕТ'
#
# for i in range(len(lst_nums) - 1):
#     for j in range(i + 1, len(lst_nums)):
#         if lst_nums[i] * [j] == mult:
#             res = 'ДА'
#             break
#
# print(res)


# Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" соответствует
# выпадению Орла, а буква "Р" - выпадению Решки.
# Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
# def max_consecutive_chars(string):
#     max_count = 1
#     current_count = 1
#
#     if 'Р' not in string:
#         return 0
#
#     for i in range(1, len(string)):
#         if string[i] == 'Р' and string[i-1] == 'Р':
#             current_count += 1
#             max_count = max(max_count, current_count)
#         else:
#             current_count = 1
#
#     return max_count
#
#
# str_in = input()
# print(max_consecutive_chars(str_in))


# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников.
# Теперь он использует их в качестве серверов "Пегого дудочника".
# Помогите владельцу фирмы отыскать все зараженные холодильники.
# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр,
# и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы,
# главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника,
# нумерация начинается с единицы.

# В первой строке подаётся число n – количество холодильников. В последующих n строках вводятся строки,
# содержащие латинские строчные буквы и цифры, в каждой строке от 5 до 100 символов.

# Программа должна вывести номера зараженных холодильников через пробел.
# Если таких холодильников нет, ничего выводить не нужно.
# def check_str(text:str, pattern:str):
#     for char in pattern:
#         if text.find(char) != -1:
#             text = text[text.find(char):]
#         else:
#             return False
#     return True
#
#
# res_lst = []
# n = int(input())
# lst_patt = 'anton'
#
# for i in range(1, n + 1):
#     res = check_str(input(), lst_patt)
#     if res:
#         res_lst.append(i)
#
# print(*res_lst)


# На вход программе подается строка текста. Напишите программу, которая выводит на экран символ,
# который появляется наиболее часто.
#
# На вход программе подается строка текста. Текст может содержать строчные и заглавные буквы английского
# и русского алфавита, а также цифры.
#
# Примечание 1. Если таких символов несколько, следует вывести последний по порядку символ.
#
# Примечание 2. Следует различать заглавные и строчные буквы, а также буквы русского и английского алфавита.
# str_in = 'jfnmdbsdfnsjfqenfdssjdfhsdjlkppppppppppppppppppgggggxxzzzssswwwwwwwwwwwwwwwwwwfgdfxdfg'
#
# dct = {}
# for i in str_in[::-1]:
#     if i not in dct:
#         dct[i] = 1
#     else:
#         dct[i] += 1
#
# most_char = max(dct, key=dct.get)
# print(most_char)


# some_map = list(map(int, '527 9486'.split()))
# x = some_map[0]
# y = some_map[1]
# counter = 0
# for i in range(x,y+1):
#     if (x%i == 0 and y%i == 0) and (i%x == 0 and i%y == 0):
#         counter+=1
#
# print(counter)


s = 1234.5678

def get_nums(s, before, after):
    left, right = str(s).split('.')
    left = left[-before:]
    right = right[:after]
    return float(left + '.' + right)


print(get_nums(s, 2, 3))