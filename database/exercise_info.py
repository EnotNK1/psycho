from database.enum import FieldType


class Cpt_diary():
    title = "КПТ-дневник"
    description = "Это способ самоанализа, который позволяет отслеживать эмоции и чувства, выявлять взаимосвязи между "\
        "ситуациями и мыслями"
    picture_link = ""
    fields_has_description = True
    closed = False

    fields = [
        {
            'title': "Опиши ситуацию",
            'description': "Запиши факты, без мыслей и эмоций.",
            'hint': "Тест",
            'type': FieldType.TEXT,
            'major': True,
            'variants': [],
        },
        {
            'title': "Как ты себя повел?",
            'description': "Запиши сами действия.",
            'hint': "Тест",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "Какие чувства вызвала у вас эта ситуация",
            'description': "Опишите чувства, которые возникли. Оцени их уровень на слайдере ниже.",
            'hint': "Тест",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "Уровень настроения",
            'description': "",
            'hint': "Тест",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "Какие были мысли в этот момент?",
            'description': "Опиши как можно подробно основные мысли, которые пришли в голову в момент стрессовой"
                            "ситуации. Это могут быть оскорбительные насмешки, угрызения совести, жизненные убеждения,"
                            "установки и т.д.",
            'hint': "Тест",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "Что подтверждает эту мысль?",
            'description': "Запиши аргументы, подтверждающие мысли из прошлого пункта",
            'hint': "Тест",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "Что опровергает эту мысль?",
            'description': "Запиши контраргументы, показывающие, что эти мысли не совсем корректны и правдивы",
            'hint': "Тест",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "Что ты думаешь об этой ситуации теперь?",
            'description': "Сформулируй альтернативные мысли, которые можно противопоставить автоматической мысли,"
                            "и которые будут соответствовать прошлому пункту",
            'hint': "Тест",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "Какое у тебя теперь настроение?",
            'description': "Опиши, как ты себя чувствуешь после заполнения дневника",
            'hint': "Тест",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "Новый уровень",
            'description': "",
            'hint': "Тест",
            'type': FieldType.SLIDER,
            'major': False,
            'variants': [],
            'exercises': [],
        }
    ]


class Definition_group_problems():
    title = "Определение групп проблем"
    description = "Здесь вы определите проблему, над которой хотели бы поработать. Если их несколько, распределите их "\
            "на категории. В таком случае вы сможете вернуться к своему списку позже"
    picture_link = ""
    fields_has_description = False
    closed = True

    fields = [
        {
            'title': "В какой сфере вы испытываете трудности?",
            'description': "Например, работа или личная жизнь",
            'hint': "Укажите сферу",
            'type': FieldType.TEXT,
            'major': True,
            'variants': [],
            'exercises': ["Проблемы и цели"],
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
    fields_has_description = False
    closed = True

    fields = [
        {
            'title': "Выберите сферу, в которой испытываете трудности",
            'description': "",
            'hint': "",
            'type': FieldType.CHOICE,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "Выберите эмоцию, которую испытывали в той ситуации",
            'description': "",
            'hint': "",
            'type': FieldType.CHOICE,
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
            'title': "Какое событие вызвало эти эмоции?",
            'description': "",
            'hint': "Опишите его",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
            'exercises': [],
        },
        {
            'title': "Почему вы испытывали такие эмоции?",
            'description': "Выберите аргумент, который волнует вас больше всего",
            'hint': "Проаргументируйте",
            'type': FieldType.SELECTION,
            'major': False,
            'variants': [],
            'exercises': ["Анализ проблемы"],
        },
        {
            'title': "Цель",
            'description': "",
            'hint': "Уточните свою цель",
            'type': FieldType.TEXT,
            'major': True,
            'variants': [],
            'exercises': ["Анализ проблемы", "Проверка убеждений", "Анализ убеждений"],
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
    fields_has_description = True
    closed = True

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
    fields_has_description = True
    closed = True

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
    fields_has_description = True
    closed = True

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
    closed = False

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
    closed = False

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



