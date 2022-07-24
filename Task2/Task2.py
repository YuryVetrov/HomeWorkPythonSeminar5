# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего 
# конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"
from colorama import init, Fore, Back, Style
init(autoreset=True)
import random
 
def inputUser(text=None, typeInt=True, condition=False):
    checkInput = False
    if not text:
        typeText = ('целое' if typeInt else 'вещественное') + ' число'
    else:
        typeText = text
    while not checkInput:
        try:
            num = input(f'{typeText}: ')
            n = int(num) if typeInt else float(num)
            condition = (lambda x: True if x > -1 else False) if not condition else condition
            checkInput = True if condition(n) else print('Сделайте корректный ввод')
        except:
            print()
            print(Fore.GREEN + f'{typeText} Введите число корректно ')
    if checkInput:
        return n
    
def main():
    print(Fore.YELLOW + 'Игра окончена!')
    print('\n')
count = 121 #2021
maxStepCount = 28
print(Fore.GREEN + f'Привет! Ну что, поиграем?\nНа столе {count} конфета\n')
print(Fore.YELLOW + f'За ход можно взять не более {maxStepCount} конфет\n')
print(Fore.BLUE +'Побеждает тот, кто делает последний ход!\n')
print('Выберете сложность игры от 0 до 1')
difficult = inputUser('1 - лёгкий уровень, 0 - сложный уровень', True,  lambda x: True if x in range(2) else False)
print(Fore.GREEN + 'Вы выбрали лёгкий уровень сложности') if difficult else print(Fore.YELLOW + 'Вы выбрали сложный уровень игры.\n')
n = inputUser('Загадайте число от 0 до 1.\n Если угадаете, то будете ходить первым', True,
              lambda x: True if x in range(2) else False)
draw = random.randint(0, 1)
lastStep = 0
if draw == n:
    main()
    print(Fore.BLUE + f'Выпало {draw}, Вы угадали! \nДелайте первый ход!')
    lastStep = 1
else:
    print(Fore.RED + f'Выпало {draw}. Бот ходит первый')
while count > 0:
    print(Fore.YELLOW + f'--------{lastStep + 1} ход---------')
    print(Fore.BLUE + f'На столе осталось {count} конфет')
    if lastStep % 2 == 1:
        print(Fore.GREEN + 'Ваш ход')
        step = inputUser('Выберете количество конфет', True, lambda x: True if 0 < x <= maxStepCount else False)
    else:
        print(Fore.RED + 'Ходит бот')
        if difficult == 0:
            step = random.randint(0, maxStepCount)
        else:
            step = maxStepCount if count % maxStepCount == 0 else count % maxStepCount
        print(f'Бот забрал {step} конфет')
    count = count - step if count - step > 0 else 0
    lastStep += 1
if lastStep % 2 == 0:
    main()
    print(Fore.GREEN + 'Вы победили, поздравляем!')
    print('\n')
else:
    print(Fore.RED + 'Вы проиграли. Но ничего страшного, попробуйте ещё раз.')
    main()
    