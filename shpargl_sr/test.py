import sys

# обращение в аргументам из командной строки

print(sys.argv[1])  # вывод первого элемента

# 3 5 7 9 11 => 3

print(sys.argv[-1])  # вывод последнего элемента

# 3 5 7 9 11 => 11

print(sys.argv[1:])  # вывод всех элементов

# 3 5 7 9 11 => ['3', '5', '7', '9', '11']
