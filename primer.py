#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys
import datetime


def get_human():
    """""
    Запросить данные о человеке.
    """""
    # Запросить данные о человеке.
    surname = input("Фамилия: ")
    name = input("Имя: ")
    zodiak = input("Знак Зодиака: ")
    date_str = input("Введите дату выпуска (dd/mm/yyyy)\n")
    date = datetime.datetime.strptime(date_str, '%d/%m/%Y').date()

    # Вернуть словарь.
    return {
        'surname': surname,
        'name': name,
        'zodiak': zodiak,
        'date': date
    }


def display_human(humans):
    """""
    Отобразить список людей
    """""
    # Проверить что список людей не пуст
    if humans:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 15
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                "№",
                "Фамилия и имя",
                "Знак Зодиака",
                "Дата рождения"
            )
        )
        print(line)

        # Вывести данные о всех.
        for idx, worker in enumerate(humans, 1):
            date = worker.get('date', '')
            print(
                '| {:^4} | {:<14} {:<15} | {:<20} | {}{} |'.format(
                    idx,
                    worker.get('surname', ''),
                    worker.get('name', ''),
                    worker.get('zodiak', ''),
                    date,
                    ' ' * 5
                )
            )

        print(line)

    else:
        print("Список работников пуст.")


def select_humans(humans, addedzz):
    """""
    Выбрать людей с заданным ЗЗ
    """""
    # Инициализировать счетчик.
    count = 0
    # Сформировать список людей
    result = []
    # Проверить сведения людей из списка.
    for human in humans:
        if human.get('zodiak', '') == addedzz:
            count += 1
            result.append(human)

    return result


def main():
    """""
    Главная функция программы
    """""
    print("help - список всех команд")
    # Список людей.
    humans = []

    # Организовать бесконечный цикл запроса команд
    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            human = get_human()
            # Добавить словарь в список.
            humans.append(human)
            # Отсортировать список в случае необходимости.
            if len(humans) > 1:
                humans.sort(key=lambda item: item.get('date', ''))

        elif command == 'list':
            display_human(humans)

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=1)
            addedzz = int(parts[1])
            selected = select_humans(humans, addedzz)
            display_human(selected)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить человека;")
            print("list - вывести список людей;")
            print("help - список всех команд;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная комманда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()