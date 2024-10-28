#!/usr/bin/env python

import os
from pandas import read_excel

def tests():
    df = read_excel('tests.xlsx', index_col=0)
    print(df.head()) # shows headers with top 5 rows

    print("\n\n\n")
    print(df)


def gloss():
    lines = []
    with open("gloss.txt", "rt") as f:
        lines = f.readlines()

    with open("gloss.typ", "wt") as f:
        f.write("#set table.hline(stroke: .6pt)\n")
        f.write("#upper[*Глоссарий*] //добавить выравнивание по центру\n")
        f.write("#table(")
        f.write("    columns: (1fr,5fr),\n")
        f.write("    stroke: 0.5pt + rgb(\"666675\"),\n")
        f.write("    align:horizon,\n")
        f.write("    table.header[*Термин, сокращение*][*Определение*], //выравнить заколовок по центру")
        for line in lines:
            a = line.split(";")
            # print("DEBUG>", a)
            if len(a) > 1:
                f.write("  [{}], [{}],\n".format(a[0], a[1].strip()))
            else:
                print("WRONG LINE: " + line)
        f.write(")\n")

gloss()
os.system("typst compile example.typ example.pdf")
