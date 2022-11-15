import copy
# 1.Дан list произвольных чисел (напр [11, 77, 4, 22, 0, 56, 5, 95, 96, 7, 87, 13, 45, 67, 44]).
# Написать программу, которая удалит из него все числа, которые меньше 17 и больше 81.

lst = [10, 77, 4, 22, 0, 56, 5, 95, 96, 7, 87, 13, 45, 67, 44]

lst_a = copy.deepcopy(lst)
for itm in lst_a:
    if itm < 17 or itm > 81:
        lst.remove(itm)
print(lst)

# 2.Ввести из консоли строку. Найти в строке самое длинное слово,
# в котором присутствуют подряд две согласные буквы.
# Если в строке присутствует слово с тремя согласными буквами подряд - вывести его на экран

my_str = input("Введите строку:")
my_lst = my_str.split(" ")
my_tuple = ('b', 'd', 'c', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
            'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
my_lst1 = []
for item in my_lst:
    repeat = True  # Для избежания дубликации слов где несколько раз встречаются пары согласных
    counter_word = 0
    item.lower()
    for i in item:  # перебор слова по буквам
        if i in my_tuple:  # сравнение буквы с кортежем согласных букв
            counter_word += 1
        else:
            counter_word = 0

        if counter_word == 2:
            if repeat:
                my_lst1.append(item)
                repeat = False
        elif counter_word == 3:
            print(item)
            break
max_length = 0
for itm in my_lst1:
    if max_length < len(itm):
        max_length = len(itm)
print("Максимальная длина слова с двумя согласными: ", max_length)
#  print(my_lst1)
print("*" * 100)

# 3* Искусственный интеллект. Пользователь вводит строку.
# Определить что он ввел - email, номер телефона или имя.
# Правила определения email (abcd@abc.abc):
#     имя имейла - не менее трех букв
#     собака
#     домен - три буквы, точка, три буквы
# Правила определения телефона (+380671231211)-
#     +
#     11 цифр
# Правила определения имени (Bill Gates)-
#     два слова через пробел
#     оба слова с большой буквы
inp_str = input("Введите email, номер телефона или имя: ")

if inp_str[0] == "+" and len(inp_str[1:]) == 11:
    print("Ваш номер телефона: ", inp_str)
else:
    my_lst = inp_str.split(" ")
    if my_lst[0].istitle() and my_lst[1].istitle():
        print("Ваше имя: ", inp_str)
    else:
        try:
            start = len(inp_str[0:inp_str.index("@")])
            center = len(inp_str[inp_str.index("@"):inp_str.index(".")]) - 1
            end = len(inp_str[inp_str.index("."):]) - 1
            if start >= 3 and center == 3 and end == 3:
                print("Ваш email: ", inp_str)
            else:
                print("Введите корректные данные!")
        except:
            print("Введите корректные данные!")







