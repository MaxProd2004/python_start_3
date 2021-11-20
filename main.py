# task 1
num_1 = int(input("num_1 = "))
num_2 = int(input("num_2 = "))
num_3 = int(input("num_3 = "))
num_4 = int(input("num_4 = "))

if num_1 > num_2 and num_1 > num_3 and num_1 > num_4:
    print(num_1)

if num_2 > num_1 and num_2 > num_3 and num_2 > num_4:
    print(num_2)

if num_3 > num_2 and num_3 > num_1 and num_1 > num_4:
    print(num_3)

if num_4 > num_2 and num_4 > num_3 and num_4 > num_1:
    print(num_4)

# task 2
num_of_flat = int(input("Enter the num of flat: "))

if num_of_flat >= 1 and num_of_flat <= 36:
    print("Эта квартира находится в первом подъезде ", end="")
    if num_of_flat <= 4:
        print("на первом этаже")
    if num_of_flat >= 5 and num_of_flat <= 8:
        print("на втором этаже")
    if num_of_flat >= 9 and num_of_flat <= 12:
        print("на третем этаже")
    if num_of_flat > 13 and num_of_flat <= 16:
        print("на четвертом этаже")
    if num_of_flat > 17 and num_of_flat <= 20:
        print("на пятом этаже")
    if num_of_flat > 21 and num_of_flat <= 24:
        print("на шестомом этаже")
    if num_of_flat > 25 and num_of_flat <= 28:
        print("на седьмом этаже")
    if num_of_flat > 29 and num_of_flat <= 32:
        print("на восьмом этаже")
    if num_of_flat > 33 and num_of_flat <= 36:
        print("на девятом этаже")

if num_of_flat >= 37 and num_of_flat <= 72:
    print("Эта квартира находится во втором подъезде ", end="")
    if num_of_flat <= 40:
        print("на первом этаже")
    if num_of_flat >= 41 and num_of_flat <= 44:
        print("на втором этаже")
    if num_of_flat >= 45 and num_of_flat <= 48:
        print("на третем этаже")
    if num_of_flat > 49 and num_of_flat <= 52:
        print("на четвертом этаже")
    if num_of_flat > 53 and num_of_flat <= 56:
        print("на пятом этаже")
    if num_of_flat > 57 and num_of_flat <= 60:
        print("на шестомом этаже")
    if num_of_flat > 61 and num_of_flat <= 64:
        print("на седьмом этаже")
    if num_of_flat > 65 and num_of_flat <= 69:
        print("на восьмом этаже")
    if num_of_flat > 69 and num_of_flat <= 72:
        print("на девятом этаже")

if num_of_flat >= 73 and num_of_flat <= 109:
    print("Эта квартира находится в третьем подъезде ", end="")
    if num_of_flat <= 76:
        print("на первом этаже")
    if num_of_flat >= 79 and num_of_flat <= 82:
        print("на втором этаже")
    if num_of_flat >= 83 and num_of_flat <= 86:
        print("на третем этаже")
    if num_of_flat > 87 and num_of_flat <= 90:
        print("на четвертом этаже")
    if num_of_flat > 91 and num_of_flat <= 94:
        print("на пятом этаже")
    if num_of_flat > 95 and num_of_flat <= 98:
        print("на шестомом этаже")
    if num_of_flat > 99 and num_of_flat <= 102:
        print("на седьмом этаже")
    if num_of_flat > 103 and num_of_flat <= 105:
        print("на восьмом этаже")
    if num_of_flat > 106 and num_of_flat <= 109:
        print("на девятом этаже")

if num_of_flat >= 110 and num_of_flat <= 145:
    print("Эта квартира находится в четвертом подъезде ", end="")
    if num_of_flat <= 113:
        print("на первом этаже")
    if num_of_flat >= 114 and num_of_flat <= 117:
        print("на втором этаже")
    if num_of_flat >= 118 and num_of_flat <= 121:
        print("на третем этаже")
    if num_of_flat > 122 and num_of_flat <= 125:
        print("на четвертом этаже")
    if num_of_flat > 126 and num_of_flat <= 129:
        print("на пятом этаже")
    if num_of_flat > 130 and num_of_flat <= 133:
        print("на шестомом этаже")
    if num_of_flat > 134 and num_of_flat <= 137:
        print("на седьмом этаже")
    if num_of_flat > 138 and num_of_flat <= 141:
        print("на восьмом этаже")
    if num_of_flat > 142 and num_of_flat <= 145:
        print("на девятом этаже")

elif num_of_flat > 145:
    print("Такой квартиры в этом доме нет!")

# task 3
year = int(input("Введите год: "))
if year % 4 == 0:
    print("Это высокосный год!")
else:
    print("Это обычный год!")

# task 4
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
sum_of_two_sides = a + b
if c < sum_of_two_sides:
    print("Такой треугольник не может существовать!")
else:
    print("Ну а такой конечно же может!")