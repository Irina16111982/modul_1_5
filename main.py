immutable_var = (1, 3, 5, 'str', True)
print(immutable_var)
# immutable_var[0] = 11
# print(immutable_var)
# изменить кортеж нельзя, так как это неизменямый тип данных.
# Если нужен изменяемый, то буду использовать список.
# кортеж удобно использовать когда необходима неизменность (постоянство) данных.
# кортеж занимает меньше места, чем список.

mutable_list = [1, 2, 5, 'str', True]
print(mutable_list)
mutable_list[0] = 11
print(mutable_list)
mutable_list.append(88)  # добавила значение в конец строки
print(mutable_list)
mutable_list.insert(0, 44)  # добавила значение 44 в начеле строки.
print(mutable_list)
print(len(mutable_list))  # посчитала количество элементов списка
mutable_list.remove(44)  # удалила значение 44, которое добавляла ранее
print(mutable_list)
print(mutable_list[-1])  # последний элемент строки 88
print(mutable_list[-2])  # предпоследний элемент строки True
del mutable_list[-1]  # удалила полседний элемент строки
print(mutable_list)
print(8 in mutable_list)  # проверила, что цифры 8 нет в списке
print(11 in mutable_list)  # число 11 есть в списке
mutable_list[0] = 1
print(mutable_list)  # вернулась к первоначальному списку
print("длина кортежа составляет ", immutable_var.__sizeof__())  # длина кортежа
print("длина списка составляет ", mutable_list.__sizeof__())  # длина списка
