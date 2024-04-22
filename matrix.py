# Вводится  матрица чисел из трех строк. 
# В каждой строке числа разделяются пробелом. 
# Необходимо вывести на экран последний столбец этой матрицы в виде строки из трех чисел через пробел.


a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

data = [a, b, c]

new_lst = [data[0][-1], data[1][-1], data[2][-1]]

print(*new_lst)
