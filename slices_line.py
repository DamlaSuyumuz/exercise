# Вводятся два слова (через пробел в одной строке). Длина первого слова меньше второго. 
# Необходимо обрезать второе слово до длины первого и отобразить обрезанное слово на экране.


s1, s2 = map(str, input().split())
ls1 = len(s1)

print(s2[0:ls1])
