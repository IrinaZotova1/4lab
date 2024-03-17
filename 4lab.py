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
    god_len=len(god)
    if god_len==4 and den in range(1, 32) and mec in range(1, 13):
        god1=god[-2:]
        god1=int(god1)
        pr=den*mec
        if pr==god1:
            print("Счастливая дата")
        else:
            print("Несчастливая дата")
    else:
        print("Введенa некорректная дата")

def nom4():
    x = str(input("Введите номер вашего билета: "))
    if len(x) == 6:
        x1 = x[0:3]
        x2 = x[3:7]
        print(x1, x2)
        x11 = int(x1[0:2])
        x12 = int(x1[1:3])
        x13 = int(x1[2:4])
        x21 = int(x2[0:2])
        x22 = int(x2[1:3])
        x23 = int(x2[2:4])
        s1=x11+x12+x13
        s2=x21+x22+x23
        if s1 == s2:
            print("Ваш билет счастливый!")
        else:
            print("Ваш билет несчастливый!")
    else:
        print("Неверно введено количество чисел")

