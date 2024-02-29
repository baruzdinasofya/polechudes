set0 = {'чихание', 'сковорода', 'болтливость', 'подросток', 'каблук', 'ложь', 'терроризм', 'ошибка'}
alphabet = ['a', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
word = [i[1] for i in set0]
word0 = '_' * len(word)
print('Ваше слово:', word0)
print('Введите букву:')
letter = input()
while word0 != word:
    while letter not in alphabet:
        print('Ошибка! Вы ввели недопустимый символ, введите снова')
        letter = input()
    while len(letter) > 1:
        print('Ошибка! Слишком много букв, введите снова')
        letter = input()
    for i in range(len(word)):
        if word[i] == letter:
            word[i] = word0[i]
            print('Откройте букву!')
            print(word0)
            letter = input()
        else:
            print('Этой буквы нет в слове :(')
            letter = input()
print('Вы отгадали слово! Good job')