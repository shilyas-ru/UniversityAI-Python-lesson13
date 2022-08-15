"""
ЗАДАНИЕ 1
1. В подпрограмме Мой банковский счет;
2. Добавить сохранение суммы счета в файл.

При первом открытии программы на счету 0
После того как мы воспользовались программой и вышли сохранить сумму счета
При следующем открытии программы прочитать сумму счета, которую сохранили
...
3. Добавить сохранение истории покупок в файл

При первом открытии программы истории нет.
После того как мы что нибудь купили и закрыли программу сохранить историю покупок.
При следующем открытии программы прочитать историю и новые покупки уже добавлять к ней;
...
4. Формат сохранения количество файлов и способ можно выбрать самостоятельно.
"""


import json
from os.path import isfile

from personal_account import personal_account


# Проверяем, что существует файл с историей.
if isfile('data_json.txt'):
    # Если файл с историей существует, то историю загружаем.
    # Корректность данных не проверяем
    with open('data_json.txt', 'r') as f:
        account, account_lst, history_lst = json.load(f)
    print('Файл с историей загружен.')
else:
    # Если файл с историей отсутстует, то
    # инициируем переменные нулевыми значениями.
    account = 0         # Исходное состояние счёта
    account_lst = []    # Список хранит историю поступлений и списаний со счёта.
    history_lst = []    # Список хранит историю покупок.
                        # Будет храниться в виде кортежей (название покупки, сумма покупки).
                        # То есть, итоговый список с историей будет примерно такой:
                        # [('Наименование1', 100), ('Наименование2', 200)]

print('\n\nВнимание!!!\nВводить цифры требуется только целые,\n' +
      'проверка корректности ввода не производится!\n')

# Основной цикл по работе с программой "Банковский счёт"
while True:
    account, account_lst, history_lst = personal_account(account=account,
                                                         account_lst=account_lst,
                                                         history_lst=history_lst)

    choice = input('Запустить приложение "Мой банковский счет" ещё раз ("да" - д)? ')
    if choice != 'д':
        break

# Сохранение истории в файл
with open('data_json.txt', 'w') as f:
    json.dump((account, account_lst, history_lst), f, ensure_ascii=False)