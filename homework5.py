
def inc_tally(tally):
    return tally * 3.5
# Измените значение, хранимое в переменной tally, увеличив его в 3.5 раза, результат свяжите с
 # переменной icc_tal.
tally = inc_tally(15)
print(tally)


def subtraction(var_fl):
# Измените значение, хранимое в переменной var_float,
# уменьшив его на единицу, результат свяжите с той же переменной.
    result = var_fl - 1
    return result

var_fl = subtraction(8.4)
print("var_fl:", var_fl)


def a_list(un_list):
    return un_list
# Есть список: [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3] оставить в нем только уникальные
# # значения.
list_pr = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
un_list = list(set(list_pr))

print(un_list)
