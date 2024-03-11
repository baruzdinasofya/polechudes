list0 = ['фортнайт', 'компания', 'болезнь', 'рождение', 'кетчуп', 'крипта', 'цыган', 'деньги']  # список слов
alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'] # алфавит
for_while = 1       # переменная, контролирующая цикл
while for_while == 1 and len(list0) != 0:
    word = list0.pop()      # загаданное слово
    word0 = '_' * len(word)     # загаданное слово, в котором скрыты неугаданные буквы
    print('Ваше слово:', word0)
    all_trying = 0      # попыток истрачено
    for_while = 2
    trying = 3      # попыток всего
    print('Начнем игру!')
    while for_while == 2:
        print('Выберите действие:')
        print('1. сдаться')
        print('2. ввести букву')
        print('3. отгадать слово')
        number = input()    # номер действия
        while number != '1' and number != '2' and number != '3':
            print('Упс, такого варианта нет, попробуйте снова:')
            number = input()
        if number == '1':
            print('Сдаваться - удел слабых, ждем вас снова')
            print('Попробуем еще раз?')
            print('1. да')
            print('2. нет')
            number1 = input()       # номер выбора
            while number1 != '1' and number1 != '2':
                print('Упс, такого варианта нет, попробуйте снова:')
                number1 = input()
            if number1 == '1':
                for_while = 1
            elif number1 == '2':
                for_while = 3
        elif number == '2':
            print('Введите букву:')
            print(*alphabet)
            letter = input().lower()    # буква, введенная пользователем
            all_trying += 1
            while letter not in alphabet or len(letter) > 1:
                print('Ошибка, попробуйте снова:')
                letter = input().lower()
            alphabet.remove(letter)
            word0 = list(word0)
            list_word = list(word)      # список букв, в загаданном слове
            if letter in word:
                print('Вы угадали букву! Введите букву:')
            else:
                print('Вы не угадали букву, но это неплохо')
            for i in range(list_word.count(letter)):
                word0.insert(list_word.index(letter), letter)
                del word0[list_word.index(letter) + 1]
                del list_word[list_word.index(letter)]
            print(''.join(word0))
            if word == ''.join(word0):
                print('Вы угадали слово ( ͡~ ͜ʖ ͡°)!')
                print('Кол-во потраченных попыток:', all_trying)
                print('Хотите попробовать еще раз?')
                print('1. да')
                print('2. нет')
                number1 = input()
                while number1 != '1' and number1 != '2':
                    print('Упс, такого варианта нет, попробуйте снова:')
                    number1 = input()
                if number1 == '1':
                    for_while = 1
                else:
                    for_while = 3
        elif number == '3':
            print('Введите слово:')
            answer = input()    # слово, которое хочет ввести пользователь
            trying += 1
            answer = answer.lower()
            if answer == word:
                print('Вы угадали слово!')
                print('Кол-во потраченных попыток:', all_trying)
                print('Хотите попробовать еще раз?')
                print('1. да')
                print('2. нет')
                number1 = input()
                while number1 != '1' and number1 != '2':
                    print('Упс, такого варианта нет, попробуйте снова:')
                    number1 = input()
                if number1 == '1':
                    for_while = 1
                else:
                    for_while = 3
            elif answer != word and trying > 1:
                print('Вы не отгадали слово')
                trying -= 1
                print('Осталось', trying, 'попыток')
                print('Хотите продолжить угадывать загаднное слово?')
                print('1. да')
                print('2. нет')
                number1 = input()
                while number1 != '1' and number1 != '2':
                    print('Упс, такого варианта нет, попробуйте снова:')
                    number1 = input()
                if number1 == '1':
                    for_while = 2
                else:
                    print('Хотите попробовать еще раз?')
                    print('1. да')
                    print('2. нет')
                    number1 = input()
                    while number1 != '1' and number1 != '2':
                        print('Упс, такого варианта нет, попробуйте снова:')
                        number1 = input()
                    if number1 == '1':
                        for_while = 1
                    else:
                        for_while = 3
            else:
                print('Попыток больше нет..')
                print('Хотите попробовать еще раз?')
                print('1. да')
                print('2. нет')
                number1 = input()
                while number1 != '1' and number1 != '2':
                    print('Упс, такого варианта нет, попробуйте снова:')
                    number1 = input()
                if number1 == '1':
                    for_while = 1
                else:
                    for_while = 3
if len(list0) == 0:
    print('А слов больше нет')
print('Надеюсь вам понравилась игра ( ͡~ ͜ʖ ͡°)')
print('Чтобы закончить программу, напечатайте любые символы)')
input()