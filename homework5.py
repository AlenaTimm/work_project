def subtraction(var_fl):
# 1 Измените значение, хранимое в переменной var_float,
# уменьшив его на единицу, результат свяжите с той же переменной.
    result = var_fl - 1
    return result

var_fl = subtraction(8.4)
print("var_fl:", var_fl)

# 2 Измените значение, хранимое в переменной var_int, увеличив его в 3.5 раза, результат свяжите с
# переменной big_int.
def big_int(var_int):
    return var_int * 3.5

var_int = big_int(15)
print(var_int)


# 3. Есть список: [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3] оставить в нем только уникальные
def unique_list(a_list):
     return a_list

b_list = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
a_list =list(set(b_list))
print(a_list)
