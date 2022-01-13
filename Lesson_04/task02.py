# В первом варианте для поиска элементов соответствующих условию, пишем отдельную функцию.
def func_list(n):
    i = list_origin.index(n)
    if i > 1:
        # Определяем индекс элемента в списке если он больше второго, сравниваем с предыдущим элементом.
        result = True if list_origin[i] > list_origin[i - 1] else False
    else:
        result = False
    return result


list_origin = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list_new = [el for el in list_origin if func_list(el)]
print(list_new)

# вариант - 2
# Во втором варианте нумеруем список и сравниваем элементы с предыдущими начиная со второго.
list_origin = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list_new = [el for n, el in enumerate(list_origin, -1) if n > 0 and el > list_origin[n]]
print(list_new)
