# Функция, рекурсия, алгоритмы

# Функция считающая от 1 до n
def sum_numbers(n, y = "Hello"):
    print(y)
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa

print(sum_numbers(5))

# Функция принимающая неограниченное количество аргументов
def sum_str(*args):
    res = ''
    for i in args:
        res += i
    return res

print(sum_str('q', 'e', 'l'))

# Модульность
# Импортируем функцию из другого файла (modul1.py)
import modul1
print(modul1.max1(5, 9))
# вариант 2
from modul1 import max1
print(max1(10, 9))
# импорт всех функций из другого файла
from modul1 import *
print(max1(10, 265))
# импорт функции из другого файла с упрощённым названием
import modul1 as m1
print(m1.max1(16, 9))

# Рекурсия
# На примере последовательности Фибоначчи
def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)

list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1)

# Алгоритмы
# Быстрая сортировка
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([14, 5, 9, 6, 3, 58, 7, 5, 2, 7]))

# Сортировка слиянием
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
        
list1 = [1, 5, 6, 9, 8, 7, 2, 1, 55, 2, 4]
merge_sort(list1)
print(list1)