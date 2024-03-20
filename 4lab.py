def nom1():
    a = int(input("Введите число: "))
    if a % 3 == 0:
        print("Число деляится на 3!")
    else:
        print("Число не делится на 3! ")


def nom2():
    try:
        a = 100
        ch = int(input("Введите число: "))
        rez = a / ch
        print("Результат: ", str(a), "/", str(ch), "=", str(rez))
    except ZeroDivisionError:
        print("Деление на 0 невозможно")
    except ValueError:
        print("Введено буква, а не цифра")


def nom3():
    den = int(input("Введите день: "))
    mec = int(input("Введите месяц: "))
    god = str(input("Введите год: "))
    god_len = len(god)
    if god_len == 4 and den in range(1, 32) and mec in range(1, 13):
        god1 = god[-2:]
        god1 = int(god1)
        pr = den * mec
        if pr == god1:
            print("Счастливая дата")
        else:
            print("Несчастливая дата")
    else:
        print("Введенa некорректная дата")


def nom4():
    s1 = 0
    s2 = 0
    x = str(input("Введите номер вашего билета: "))
    if len(x) % 2 == 0:
        x1_2 = len(x) // 2
        half_left = int(x[:x1_2])
        half_right = int(x[x1_2:])
        for i in range(x1_2):
            s1 = int(s1) + int(x[i])
        for i in range(x1_2, len(x)):
            s2 = int(s2) + int(x[i])

        if s1 == s2:
            print("Ваш билет счастливый!")
        else:
            print("Ваш билет несчастливый!")
    else:
        print("Неверно введено количество чисел")
