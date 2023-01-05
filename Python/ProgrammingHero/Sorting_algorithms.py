# generate random list, swap function
from random import randint


def r_l(x=12):
    a = [randint(0, 100) for i in range(x)]
    return a


def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

# bubble sort


def bubble_sort(x):
    """
    Тут просто реализирует формула: сравниваем элемент со стоящим с права от него,
    если элемент больше меняем их местами, кроме последнего элемента len(x-1).
    Эту процедуру проводим (len(массива)) раз.
    """
    for i in range(len(x)):
        for i in range(len(x) - 1):
            if x[i] > x[i+1]:
                swap(x, i, i+1)
    return x


bbl = bubble_sort(r_l())

print("bubble sort -", bbl, bbl == sorted(bbl))

# selection sort


def selection_sort(x):
    """
    Суть метода: итерацией находим индекс минимального элемента, меняем его местами с
    элементом на индексе 0, находим индекс следующего минимального элемент, но ищем уже
    с первого элемента, меняем его местами с элементом на 1 индексе и тд. Мы с каждой
    петлей отсекаем левую, уже отсортированною часть массива.
    """
    for i in range(len(x)-1):
        # Понятно, что если предпоследний элемент стоит на месте, последний элемент самый большой в массиве
        min_idx = i
        # Объявляем, что минимальный элемент это нулевой
        for j in range(i+1, len(x)):
            # Это итерация нужна, для поиска минимального индекса
            # i+1 остекаем уже пройдённую, левую часть
            if x[j] < x[min_idx]:
                min_idx = j
        if min_idx != i:
            # Если мы нашли индекс меньше, меняем элементы местами
            swap(x, i, min_idx)
    return x


select = selection_sort(r_l())

print('selection sort -', select, select == sorted(select))

# insertion sort


def insertion_sort(x):
    for i in range(1, len(x)):
        j = i
        while x[j] < x[i-1] and i > 0:
            i -= 1
        if j != i:
            x.insert(i, x.pop(j))
    return x


insert = insertion_sort(r_l())

print("insertion sort -", insert, insert == sorted(insert))

# merge sort


def merge_two_sorted_list(x, y):
    '''
    Нужный алгоритм для сортировки слиянием
    '''
    z = []
    i = j = 0
    while i < len(x) or j < len(y):
        if j == len(y) or (i < len(x) and x[i] <= y[j]):
            z.append(x[i])
            i += 1
        else:
            z.append(y[j])
            j += 1
    return z
# Проверка корректной работы алгоритма
# a = sorted(r_l(randint(1, 7)))
# b = sorted(r_l(randint(1, 7)))
# ab = merge_two_sorted_list(a, b)
# print(a, b, len(a+b))
# print(ab, sorted(ab) == ab, len(ab))


def merge_sort(x):
    if len(x) == 1:
        return x
    mid = len(x)//2
    left = merge_sort(x[:mid])
    right = merge_sort(x[mid:])
    return merge_two_sorted_list(left, right)


merge = merge_sort(r_l())

print("merge sort -", merge, sorted(merge) == merge)

# quick sort


def quick_sort(x):
    if len(x) <= 1:
        return x
    element = x[0]
    # left = list(filter(lambda l: l < elem, x))
    left = [i for i in x if i < element]
    center = [i for i in x if i == element]
    right = [i for i in x if i > element]
    return quick_sort(left) + center + quick_sort(right)


quick = (quick_sort(r_l()))


print('quick sort -', quick, quick == sorted(quick))
