from database.enum import FieldType


class Cpt_diary():
    title = "КПТ-дневник"
    description = "Это способ самоанализа, который позволяет отслеживать эмоции и чувства, выявлять взаимосвязи между "\
        "ситуациями и мыслями"
    picture_link = ""
    closed = False

    fields = [
        {
            'title': "Опишите ситуацию",
            'description': "Факты без мыслей и эмоций.",
            'hint': "Только что случилось такое...",
            'type': FieldType.TEXT,
            'major': True,
            'variants': [],
            'exercises': ['Проблемы и цели', 'Анализ проблемы'],
        },
        {
            'title': "",
            'description': "Запиши сами действия.",
            'hint': "Как ты себя повел?",
            'type': FieldType.TEXT,
            'major': True,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "",
            'description': "Опишите чувства, которые возникли. Оцени их уровень на слайдере ниже.",
            'hint': "Какие чувства вызвала у вас эта ситуация?",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "Автоматические мысли",
            'description': "Опиши как можно подробнее основные мысли, которые пришли в голову в момент стрессовой ситуации.",
            'hint': "Какие мысли были в этот момент?",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "",
            'description': "Запиши аргументы подтверждающие мысли из прошлого пункта",
            'hint': "Что подтверждает эту мысль?",
            'type': FieldType.SLIDER,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "",
            'description': "Запиши контраргументы, показывающие, что эти мысли не совсем корректны и правдивы",
            'hint': "Что опровергает эту мысль?",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "Что думаете про эту ситуацию теперь?",
            'description': "Сформулируйте альтернативные мысли, которые можно противопоставить автоматической мысли, и которые будут соответствовать прошлому пункту",
            'hint': "Сейчас мне...",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "",
            'description': "Опиши как ты себя чувствуешь после дневника",
            'hint': "Какое у вас теперь настроение?",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "Настроение теперь",
            'description': "",
            'hint': "",
            'type': FieldType.SLIDER,
            'major': False,
            'variants': [],
            'exercises': [],
        }
    ]


class Definition_group_problems():
    title = "Определение групп (категорий) проблем"
    description = "Здесь вы определите проблему, над которой хотели бы поработать. Если их несколько, распределите их "\
            "на категории. В таком случае вы сможете вернуться к своему списку позже."
    picture_link = ""
    closed = False

    fields = [
        {
            'title': "В какой сфере вы испытываете трудности?",
            'description': "Например, работа или личная жизнь",
            'hint': "Укажите сферу",
            'type': FieldType.TEXT,
            'major': True,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "Что вы чувствуете по этому поводу?",
            'description': "Одно слово, наиболее ярко, описывающее ваши ощущения",
            'hint': "Укажите эмоцию",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "Чего вы хотите добиться, когда решите свою проблему?",
            'description': "",
            'hint': "Укажите цель",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        }
    ]


class Definition_problems_setting_goals():
    title = "Проблемы и цели"
    description = "А теперь, как из камня высекают фигуру, вы сможете придать четкую форму своей проблеме"
    picture_link = ""
    closed = False

    fields = [
        {
            'title': "Выберите эмоцию, которую испытываете из-за проблемы",
            'description': "",
            'hint': "",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [
                {'title': 'Тревога'},
                {'title': 'Депрессия'},
                {'title': 'Гнев'},
                {'title': 'Нездоровая ревность'},
                {'title': 'Чувство вины'},
                {'title': 'Боль'},
                {'title': 'Стыд'}
            ],
            'exercises': [],
        },
        {
            'title': "Какое событие вызвало у вас эти эмоции",
            'description': "Краткое запишите конкретное событие, которое вызвало у вас такие эмоции",
            'hint': "Опишите его",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "Почему вы испытываете такие эмоции?",
            'description': "Выберите аргумент, который волнует вас больше всего",
            'hint': "Аргумент",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "Цель",
            'description': "",
            'hint': "Укажите цель еще раз, если она изменилась",
            'type': FieldType.TEXT,
            'major': True,
            'variants': [],
            'exercises': [],
        }
    ]


