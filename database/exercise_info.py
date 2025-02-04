from database.enum import FieldType

class Cpt_diary():
    title = "КПТ-дневник"
    description = "Это способ самоонализа, который позволяет отслеживать эмоции и чувства, выявлять взаимосвязи между "\
    "ситуациями и мыслями"
    picture_link = ""

    fields = [
        {
            'title': "Опиши ситуацию",
            'description': "Запиши факты, без мыслей и эмоций.",
            'type': FieldType.TEXT,
            'major': True,
        },
        {
            'title': "Как ты себя повел?",
            'description': "Запиши сами действия.",
            'type': FieldType.TEXT,
            'major': False,
        },
        {
            'title': "Какие чувства вызвала у вас эта ситуация",
            'description': "Опиши все чувства, которые возникли. Оцени их уровень на слайдере ниже.",
            'type': FieldType.TEXT,

            'major': False,
        },
        {
            'title': "Уровень настроения",
            'description': "",
            'type': FieldType.SLIDER,
            'major': False,
        },
        {
            'title': "Какие были мысли в этот момент?",
            'description': "Опиши как можно подробно основные мысли, которые пришли в голову в момент стрессовой" \
                           "ситуации. Это могут быть оскорбительные насмешки, угрызения совести, жизненные убеждения," \
                           "установки и т.д.",
            'type': FieldType.TEXT,
            'major': True,
        },
        {
            'title': "Что подтверждает эту мысль?",
            'description': "Запиши аргументы, подтверждающие мысли из прошлого пункта",
            'type': FieldType.TEXT,
            'major': True,
        },
        {
            'title': "Что опровергает эту мысль?",
            'description': "Запиши контраргументы, показывающие, что эти мысли не совсем корректны и правдивы",
            'type': FieldType.TEXT,
            'major': True,
        },
        {
            'title': "Что ты думаешь об этой ситуации теперь?",
            'description': "Сформулируй альтернативные мысли, которые можно противопоставить автоматической мысли," \
                           "и которые будут соответствовать прошлому пункту",
            'type': FieldType.TEXT,
            'major': True,
        },
        {
            'title': "Какое у тебя теперь настроение?",
            'description': "Опиши, как ты себя чувствуешь после заполнения дневника",
            'type': FieldType.TEXT,
            'major': True,
        },
        {
            'title': "Новый уровень",
            'description': "",
            'type': FieldType.SLIDER,
            'major': False,
        }
    ]

class Mood_tracker():
    title = "Трекер настроения"
    description = ""
    picture_link = ""

    fields = [
        {
            'title': "Как ты себя чувствуешь?",
            'description': "",
            'type': FieldType.SLIDER,
            'major': True,
        }
    ]

class Note():
    title = "Заметки"
    description = "Заметки помогают отслеживать, как прошёл день, как себя чувствуешь и так далее"
    picture_link = ""

    fields = [
        {
            'title': "Напиши сюда что-нибудь",
            'description': "",
            'type': FieldType.TEXT,
            'major': True,
        }
    ]