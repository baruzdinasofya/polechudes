list0 = ['чихание', 'сковорода', 'болтливость', 'подросток', 'каблук', 'ложь', 'терроризм', 'ошибка']
alphabet = ['a', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
word = list0.pop()
word0 = '_' * len(word)
print('Ваше слово:', word0)
print('Начнем игру, выберите действие:')
print('1. сдаться')
print('2. ввести букву')
print('3. отгадать слово')
number = int(input())
while number != 1 or number != 2 or number != 3:
    print('Вы ввели недопустимое значение, попробуйте снова:')
    number = int(input())
if number == 1:
    print('Удачи в следующий раз :(')
    input()
elif number == 3:
    print('Введите слово:')
    answer = input()
    if answer == word:
        print('Вы отгадали слово! Хотите попробовать еще раз?')
        print('1. да')
        print('2. нет')
        answer_numb = int(input())
        while answer_numb != 1 or answer_numb != 2:
            print('Вы ввели недопустимое значение, попробуйте снова:')
            answer_numb = int(input())
        if answer_numb == 2:
            print('Удачи, ждем вас снова!')
