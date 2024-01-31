# Объявите функцию, которая принимает список, находит максимальное, минимальное и сумму значений
# этого списка и выводит результат в виде строки:
# "Min = v_min, max = v_max, sum = v_sum"
# После объявления функции прочитайте (с помощью функции input) список целых чисел,
# записанных в одну строку через пробел, и вызовите функцию с этим списком.
def find_min_max_sum(list_num):  # 8 11 5 -10 12 0
    v_min = min(list_num)
    v_max = max(list_num)
    v_sum = sum(list_num)
    print(f"Min = {v_min}, max = {v_max}, sum = {v_sum}")

list_num = list(map(int, input().split()))
find_min_max_sum(list_num)