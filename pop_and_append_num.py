# Вводятся целые числа в одну строчку через пробел. Необходимо преобразовать их в список lst , затем, удалить последнее значение и если оно нечетное, то в список (в конец) добавить True, иначе - False. 
# Отобразить полученный список на экране командой:
# print(*lst)
# Реализовать программу без использования условного оператора.

numbers = list(map(int, input().split()))

a = (numbers.pop()//2 == 0)
numbers.append(a)

print(*numbers)