from database.enum import FieldType


class Cpt_diary():
    title = "КПТ-дневник"
    description = "Это способ самоонализа, который позволяет отслеживать эмоции и чувства, выявлять взаимосвязи между "\
        "ситуациями и мыслями"
    picture_link = ""
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
            'variants': [
                {'title': 'Не помню'},
                {'title': 'Плохо'},
                {'title': 'Как Макс'}
            ],
        },
        {
            'title': "Какие чувства вызвала у вас эта ситуация",
            'description': "Опиши все чувства, которые возникли. Оцени их уровень на слайдере ниже.",
            'hint': "Тест",
            'type': FieldType.TEXT,
            'major': False,
            'variants': [],
        },
        {
            'title': "Уровень настроения",
            'description': "",
            'hint': "Тест",
            'type': FieldType.SLIDER,
            'major': False,
            'variants': [],
        },
        {
            'title': "Какие были мысли в этот момент?",
            'description': "Опиши как можно подробно основные мысли, которые пришли в голову в момент стрессовой"
                           "ситуации. Это могут быть оскорбительные насмешки, угрызения совести, жизненные убеждения,"
                           "установки и т.д.",
            'hint': "Тест",
            'type': FieldType.TEXT,
            'major': True,
            'variants': [],
        },
        {
            'title': "Что подтверждает эту мысль?",
            'description': "Запиши аргументы, подтверждающие мысли из прошлого пункта",
            'hint': "Тест",
            'type': FieldType.TEXT,
            'major': True,
            'variants': [],
        },
        {
            'title': "Что опровергает эту мысль?",
            'description': "Запиши контраргументы, показывающие, что эти мысли не совсем корректны и правдивы",
            'hint': "Тест",
            'type': FieldType.TEXT,
            'major': True,
            'variants': [],
        },
        {
            'title': "Что ты думаешь об этой ситуации теперь?",
            'description': "Сформулируй альтернативные мысли, которые можно противопоставить автоматической мысли,"
                           "и которые будут соответствовать прошлому пункту",
            'hint': "Тест",
            'type': FieldType.TEXT,
            'major': True,
            'variants': [],
        },
        {
            'title': "Какое у тебя теперь настроение?",
            'description': "Опиши, как ты себя чувствуешь после заполнения дневника",
            'hint': "Тест",
            'type': FieldType.TEXT,
            'major': True,
            'variants': [],
        },
        {
            'title': "Новый уровень",
            'description': "",
            'hint': "Тест",
            'type': FieldType.SLIDER,
            'major': False,
            'variants': [],
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
        }
    ]
