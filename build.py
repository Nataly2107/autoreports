#!/usr/bin/env python

import os
import pandas
from pandas import read_excel

def tests():
    # df = read_excel('tests.xlsx', index_col=0)
    # print(df.head()) # shows headers with top 5 rows

    # print("\n\n\n")
    # print(df)

    lines = []
    with open("tasks.txt", "rt") as f:
        lines = f.readlines()

    tests = pandas.read_csv('tests.csv',delimiter=';')
    N=1

    with open("request.typ", "wt") as f:
        f.write("#pagebreak()\n")
        f.write("#set page(flipped: true)\n")
        f.write("*Таблица 1 - Перечень требований*\n")
        f.write("\n")
        f.write("#table(\n")
        f.write("    columns: (0.5fr, 3fr, 0.75fr, 6fr),\n")
        f.write("    table.header([*N*], [*Текст\ требования*], [*Раздел\ ЧТЗ*], [*Наименование теста\ (контрольного сценария)*]), \n")
        f.write("\n")
        for line in lines:
            a = line.split(";")
            #print("DEBUG>", a)
            if len(a) > 1:
                tests_name = []
                z = a[0]
                indexs = []
                for i, v in enumerate(tests['Задача']):
                    if v == z:
                        indexs.append(i)
                # print(indexs)

                for i in indexs:
                    tests_name.append(tests['Наименование'][i].replace('*', '\*'))

                f.write("[{}], [{}], [2.2.1.{}], [{}],\n".format(N, a[1].strip(), N, " \\ \n".join(tests_name)))
            else:
                print("WRONG LINE: " + line)
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
        f.write("    //stroke: 0.25pt,")
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

gloss()
tests()

os.system("typst compile example.typ example.pdf")
