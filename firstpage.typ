
#let undertitle(title, width: auto, body) = {
    layout(size => {
        stack(
            dir: ttb,
            body,
            block(inset: (y: 3pt)),
            text(size: 5pt)[(#title)]
        )
    })
}

#let dush(count) = box(width: count, line(length: 100%))

#table(
    stroke: none,
    columns: (5fr, 1fr,5fr),
    [*УТВЕРЖДАЮ*],[], [*УТВЕРЖДАЮ*],
    [Генеральный директор \ ООО «ПочтаТех»], [],[Заместитель генерального \ директора по информационным \ технологиям и развитию  цифровых \ сервисов АО «Почта России»],
    [], [], [],
    [
        #table(
            row-gutter: 18pt,
            stroke: none,
            columns: (1fr,auto),
            align: (x,y) => if x == 0 { center } else { center },
            rows: 1,
            [#undertitle("Подпись", width: 100%)[#box(width: 100%, repeat[\_])]], [#undertitle("ФИО", width: 100%)[Садыков Д.Н.]],
        )
    ],
    [],
    [
        #table(
            row-gutter: 18pt,
            stroke: none,
            columns: (1fr,auto),
            align: (x,y) => if x == 0 { center } else { center },
            rows: 1,
            [#undertitle("Подпись", width: 100%)[#box(width: 100%, repeat[\_])]], [#undertitle("ФИО", width: 100%)[Савкин В.В.]],
        )
    ]
)

#parbreak()
#square(size: 2cm, stroke: none)

#text(size: 14pt)[
    #set align(center)
    #upper("Заявка на выполнение работ №")
]

#text(size: 12pt)[
    #set align(center)
    к Договору № #dush(10mm) / #dush(10mm) -- #dush(10mm) от « #dush(10mm) » #dush(50mm) 202 #dush(5mm) г. \
    на выполнение работ по созданию новых информационных систем, развитию и оказание услуг в отношении Комплекса информационных систем АО «Почта России»
]

#square(size: 1cm, stroke: none)

#text(size: 14pt)[
    #set align(center)
    *ПРОГРАММА и МЕТОДИКА ИСПЫТАНИЙ*
]

#square(size: 1cm, stroke: none)

#text(size: 12pt)[
    #set align(center)
    на развитие информационной автоматизированной системы \ «КурьерХаб» в рамках инициативы «Развитие системы КурьерХаб 2024»
]

#square(size: 2cm, stroke: none)

#text(size: 12pt)[
    #set align(center)
    На
    #context counter(page).final().at(-1)
    листах
]
