# 2- Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). 
# Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

def ControlNumber(lim, nums):
    while True:
        try:
            n = int(input())
            if (1 <= n <= lim) and (nums >= lim):
                break
            elif (1 <= n < nums) and (nums < lim):
                break
            else:
                print(f'Введите корректное число: ')
        except:
            continue
    return n

N2 = None
n2 = None
while True:
    print('Введите число конфет (от 100 до 1000):')
    N2 = input()
    try:
        N2 = int(N2)
        if 10000 >= N2 >= 100:
            print('Введите максимальное число конфет которые можно взять за раз (от 10 до 50):')
            n2 = input()
            try:
                n2 = int(n2)
                if 50 >= n2 >= 10:
                    break
                else:
                    print('Введите корректные данные!')
            except: continue
        else:
            print('Введите корректные данные!')
    except: continue
print(f"Число конфет: {N2}, за один раз можно взять от 1 до {n2} конфет")

bh = input('С кем бем играть? С ботом - введите цифру 0, с человеком любой другой символ: ')
fs2 = None
if bh == '0':
    input('Определяем кто ходит первым, нажмите Enter ')
    fs2 = random.randint(1, 2)
    if fs2 == 1:
        print('Первым ходит Игрок, вторым Бот')
        while N2 > 1:
            g1 = ControlNumber(n2, N2)
            N2 -= g1
            if N2 == 1:
                print('Бот проиграл!')
                break
            print(f'Осталось конфет {N2}')
            print('Ход делает Бот')
            if (2*n2+1 < N2):
                g2 = random.randint(1,n2)
            elif N2 <= n2:
                g2 = N2 - 1
            elif (2*n2 >= N2 > n2):
                g2 = N2 - n2 - 1
            N2 -= g2
            if N2 == 1:
                print('Игрок проиграл!')
                break
            print(f'Осталось конфет {N2}')
    else:
        print('Первым ходит Бот, вторым Игрок')
        while N2 > 1:
            print('Ход делает Бот')
            if (2 * n2 + 1 < N2):
                g2 = random.randint(1, n2)
            elif N2 <= n2:
                g2 = N2 - 1
            elif (2 * n2 >= N2 > n2):
                g2 = N2 - n2 - 1
            N2 -= g2
            if N2 == 1:
                print('Игрок проиграл!')
                break
            print(f'Осталось конфет {N2}')
            g1 = ControlNumber(n2, N2)
            N2 -= g1
            if N2 == 1:
                print('Бот проиграл!')
                break
            print(f'Осталось конфет {N2}')
else:
    input('Определите кто из вас Игрок1, кто - Игрок2, мы определим кто ходит первый, нажмите Enter ')
    fs2 = random.randint(1,2)
    if fs2 == 1:
        print('Первым ходит Игрок1, вторым Игрок2')
        while N2 > 1:
            print('Игрок1')
            g1 = ControlNumber(n2,N2)
            N2 -= g1
            if N2 == 1:
                print('Игрок2 проиграл!')
                break
            print(f'Осталось конфет {N2}')
            print('Игрок2')
            g2 = ControlNumber(n2, N2)
            N2 -= g2
            if N2 == 1:
                print('Игрок1 проиграл!')
                break
            print(f'Осталось конфет {N2}')
    else:
        print('Первым ходит Игрок 2, вторым Игрок 1')
        while N2 > 1:
            print('Игрок 2')
            g1 = ControlNumber(n2, N2)
            N2 -= g1
            if N2 == 1:
                print('Игрок 1 проиграл!')
                break
            print(f'Осталось конфет {N2}')
            print('Игрок1')
            g2 = ControlNumber(n2, N2)
            N2 -= g2
            if N2 == 1:
                print('Игрок2 проиграл!')
                break
            print(f'Осталось конфет {N2}')