# Вводится целое число. Необходимо переменной msg присвоить строку "кратно 3", если введенное число кратно 3, а иначе присвоить строку "не кратно 3". 
# Реализовать программу с использованием тернарного оператора. Переменную msg отобразить на экране.

a = int(input())

msg = "кратно 3" if a%3==0 else "не кратно 3"
print(msg)