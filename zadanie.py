#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys


def show_commands():
    print("Список команд:\n")
    print("add - добавить студента;")
    print("list - вывести список студентов;")
    print("select <средний балл> - запросить студентов с баллом выше 4.0;")
    print("exit - завершить работу с программой.")


def add_student():
    # Запросить данные о студенте.
    name = input("Фамилия и инициалы? ")
    group = input("Номер группы? ")
    grade = str(input('Успеваемость: '))
    # Создать словарь.
    student = {
        'name': name,
        'group': group,
        'grade': grade,
    }
    # Добавить словарь в список.
    students.append(student)
    # Отсортировать список в случае необходимости.
    if len(students) > 1:
        students.sort(key=lambda item: item.get('group')[::-1])


def show_list():
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
            "Ф.И.О.",
            "Группа",
            "Успеваемость"
        )
    )
    print(line)
    # Вывести данные о всех студентах.
    for idx, student in enumerate(students, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                idx,
                student.get('name', ''),
                student.get('group', ''),
                student.get('grade', 0)
            )
        )
    print(line)


def show_selected():
    # Инициализировать счетчик.
    count = 0
    # Проверить сведения студентов из списка.
    for student in students:
        grade = list(map(int, student.get('grade', '').split()))
        if sum(grade) / max(len(grade), 1) >= 4.0:
            print(
                '{:>4} {}'.format('*', student.get('name', '')),
                '{:>1} {}'.format('группа №', student.get('group', ''))
            )
            count += 1
    if count == 0:
        print("Студенты с баллом 4.0 и выше не найдены.")


def main():
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            add_student()

        elif command == 'list':
            show_list()

        elif command.startswith('select'):
            show_selected()

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    # Список студентов.
    students = []
    show_commands()

    main()