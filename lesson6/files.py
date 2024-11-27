from fileinput import close

f = open("text.txt","r")
for line in f:
    print(line[0])
    print(line[1])
    print(line[4])
    print(line[5])

    if len(line) < 3:
        print("Ошибка ввода. Количество символов неверно.")
    if len(line) > 3:
        print("Добро пожаловать!")

f.close()


f2 = open("text2.txt")
with open("text2_1.txt", "w") as f2_1:
    for i in f2:
        if int(i) % 2 == 0:
            print(i, file=f2_1)
with open("text2_2.txt", "w") as f2_2:
    print("hello!", file=f2_2, end="")
    for i in f2:
        if int(i) % 2 != 0:
            print(i, file=f2_2)

f2.close()

y = []
with open("text3.txt", "r") as f_3:
    for i in f_3:
        x = float(i)**2
        y.append(x)

f_3 = open("text3.txt", "w")
for x in y:
    f_3.write(str(x) + "\n")
f_3.close()


with open("binfl4.bin", "wb") as fb:
    fb.write(b"Good morning")

with open("binfl5.bin", "wb") as fb_2:
    fb_2.write(b"My name is Alena")

