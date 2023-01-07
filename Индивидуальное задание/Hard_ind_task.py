#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import json
import click


@click.group()
def cli():
    pass


@cli.command("add")
@click.argument("filename")
@click.option("-n", "--name")
@click.option("-p", "--phone")
@click.option("-d", "--date")
def add(filename, name, phone, date):
    mans = load_workers(filename)
    mans.append(
        {
            "name": name,
            "number": phone,
            "date": date,
        }
    )
    with open(filename, "w", encoding="utf-8") as fout:
        json.dump(mans, fout, ensure_ascii=False, indent=4)
    click.secho("Пользователь добавлен")


@cli.command("list")
@click.argument("filename")
def list_d(filename):
    list_man = load_workers(filename)
    if list_man:
        # Заголовок таблицы.
        line = "+-{}-+-{}-+-{}-+-{}-+".format("-" * 4, "-" * 30, "-" * 20, "-" * 20)
        print(line)
        print(
            "| {:^4} | {:^30} | {:^20} | {:^20} |".format(
                "No", "Имя", "Номер телефона", "Дата рождения"
            )
        )
        print(line)

        # Вывести данные о человеке.
        for idx, man in enumerate(list_man, 1):
            print(
                "| {:>4} | {:<30} | {:<20} | {:<20}  |".format(
                    idx, man.get("name", ""), man.get("number", ""), man.get("date", "")
                )
            )

        print(line)
    else:
        print("Список работников пуст: ")


@cli.command("select")
@click.argument("filename")
@click.option("-s", "--select")
def select(filename, select):
    mans_list = load_workers(filename)
    count = 0
    for man in mans_list:
        if man.get("number") == select:
            count += 1
            print("{:>4}: {}".format(count, man.get("name", "")))
            print("Номер телефона:", man.get("number", ""))
            print("Дата рождения:", man.get("date", ""))

    # Если счетчик равен 0, то человек не найден.
    if count == 0:
        print("Человек не найден.")


def save_workers(file_name_1, staff):
    with open(file_name_1, "w", encoding="utf-8") as fout:
        json.dump(staff, fout, ensure_ascii=False, indent=4, default=str)


def load_workers(file_name_2):
    with open(file_name_2, "r", encoding="utf-8") as fin:
        return json.load(fin)


if __name__ == "__main__":
    cli()
