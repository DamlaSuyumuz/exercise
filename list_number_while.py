# На вход программе подается натуральное число n (то есть, целое положительное). 
# Прочитайте это число. 
# В цикле переберите все целые числа в интервале [1; n] (включая границы) и сформируйте список из чисел, кратных 3 и 5 одновременно.

# Выведите на экран полученный список чисел в одну строчку через пробел, если значение n меньше 100. 
# Иначе выведите на экран сообщение (без кавычек):

# "слишком большое значение n"

# Продумать логику работы программы так, чтобы после цикла while шел блок else.


number = int(input())

list_number = []
i = 1
while i <= number:
    if number < 100:
        if i % 3 == 0 and i % 5 == 0:
            list_number.append(i)
    else:
        print("слишком большое значение n")
        break
    i += 1

print(*list_number)
