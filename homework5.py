# def create_vars(*args, **kwargs):
#    # 1.Переменной var_int присвойте значение 10, var_float - значение 8.4, var_str - "No".
#     var_int = 10
#     print(var_int, type(var_int))
#     var_float = 8.4
#     print(var_float, type(var_float))
#     var_str = "No"
#     print(var_str, type(var_str))
#
#     return var_int, var_float, var_str
# result = create_vars()
# print(result)


def big_int():
    # Измените значение, хранимое в переменной var_int, увеличив его в 3.5 раза, результат свяжите с
 # переменной big_int.
    return  var_int_2 * 3.5
var_int_2 = 11
print(var_int_2, type(var_int_2))

result = big_int()
print(result)


def subtraction(var_fl):
# Измените значение, хранимое в переменной var_float,
# уменьшив его на единицу, результат свяжите с той же переменной.
    result = var_fl - 1
    return result

var_fl = subtraction(8.4)
print("var_fl:", var_fl)


def unique_val():
# Есть список: [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3] оставить в нем только уникальные
# значения.
    return list_unique_value
list_unique_value = []
value = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
value_2 = set(value)

for value in value_2:
    list_unique_value.append(value)
print(unique_val())



