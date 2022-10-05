# 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком


lang = ['java', 'python', 'c#', 'c', 'c++', 'javascript', 'typescript', 'php']
nums = [i for i in range(1, len(lang)+1)]
ln = list(zip(nums,lang))
for i in range(len(ln)):
    ln[i] = list(ln[i])
    ln[i][1] = str(ln[i][1]).upper()
    ln[i] = tuple(ln[i])
print(ln)
for i in range(len(ln)):
    ln[i] = list(ln[i])
sums = []
for i in range(len(ln)):
    sum = 0
    for j in ln[i][1]:
        sum += ord(j)
    sums.append(sum)
print(sums)
ln_new = []
for i in range(len(ln)):
    if sums[i] % ln[i][0] == 0:
        ln_new.append((sums[i], ln[i][1]))
print(ln_new)


# 1 - Создайте программу для игры в ""Крестики-нолики"".


table_example = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
table = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
def print_table(t:list):
    print(t[0] + ' | ' + t[1] + ' | ' + t[2])
    print('----------')
    print(t[3] + ' | ' + t[4] + ' | ' + t[5])
    print('----------')
    print(t[6] + ' | ' + t[7] + ' | ' + t[8])

def check_game(sym, t:list):
    if sym == t[0] and sym == t[1] and sym == t[2]:
        return 1
    elif sym == t[3] and sym == t[4] and sym == t[5]:
        return 1
    elif sym == t[6] and sym == t[7] and sym == t[8]:
        return 1
    elif sym == t[0] and sym == t[3] and sym == t[6]:
        return 1
    elif sym == t[1] and sym == t[4] and sym == t[7]:
        return 1
    elif sym == t[2] and sym == t[5] and sym == t[8]:
        return 1
    elif sym == t[0] and sym == t[4] and sym == t[8]:
        return 1
    elif sym == t[2] and sym == t[4] and sym == t[6]:
        return 1
    elif t[0] != ' ' and t[1] != ' ' and t[2] != ' ' and t[3] != ' ' and t[4] != ' ' and t[5] != ' ' and t[6] != ' ' and t[7] != ' ' and t[8] != ' ' :
        return 2
    else:
        return 0

def check_index():
    while True:
        try:
            n = int(input())
            if (1 <= n <= 9):
                break
        except:
            print('Ввведите корректные данные!')
    return n

print('При вводе данных, куда будет ставиться значки, запомните индексы игры: ')
print_table(table_example)
print()
print("Игрок 1 ходит первым и играет - 'x' ")
print("Игрок 2 ходит вторым и играет - '+' ")
print()
while True:
    print_table(table)
    print('Игрок 1, введи индекс куда поставить - "x" ')
    while True:
        c1 = check_index() - 1
        if table[c1] == ' ' :
            table[c1] = 'x'
            break
        else:
            print('Введите индекс по адресу которого нет символа!')
    print_table(table)
    v = check_game('x', table)
    if v == 1:
        print('Игрок 1 выиграл!')
        break
    if v == 2:
        print('Ничья!')
        break
    print('Игрок 2, введи индекс куда поставить - "0" ')
    while True:
        c2 = check_index() - 1
        if table[c2] == ' ':
            table[c2] = '0'
            break
        else:
            print('Введите индекс по адресу которого нет символа!')
    print_table(table)
    v = check_game('0', table)
    if v == 1:
        print('Игрок 2 выиграл!')
        break
    if v == 2:
        print('Ничья!')
        break