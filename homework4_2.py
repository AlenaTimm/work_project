# Работа с переменными

# var_int = 10
# var_float = 8.4
# var_str = "No"
# big_int = var_int * 3.5
# print(big_int)

# Строки

# n = "Hi, friends"
# print(type(n))
# print(n[0])
# print(n[-1])
# print(n[2])
# print(n[-3])
# print(len(n))
#
# k = "my name is {}"
# print(k.format("Alena"))

# Списки
# set_1 = [1, 2, 3, 4, 5]
# set_2 = [3, 4, 5, 6, 7]
# print(set_1[1])
# set_1[1] = -2
# print(set_1)

# Логические операции
# a = 1
# b = 2
# print((a > 0) and (b > 0))
# print((a<=10) and (b == 0))
# print((a == 0) and (b == 3))
# print((a == 1) and (b == 2))
#
# print((a > 4) or (b > 0))
# print((a >= 0) or (b > 7))
# print((a >= 10) or (b > 8))
# print((a > 6) or (b < 1))

# Словари
# school = {
#     "1a" : 10,
#     "1b" : 11,
#     "1c" : 12,
#     "1d" : 13,
#     "1f" : 10,
#     "2a" : 11,
#     "2b" : 12,
#     "2c" : 13,
#     "2d" : 14,
#     "2e" : 15
# }
# print(school["1a"])

# Преобразование типов
# name = "Robin Singh"
# name_list = list(name)
# print(name_list)
# text = "I love arrays they are my favorite"
# text_list = list(text)
# print(text_list)
#
# text_print = ["I", "love", "arrays", "they", "are", "my", "favorite"]
# print(" ".join(text_print))

# Условия
# n = 5
# if n > 0:
#     n += 1
#     print(n)
# else:
#     print(n)
#
# aa = -1
# bb = 1
# cc = 10
# summ = 0;
# if aa > 0:
#     summ = summ + 1
# if bb > 0:
#     summ = summ + 1
# if cc > 0:
#     summ = summ + 1
# print("Количество положительных чисел: ", summ)

# Цикл for

# n = 2
# m = 4
# result = 0
# for i in range(n, m+1):
#     result += i
# print(result)
#
# print("Введите наименьшее число диапазона")
# a=int(input())
# print("Введите наибольшее число диапазона")
# b=int(input())
# sum_ = 0
# for i in range(a,b+1):
#     sum_ += i
# print(sum_)

# Цикл while

# j = 5
# factorial = 1
# while j > 1:
#     factorial *= j
#     j -= 1
# print(factorial)

l = 10
c = 0
s = 0
while l > 0:
    c += 1
    s += l % 10
    l //= 10
print(c, s)