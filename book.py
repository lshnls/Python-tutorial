myscore=100
print('Мои очки: %s' % myscore)

nums='Что сказало число %s числу %s'
print(nums %(0,8))

print(10*'Десять приветов,')

spaces = ' ' * 25
print('%s Задний переулок 12' % spaces)
print('%s Трясогузочья пустошь' % spaces)
print('%s Западный Всхрапшир' % spaces)
print()
print()
print('Уважаемый Сэр,')
print()
print('Хочу сообщить вам, что кое-где на крыше уборной')
print('недостает кусков черепицы.')
print('Думаю, прошлой ночью их сдуло внезапным порывом ветра.')
print()
print('С почтением')
print('Малькольм Конфузли')

wizard_list = 'Паучьи лапки, жабий палец, глаз тритона, крыло летучей мыши, жир слизня, перхоть змеи'
print(wizard_list)
wizard_list = ['паучьи лапки', 'жабий палец', 'глаз тритона', 'крыло летучей мыши', 'жир слизня', 'перхоть змеи']
print(wizard_list)
print(wizard_list[2])
print(wizard_list[2:5])

some_numbers = [1, 2, 5, 10, 20]
some_strings = ['Нож', 'отточен', 'точен', 'очень']
numbers_and_strings = [7, 'раз', 'отпей', 1, 'раз', 'отъешь']
print(numbers_and_strings)

numbers = [1, 2, 3, 4, 5]
strings = ['хватит', 'циферки', 'считать']
mylist = [numbers, strings]
print(mylist)

wizard_list.append('медвежий коготь')
print(wizard_list)

wizard_list.append('мандрагора')
wizard_list.append('болиголов')
wizard_list.append('болотный газ')
print(wizard_list)

del wizard_list[5]
print(wizard_list)

del wizard_list[8]
del wizard_list[7]
del wizard_list[6]
print(wizard_list)

list1 = [1, 2, 3, 4, 5]
list2 = ['я', 'забрался', 'под', 'кровать']
print(list1 + list2)


list1 = [1, 2, 3, 4]
list2 = ['я', 'мечтаю', 'о', 'пломбире']
list3 = list1 + list2
print(list3)

list1 = [1, 2]
print(list1 * 5)

# Кортеж
fibs = (0, 1, 1, 2, 3)
print(fibs[3])

# Словарь
favorite_sports = {'Ральф Уильямс': 'Футбол',
'Майкл Типпетт': 'Баскетбол',
'Эдвард Элгар': 'Бейсбол',
'Ребекка Кларк': 'Нетбол',
'Этель Смит': 'Бадминтон',
'Фрэнк Бридж': 'Регби'}
print(favorite_sports['Ребекка Кларк'])

del favorite_sports['Этель Смит']
print(favorite_sports)

favorite_sports['Ральф Уильямс'] = 'Хоккей на льду'
print(favorite_sports)


# Упражнение
wishes=['компьютер', 'мясорубка','ведро']
things=['мото','вело','охота']
print(wishes+things)

# if
age = 21
if age > 20: 
    print('Как-то вы староваты!')

if age == 10:
    print("Что выйдет, если клюква наденет штаны?")
    print("Брюква!")
elif age == 11:
    print("Что сказала зеленая виноградина синей виноградине?")
    print("Дыши! Дыши!")
elif age == 12:
    print("Что сказал 0 числу 8?")
    print("Привет, ребята!")
elif age == 13:
    print("Что такое: на потолке сидит и хохочет?")
    print("Муха-хохотуха!")
else:
    print("Что-что?")

myval = None
print(myval)


age = '10'
converted_age = int(age)
if converted_age == 10:
    print("Как лучше всего общаться с монстром?")
    print("Издалека!")

converted_age = float(age)

# Циклы
for x in range(0, 5):
    print('привет')


print(list(range(10, 20)))

from random import random
print(list(range(0,int(random()*20))))

hugehairypants = ['огромные', 'волосатые', 'штаны']
for i in hugehairypants:
    print(i,":",sep="",end="\n")
    for j in hugehairypants:
        print(j)

found_coins = 20
magic_coins = 70
stolen_coins = 3
coins = found_coins
for week in range(1, 10):
    coins = coins + magic_coins - stolen_coins
    print('Неделя %s = %s' % (week, coins))

# While

step = 0
tired = False
badweather = False
while step < 10:
    print(step)
    if tired == True:
        break
    elif badweather == True:
        break
    else:
        step = step + 1

# Функции
def testfunc(myname):
    print('Привет, %s' % myname)
testfunc('Мэри')

def testfunc(fname, lname):
    print('Привет, %s %s' % (fname, lname))
testfunc('Мэри', 'Смит')

import sys
#print(sys.stdin.readline())

class Things:
    pass

class Inanimate(Things):
    pass
class Animate(Things):
    pass
class Sidewalks(Inanimate):
    pass
class Animals(Animate):
    pass
class Mammals(Animals):
    pass
class Giraffes(Mammals):
    pass

reginald = Giraffes()

def this_is_a_normal_function():
    print('Я — обычная функция')

class ThisIsMySillyClass:
    def this_is_a_class_function():
        print('Я – функция класса')
    def this_is_also_a_class_function():
        print('Я тоже функция класса, понятно?')

class Animals(Animate):
    def breathe(self):
        pass
    def move(self):
        pass
    def eat_food(self):
        pass

class Mammals(Animals):
    def feed_young_with_milk(self):
        pass
class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        pass


class Animals(Animate):
    def breathe(self):
        print('дышит')
    def move(self):
        print('двигается')
    def eat_food(self):
        print('ест')
class Mammals(Animals):
    def feed_young_with_milk(self):
        print('кормит детенышей молоком')
class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print('ест листья')

        reginald = Giraffes()

harold = Giraffes()
reginald = Giraffes()
                              reginald.move()
harold.eat_leaves_from_trees()
