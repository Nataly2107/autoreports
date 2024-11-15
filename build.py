#!/usr/bin/env python

import os
import pandas
from pandas import read_excel

def to_typst(text):
    return text.replace('*', '\*').replace('[', '\[').replace(']', '\]').replace('<', '\<').replace('>', '\>').replace('@', '\@')

def load_data():
    lines = []
    with open("tasks.txt", "rt") as f:
        lines = f.readlines()

    ctz = {}
    m = {}
    N = 1
    for line in lines:
        a = line.split(";")
        if len(a) > 1:
            ctz[a[0].strip()] = N
            m[N] = a[1].strip()
            N += 1

    tests = pandas.read_csv('tests.csv', delimiter=';')
    height, _ = tests.shape

    indexs = [h for h in range(height) if type(tests['Задача'][h]) is str]

    records = []
    for i in range(len(indexs)-1):
        z = tests['Задача'][indexs[i]]
        r = {
            'Задача': z,
            'Наименование': [],
            'Предусловия': [],
            'Ожидаемый результат': [],
            'Шаги': [],
            'ЧТЗ': ctz[z],
            'Требование': m[ctz[z]]
        }

        for n in range(indexs[i], indexs[i + 1]):
            if type(tests['Наименование'][n]) is str:
                r['Наименование'] = to_typst(tests['Наименование'][n])
            if type(tests['Предусловия'][n]) is str:
                r['Предусловия'].append(tests['Предусловия'][n])

            if type(tests['Шаги'][n]) is str:
                r['Шаги'].append(tests['Шаги'][n])
                if type(tests['Ожидаемый результат'][n]) is str:
                    r['Ожидаемый результат'].append(tests['Ожидаемый результат'][n])
                else:
                    r['Ожидаемый результат'].append(" ")

        records.append(r)

    records = sorted(records, key=lambda x: x['ЧТЗ'])
    return records


def tests(records):
    with open("request.typ", "wt") as f:
        f.write("#pagebreak()\n")
        f.write("#set page(flipped: true)\n\n")
        f.write("*Таблица 1 - Перечень требований*\n")
        f.write("\n")
        f.write("#table(\n")
        f.write("    columns: (0.5fr, 3fr, 0.75fr, 6fr),\n")
        f.write("    table.header([*N*], [*Текст\ требования*], [*Раздел\ ЧТЗ*], [*Наименование теста\ (контрольного сценария)*]), \n")
        f.write("\n")
        ctz = sorted(list(set(map(lambda x: x['ЧТЗ'], records))))
        N = 1
        for c in ctz:
            d = [x for x in records if x['ЧТЗ'] == c]
            if len(d) > 0:
                req = d[0]['Требование']
                ctz = d[0]['ЧТЗ']
                tests_name = list(map(lambda x: x['Наименование'], d))
                f.write("[{}], [{}], [2.2.1.{}], [{}],\n".format(N, req, N, " \\ \n".join(tests_name)))
                N += 1

        f.write(")\n")


def gloss():
    lines = []
    with open("gloss.txt", "rt") as f:
        lines = f.readlines()

    with open("gloss.typ", "wt") as f:
        f.write("= *#upper(\"Глоссарий\")*\n")
        f.write("\n")
        f.write("#table(")
        f.write("    columns: (1fr,4fr),")
        f.write("    table.header[*Термин, сокращение*][*Определение*], //выравнить заколовок по центру\n")
        f.write("\n")
        for line in lines:
            a = line.split(";")
            #print("DEBUG>", a)
            if len(a) > 1:
                f.write("    [{}], [{}],\n".format(a[0], a[1].strip()))
            else:
                print("WRONG LINE: " + line)
        f.write(")\n")


def app(records):
    with open("app.typ", "wt") as f:
        f.write("#pagebreak()\n")
        f.write("#set page(flipped: true)\n")
        f.write("\n")
        f.write("*ПРИЛОЖЕНИЕ 1 КОНТРОЛЬНЫЕ СЦЕНАРИИ ДЛЯ ПРОВЕРКИ ПОЛНОТЫ И КАЧЕСТВА РЕАЛИЗАЦИИ ФУНКЦИЙ СИСТЕМ*\n")
        f.write("\n")
        f.write("#show table: set par(leading: 0.6em)\n")
        f.write("\n")
        f.write("#table(\n")
        f.write("    columns: (0.5fr, 1fr, 1.5fr, 4.5fr, 4fr, 2fr),\n")
        f.write("    table.header([*N*], [*Пункт\ ЧТЗ*], [*Проверка*], [*Шаги проверки*], [*Ожидаемый результат*], [*Система, в которой выполняется проверка*]),\n")
        f.write("\n")

        records = sorted(records, key=lambda x: x['ЧТЗ'])
        N = 0
        for r in records:
            N += 1

            f.write("table.cell(rowspan: {})[{}],\n".format(1 + len(r['Шаги']), N))
            f.write("table.cell(colspan: 5)[")
            f.write("Проверка: " + r['Наименование'] + " \ \n")
            f.write("Предварительное условие: \ ")
            for cond in r['Предусловия']:
                f.write("\n + " + to_typst(cond))
            f.write("\n],\n")

            f.write("table.cell(rowspan: {})[2.2.1.{}],\n".format(len(r['Шаги']), r['ЧТЗ']))
            f.write("table.cell(rowspan: {})[{}],\n".format(len(r['Шаги']), to_typst(r['Требование'])))
            for i in range(len(r['Шаги'])):
                f.write("[{}],\n".format(to_typst(r['Шаги'][i])))
                f.write("[{}],\n".format(to_typst(r['Ожидаемый результат'][i])))
                f.write("[Курьер Хаб],\n")

        f.write(")\n")
    pass

records = load_data()

gloss()
tests(records)
app(records)

os.system("typst compile example.typ example.pdf")