class Problem_analysis():
    title = "Анализ проблемы"
    description = "И вот, проблема перед нами, но что с ней делать? Мы сами себе придумываем требования, которые не "\
            "можем выполнить, из-за чего в итоге переживаем. Здесь вам предстоит описать свою проблему в форме "\
            "требования. А потом, с помощью подсказок вы сможете это требование сделать более гибким. Таким образом, "\
            "вы не загоняете себя в жесткие рамки, которые мешают вам жить, а выбираете "\
            "предпочтения, осознавая их возможное невыполнение."
    picture_link = ""
    closed = False

    fields = [
        {
            'title': "Проблема",
            'description': "",
            'hint': "",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "Цель",
            'description': "",
            'hint': "",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "Проработка",
            'description': "Напишите вашу проблему в с использованием слов «должен – не должен», «следует – не следует», "\
            "'«надо» и «обязан». Непоколибимый закон, который нельзя нарушить",
            'hint': "Догматическое требование...",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "",
            'description': "Это убеждение, в котором мы выражаем свое желание чего-то, но признаем, что это не "\
            "обязательно должно произойти. Используйте для своего требования слова «я предпочитаю», «я желаю», "\
            "«я надеюсь», «я хотел бы», так вы сможете смягчить его",
            'hint': "Гибкое предпочтение...",
            'type': FieldType.TEXT,
            'major': True,
            'variants': [],
            'exercises': [],
        }
    ]


class Testing_beliefs():
    title = "Проверка убеждений"
    description = "Чтобы убедиться в правильности и силе вашего нового здорового убеждения, вам предстоит ответить "\
            "на несколько вопросов. Если после этого ваше новое убеждение показало свою несостоятельность, то стоит "\
            "пройти весь путь заново. Это нормально, ведь мы не обязаны делать все совершенно, особенно, когда мы "\
            "сталкиваемся с чем-то новым. Если вам нужна помощь, обратитесь к психологу, он сможет прояснить для вас "\
            "некоторые моменты"
    picture_link = ""
    closed = False

    fields = [
        {
            'title': "Догматическое требование",
            'description': "Что указывает на реальность данного убеждения? Какие наблюдение и опыт об этом вам говорят?",
            'hint': "Правдиво ли убеждение?",
            'type': FieldType.TEXT,
            'major': True,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "",
            'description': "(Можете использовать следующую форму для проверки «Только потому, что я думаю, что Впишите "\
            "сюда предпосылку, следует ли из этого, что сюда впишите вывод?",
            'hint': "Логично ли убеждение?",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "",
            'description': "Помогает ли вам это убеждение в достижение вашей цели?",
            'hint': "Помогает ли это убеждение?",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "Гибкое убеждение",
            'description': "Что указывает на реальность данного убеждения? Какие наблюдение и опыт об этом вам говорят?",
            'hint': "Правдиво ли убеждение?",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "",
            'description': "(Можете использовать следующую форму для проверки «Только потому, что я думаю, что Впишите "\
            "сюда предпосылку, следует ли из этого, что сюда впишите вывод?",
            'hint': "Логично ли убеждение?",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "",
            'description': "Помогает ли вам это убеждение в достижение вашей цели?",
            'hint': "Помогает ли это убеждение?",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        }
    ]


class Beliefs_analysis():
    title = "Анализ убеждений"
    description = "Ранее вам уже приходилось использовать технику аргументов, чтобы выделить проблему. На этом этапе, "\
            "данная техника поможет вам сформулировать значимые, эмоциональные и сложные аргументов, которые помогут "\
            "отпустить вредные мысли"
    picture_link = ""
    closed = False

    fields = [
        {
            'title': "Догматическое требование",
            'description': "Как я думаю, чувствую и действую, придерживаясь этого убеждения?",
            'hint': "Действие",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "",
            'description': "Что это убеждение мешает мне делать?",
            'hint': "Помехи",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "",
            'description': "Какие результаты я получаю с этим убеждением и нравятся ли мне эти результаты?",
            'hint': "Результаты",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "Гибкое предпочтение",
            'description': "Как я думаю, чувствую и действую, придерживаясь этого убеждения?",
            'hint': "Действие",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "",
            'description': "Что это убеждение мешает мне делать?",
            'hint': "Помехи",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "",
            'description': "Какие результаты я получаю с этим убеждением и нравятся ли мне эти результаты?",
            'hint': "Результаты",
            'type': FieldType.TEXT,
            'major': True,
            'variants': [],
            'exercises': [],
        }
    ]


class Mood_tracker():
    title = "Трекер настроения"
    description = ""
    picture_link = ""
    closed = True

    fields = [
        {
            'title': "Как ты себя чувствуешь?",
            'description': "",
            'hint': "Тест",
            'type': FieldType.SLIDER,
            'major': True,
            'variants': [],
            'exercises': [],
        }
    ]


class Note():
    title = "Заметки"
    description = "Заметки помогают отслеживать, как прошёл день, как себя чувствуешь и так далее"
    picture_link = ""
    closed = True

    fields = [
        {
            'title': "Напиши сюда что-нибудь",
            'description': "",
            'hint': "Тест",
            'type': FieldType.TEXT,
            'major': True,
            'variants': [],
            'exercises': [],
        }
    ]



