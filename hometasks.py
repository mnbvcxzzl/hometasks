# задание1
name = "Таня"
print(name)

# задание2
age = 18
print(age)

# задание3
name = "Таня " * 5
print(name)

# задание4-5-9
name = input("Ваше имя? ")
age = input("Ваш возраст? ")

flag = 1
try:
    name = int(name)
except ValueError:
    try:
        age = int(age)
    except ValueError:
        flag = 0
        n = "Привет, ты указал неправильно возраст!"
else:
    flag = 0
    n="Привет, ты указал некорректное имя!"

if flag == 1:
    if " " in name:
        n = "Введи имя без пробелов!"
        flag = 0

if flag == 1:
    if int(age) <= 0 or int(age) > 150:
        n = "ты указал неверный возраст."
    elif int(age) <= 7:
        n = "первый период детства."
    elif int(age) > 7 and int(age) < 13:
        n = "второй период детства."
    elif int(age) > 12 and int(age) < 17:
        n = "подростковый возраст."
    elif int(age) > 16 and int(age) < 22:
        n = "юношеский возраст."
    elif int(age) > 21 and int(age) < 36:
        n = "первый период зрелого возраста."
    elif int(age) > 35 and int(age) < 61:
        n = "второй период зрелого возраста."
    elif int(age) > 60 and int(age) < 76:
        n = "пожилой возраст."
    elif int(age) > 75 and int(age) < 91:
        n = "старческий возраст."
    elif int(age) > 90:
        n = "долгожитель. Поздравляю!"
    print("Привет,", name,"! Твой возрастной период -", n)
else:
    print(n)


# задание6
name = input("Ваше имя?")
list(name)
print(name[::-1])
print(name[1:-1])
print(name[len(name) - 3:])
print(name[0:4])

# задание8
name = input("Ваше имя?")
print(name.upper())
print(name.lower())

# задание10
def ex(a):
    try:
        a = int(a)
    except ValueError:
        a = input("Вам нужно ввести численное значение! - ")
        return ex(a)
    if int(a) == (2 * 2 + 2):
        print("Правильно!")
    else:
        print("Неравильно!")
        a = input("Попробуйте еще раз - ")
        return ex(a)

a = input("Привет! Сколько будет 2*2+2 ?")
ex(a)



a = input("Привет! Сколько будет 2*2+2 ?")

try:
    a = int(a)
except ValueError:
    a = input("Вам нужно ввести численное значение! - ")

if int(a) == (2 * 2 + 2):
    print("Правильно!")
else:
    print("Неравильно!")
