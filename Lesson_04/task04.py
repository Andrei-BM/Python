# Формируем список из неповторяющихся элементов исходного.
list_origin = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
list_new = [el for el in list_origin if
            list_origin.count(el) == 1]  # Для отбора используем функцию подсчета элементов списка
print(list_new)
