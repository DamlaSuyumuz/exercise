# Вводится число новых подписчиков канала по дням в одну строку через пробел. 
# На основе введенной строки необходимо сформировать список lst из целых чисел. 
# Требуется отсортировать элементы этого списка по убыванию и результат вывести на экран командой: print(*lst)

subscribers = list(map(int, input().split()))

print(*(sorted(subscribers, reverse=True)))
