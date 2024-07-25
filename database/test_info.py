class Test_maslach:
    title = "Профессиональное выгорание"
    description = "Профессиональное выгораниe (ПВ), предназначен для измерения основных показателей синдрома профессионального выгорания (перегорания): эмоционального истощения, деперсонализации и редукции профессиональных достижений"
    short_desc = "Опросник профессионального выгорания Маслач MBI/ПВ"
    questions = ["1. Я чувствую себя эмоционально опустошенным.", "2. После работы ячувствую себя как «выжатый лимон».",
                 "3. Утром ячувствую усталость и нежелание идти на работу.",
                 "4. Я хорошо понимаю, что чувствуют мои подчиненные иколлеги, и стараюсь учитывать это в интересах дела.",
                 "5. Я чувствую, что общаюсь с некоторыми подчиненными и коллегами как с предметами (без теплоты и расположения к ним)",
                 "6. Я чувствую себя энергичным иэмоционально воодушевленным.",
                 "7. Я умею находить правильное решение в конфликтных ситуациях, возникающих при общении с коллегами.",
                 "8. Я чувствую угнетенность и апатию.", "9. Я уверен, что моя работа нужна людям.",
                 "10. В последнее время ястал более «черствым» поотношению ктем, скем работаю.",
                 "11. Я замечаю, что моя работа ожесточает меня.", "12. У меня много планов на будущее, и я верю в их осуществление.",
                 "13. Моя работа всё больше меня разочаровывает.", "14. Мне кажется, что я слишком много работаю.",
                 "15. Бывает, что мне действительно безразлично то, что происходит c некоторыми моими подчиненными и коллегами.",
                 "16. Мне хочется уединиться и отдохнуть от всего и всех.",
                 "17. Я легко могу создать атмосферу доброжелательности и сотрудничества в коллективе.",
                 "18. Во время работы я чувствую приятное оживление.", "19. Благодаря своей работе я уже сделал в жизни много действительно ценного.",
                 "20. Я чувствую равнодушие и потерю интереса ко многому, что радовало меня в моей работе.",
                 "21. На работе я спокойно справляюсь с эмоциональными проблемами.",
                 "22. В последнее время мне кажется, что коллеги и подчиненные всё чаще перекладывают на меня груз своих проблем и обязанностей."]

    answers_cnt = 7
    answers = [["Никогда", "Очень редко", "Редко", "Иногда", "Часто", "Очень часто", "Ежедневно"],
               ["Никогда", "Очень редко", "Редко", "Иногда", "Часто", "Очень часто", "Ежедневно"],
               ["Никогда", "Очень редко", "Редко", "Иногда", "Часто", "Очень часто", "Ежедневно"],
               ["Никогда", "Очень редко", "Редко", "Иногда", "Часто", "Очень часто", "Ежедневно"],
               ["Никогда", "Очень редко", "Редко", "Иногда", "Часто", "Очень часто", "Ежедневно"],
               ["Никогда", "Очень редко", "Редко", "Иногда", "Часто", "Очень часто", "Ежедневно"],
               ["Никогда", "Очень редко", "Редко", "Иногда", "Часто", "Очень часто", "Ежедневно"],
               ["Никогда", "Очень редко", "Редко", "Иногда", "Часто", "Очень часто", "Ежедневно"],
               ["Никогда", "Очень редко", "Редко", "Иногда", "Часто", "Очень часто", "Ежедневно"],
               ["Никогда", "Очень редко", "Редко", "Иногда", "Часто", "Очень часто", "Ежедневно"],
               ["Никогда", "Очень редко", "Редко", "Иногда", "Часто", "Очень часто", "Ежедневно"],
               ["Никогда", "Очень редко", "Редко", "Иногда", "Часто", "Очень часто", "Ежедневно"],
               ["Никогда", "Очень редко", "Редко", "Иногда", "Часто", "Очень часто", "Ежедневно"],
               ["Никогда", "Очень редко", "Редко", "Иногда", "Часто", "Очень часто", "Ежедневно"],
               ["Никогда", "Очень редко", "Редко", "Иногда", "Часто", "Очень часто", "Ежедневно"],
               ["Никогда", "Очень редко", "Редко", "Иногда", "Часто", "Очень часто", "Ежедневно"],
               ["Никогда", "Очень редко", "Редко", "Иногда", "Часто", "Очень часто", "Ежедневно"],
               ["Никогда", "Очень редко", "Редко", "Иногда", "Часто", "Очень часто", "Ежедневно"],
               ["Никогда", "Очень редко", "Редко", "Иногда", "Часто", "Очень часто", "Ежедневно"],
               ["Никогда", "Очень редко", "Редко", "Иногда", "Часто", "Очень часто", "Ежедневно"],
               ["Никогда", "Очень редко", "Редко", "Иногда", "Часто", "Очень часто", "Ежедневно"],
               ["Никогда", "Очень редко", "Редко", "Иногда", "Часто", "Очень часто", "Ежедневно"]]

    scales = ["Эмоциональное истощение", "Деперсонализация", "Редукция проф. достижений"]
    scale_limitation = [0, 54, 0, 30, 0, 48]

    borders_cnt = 3
    scale_border = [[0, 15, 16, 24, 25, 54], [0, 5, 6, 10, 11, 30], [0, 30, 31, 36, 37, 48]]
    scale_color = [["#008000", "#E1B92A", "#ff0000"], ["#008000", "#E1B92A", "#ff0000"], ["#ff0000", "#E1B92A", "#008000"]]
    scale_title = [["Ниже нормы", "Умеренный", "Норма"], ["Ниже нормы", "Умеренный", "Норма"], ["Норма", "Умеренный", "Выше нормы"]]

class Test_DASS:
    title = "DASS-21"
    description = "Данный опросник состоит из 21 вопроса о вашем самочувствии. Он поможет оценить ваше состояние за последнее время. Поэтому вспомните своё эмоциональное состояние за последние 2 недели и отметьте нужный вам вариант ответа. В опроснике используется три шкалы самоотчёта: депрессия, тревога и стресс,"
    short_desc = "Шкалы депрессии, тревоги и стресса"
    questions = ["1. Мне было трудно успокоиться", "2. Я чувствовал сухость во рту.",
                 "3. Мне кажется, что я не испытывал никаких позитивных чувств.",
                 "4. У меня были проблемы с дыханием (например, учащенное дыхание, одышка при отсутствии физической активности).",
                 "5. Мне было трудно проявить инициативу для того, чтобы что-то сделать.",
                 "6. Я слишком остро реагировал на некоторые ситуации.",
                 "7. У меня была дрожь (например, в руках).",
                 "8. Я чувствовал, что трачу много нервов.", "9. Меня тревожили ситуации, в которых я мог запаниковать и выглядеть глупо.",
                 "10. Я чувствовал, что мне не на что надеяться.",
                 "11. Я обнаруживал себя взволнованным.", "12. Мне было трудно расслабиться.",
                 "13. Я чувствовал себя унылым и подавленным.", "14. Я был нетерпим ко всему, что мешало мне в моих делах.",
                 "15. Я был близок к панике.",
                 "16. Я не мог ничем увлечься.",
                 "17. Мне казалось, что как человек я ничего не стою.",
                 "18. Я чувствовал, что был довольно обидчив.", "19. Я чувствовал работу своего сердца при отсутствии физической активности (например, ощущение увеличения частоты сердечных сокращений, пропуска сердечных ударов).",
                 "20. Мне было страшно без всякой на то причины.",
                 "21. Мне казалось, что жизнь бессмысленна."]

    answers_cnt = 4
    answers = [["Никогда", "Редко", "Часто", "Почти всегда"],
               ["Никогда", "Редко", "Часто", "Почти всегда"],
               ["Никогда", "Редко", "Часто", "Почти всегда"],
               ["Никогда", "Редко", "Часто", "Почти всегда"],
               ["Никогда", "Редко", "Часто", "Почти всегда"],
               ["Никогда", "Редко", "Часто", "Почти всегда"],
               ["Никогда", "Редко", "Часто", "Почти всегда"],
               ["Никогда", "Редко", "Часто", "Почти всегда"],
               ["Никогда", "Редко", "Часто", "Почти всегда"],
               ["Никогда", "Редко", "Часто", "Почти всегда"],
               ["Никогда", "Редко", "Часто", "Почти всегда"],
               ["Никогда", "Редко", "Часто", "Почти всегда"],
               ["Никогда", "Редко", "Часто", "Почти всегда"],
               ["Никогда", "Редко", "Часто", "Почти всегда"],
               ["Никогда", "Редко", "Часто", "Почти всегда"],
               ["Никогда", "Редко", "Часто", "Почти всегда"],
               ["Никогда", "Редко", "Часто", "Почти всегда"],
               ["Никогда", "Редко", "Часто", "Почти всегда"],
               ["Никогда", "Редко", "Часто", "Почти всегда"],
               ["Никогда", "Редко", "Часто", "Почти всегда"],
               ["Никогда", "Редко", "Часто", "Почти всегда"]]

    scales = ["Стресс", "Тревога", "Депрессия"]
    scale_limitation = [0, 21, 0, 21, 0, 21]

    borders_cnt = 5
    scale_border = [[0, 7, 8, 9, 10, 12, 13, 16, 17, 21], [0, 3, 4, 5, 6, 7, 8, 9, 10, 21], [0, 4, 5, 6, 7, 10, 11, 13, 14, 21]]
    scale_color = [["#008000", "#008000", "#E1B92A", "#ff0000", "#ff0000"], ["#008000", "#008000", "#E1B92A", "#ff0000", "#ff0000"], ["#008000", "#008000", "#E1B92A", "#ff0000", "#ff0000"]]
    scale_title = [["Норма", "Низкий", "Умеренный", "Высокий", "Очень высокий"], ["Норма", "Низкий", "Умеренный", "Высокий", "Очень высокий"], ["Норма", "Низкий", "Умеренный", "Высокий", "Очень высокий"]]

class Test_STAI:
    title = "Шкала тревоги Спилбергера-Ханина, STAI"
    description = "Шкала тревоги, предназначен для измерения основных показателей тревожного состояния"
    short_desc = "Опросник тревожного состояния Спилбергера-Ханина"
    questions = ["1. В данный момент я спокоен.", "2.  В данный момент мне ничто не угрожает.",
                 "3. В данный момент я нахожусь в напряжении.",
                 "4. В данный момент я внутренне скован.",
                 "5. В данный момент я чувствую себя свободно.",
                 "6. В данный момент я расстроен.",
                 "7. В данный момент меня волнуют возможные неудачи.",
                 "8. В данный момент я ощущаю душевный покой.",
                 "9. В данный момент я встревожен.",
                 "10. В данный момент я испытываю чувство внутреннего удовлетворения.",
                 "11. В данный момент я уверен в себе.", "12. В данный момент я нервничаю.",
                 "13. В данный момент я не нахожу себе места.", "14. В данный момент я взвинчен.",
                 "15. В данный момент я не чувствую скованности, напряжения.",
                 "16. В данный момент я доволен.",
                 "17. В данный момент я озабочен",
                 "18. В данный момент я слишком возбужден и мне не по себе.", "19. В данный момент мне радостно.",
                 "20. В данный момент мне приятно.",
                 "21. У меня бывает приподнятое настроение.",
                 "22. Я бываю раздражительным.",
                 "23. Я легко расстраиваюсь.",
                 "24. Я хотел бы быть таким же удачливым, как и другие.",
                 "25. Я сильно переживаю неприятности и долго не могу о них забыть.",
                 "26. Я чувствую прилив сил и желание работать.",
                 "27. Я спокоен, хладнокровен и собран.",
                 "28. Меня тревожат возможные трудности.",
                 "29. Я слишком переживаю из-за пустяков.",
                 "30. Я бываю вполне счастлив.",
                 "31. Я всё принимаю близко к сердцу.",
                 "32. Мне не хватает уверенности в себе.",
                 "33. Я чувствую себя беззащитным.",
                 "34. Я стараюсь избегать критических ситуаций и трудностей.",
                 "35. У меня бывает хандра.",
                 "36. Я бываю доволен.",
                 "37. Всякие пустяки отвлекают и волнуют меня.",
                 "38. Бывает, что я чувствую себя неудачником.",
                 "39. Я уравновешенный человек.",
                 "40. Меня охватывает беспокойство, когда я думаю о своих делах и заботах."]

    answers_cnt = 4
    answers = [["Нет, это не так", "Пожалуй, так", "Верно", "Совершенно верно"],
               ["Нет, это не так", "Пожалуй, так", "Верно", "Совершенно верно"],
               ["Нет, это не так", "Пожалуй, так", "Верно", "Совершенно верно"],
               ["Нет, это не так", "Пожалуй, так", "Верно", "Совершенно верно"],
               ["Нет, это не так", "Пожалуй, так", "Верно", "Совершенно верно"],
               ["Нет, это не так", "Пожалуй, так", "Верно", "Совершенно верно"],
               ["Нет, это не так", "Пожалуй, так", "Верно", "Совершенно верно"],
               ["Нет, это не так", "Пожалуй, так", "Верно", "Совершенно верно"],
               ["Нет, это не так", "Пожалуй, так", "Верно", "Совершенно верно"],
               ["Нет, это не так", "Пожалуй, так", "Верно", "Совершенно верно"],
               ["Нет, это не так", "Пожалуй, так", "Верно", "Совершенно верно"],
               ["Нет, это не так", "Пожалуй, так", "Верно", "Совершенно верно"],
               ["Нет, это не так", "Пожалуй, так", "Верно", "Совершенно верно"],
               ["Нет, это не так", "Пожалуй, так", "Верно", "Совершенно верно"],
               ["Нет, это не так", "Пожалуй, так", "Верно", "Совершенно верно"],
               ["Нет, это не так", "Пожалуй, так", "Верно", "Совершенно верно"],
               ["Нет, это не так", "Пожалуй, так", "Верно", "Совершенно верно"],
               ["Нет, это не так", "Пожалуй, так", "Верно", "Совершенно верно"],
               ["Нет, это не так", "Пожалуй, так", "Верно", "Совершенно верно"],
               ["Нет, это не так", "Пожалуй, так", "Верно", "Совершенно верно"],
               ["Почти никогда", "Иногда", "Часто", "Почти всегда"],
               ["Почти никогда", "Иногда", "Часто", "Почти всегда"],
               ["Почти никогда", "Иногда", "Часто", "Почти всегда"],
               ["Почти никогда", "Иногда", "Часто", "Почти всегда"],
               ["Почти никогда", "Иногда", "Часто", "Почти всегда"],
               ["Почти никогда", "Иногда", "Часто", "Почти всегда"],
               ["Почти никогда", "Иногда", "Часто", "Почти всегда"],
               ["Почти никогда", "Иногда", "Часто", "Почти всегда"],
               ["Почти никогда", "Иногда", "Часто", "Почти всегда"],
               ["Почти никогда", "Иногда", "Часто", "Почти всегда"],
               ["Почти никогда", "Иногда", "Часто", "Почти всегда"],
               ["Почти никогда", "Иногда", "Часто", "Почти всегда"],
               ["Почти никогда", "Иногда", "Часто", "Почти всегда"],
               ["Почти никогда", "Иногда", "Часто", "Почти всегда"],
               ["Почти никогда", "Иногда", "Часто", "Почти всегда"],
               ["Почти никогда", "Иногда", "Часто", "Почти всегда"],
               ["Почти никогда", "Иногда", "Часто", "Почти всегда"],
               ["Почти никогда", "Иногда", "Часто", "Почти всегда"],
               ["Почти никогда", "Иногда", "Часто", "Почти всегда"],
               ["Почти никогда", "Иногда", "Часто", "Почти всегда"]]

    scales = ["Шкала ситуативной тревожности", "Шкала личностной тревожности"]
    scale_limitation = [20, 80, 20, 80]

    borders_cnt = 3
    scale_border = [[20, 30, 31, 44, 45, 80], [20, 30, 31, 44, 45, 80]]
    scale_color = [["#008000", "#E1B92A", "#ff0000"], ["#008000", "#E1B92A", "#ff0000"]]
    scale_title = [["Норма", "Умеренный", "Выше нормы"], ["Норма", "Умеренный", "Выше нормы"]]


class Test_coling_strategy:
    title = "Индикатор копинг-стратегий"
    description = "Опросник Индикатор копинг-стратегий (Coping Strategy Indicator, CSI) предназначен для диагностики оминирующих копинг-стратегий личности. Методика выделяет три группы стратегий: разрешения проблем, поиска социальной поддержки и избегания."
    short_desc = "Опросник Индикатор копинг-стратегий"
    questions = ["1. Позволяю себе поделиться чувством с другом.", "2. Стараюсь все сделать так, чтобы иметь возможность наилучшим образом решить проблему.",
                 "3. Осуществляю поиск всех возможных решений, прежде чем что-то предпринять.",
                 "4. Пытаюсь отвлечься от проблемы.",
                 "5. Принимаю сочувствие и понимание от кого-либо.",
                 "6. Делаю все возможное, чтобы не дать окружающим увидеть, что мои дела плохи.",
                 "7. Обсуждаю ситуацию с людьми, так как обсуждение помогает мне чувствовать себя лучше.",
                 "8. Ставлю для себя ряд целей, позволяющих постепенно справляться с ситуацией.",
                 "9. Очень тщательно взвешиваю возможности выбора.",
                 "10. Мечтаю, фантазирую о лучших временах.",
                 "11. Пытаюсь различными способами решать проблему, пока не найду подходящий.", "12. Доверяю свои страхи родственнику или другу.",
                 "13. Больше времени, чем обычно, провожу один.", "14. Рассказываю другим людям о ситуации, так как только ее обсуждение помогает мне прийти к ее разрешению.",
                 "15. Думаю о том, что нужно сделать, чтобы исправить положение.",
                 "16. Сосредотачиваюсь полностью на решении проблемы.",
                 "17. Обдумываю про себя план действий.",
                 "18. Смотрю телевизор дольше, чем обычно.", "19. Иду к кому-нибудь (другу или специалисту), чтобы он помог мне чувствовать себя лучше.",
                 "20. Стою твердо и борюсь за то, что мне нужно в этой ситуации.",
                 "21. Избегаю общения с людьми.",
                 "22. Переключаюсь на хобби или занимаюсь спортом, чтобы избежать проблем.",
                 "23. Иду к другу за советом - как исправить ситуацию.", "24. Иду к другу, чтобы он помог мне лучше почувствовать проблему.",
                 "25. Принимаю сочувствие, взаимопонимание друзей.", "26. Сплю больше обычного.",
                 "27. Фантазирую о том, что все могло бы быть иначе.",
                 "28. Представляю себя героем книги или кино.",
                 "29. Пытаюсь решить проблему.",
                 "30. Хочу, чтобы люди оставили меня одного.", "31. Принимаю помощь от друзей или родственников.",
                 "32. Ищу успокоения у тех, кто знает меня лучше.",
                 "33. Пытаюсь тщательно планировать свои действия, а не действовать импульсивно под влиянием внешнего побуждения." ]

    answers_cnt = 3
    answers = [["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],
               ["Полностью согласен", "Согласен", "Не согласен"],]

    scales = ["Разрешение проблем", "Поиск социальной поддержки", "Избегание проблем"]
    scale_limitation = [0, 99, 0, 99, 0, 99]

    borders_cnt = 4
    scale_border = [[0, 16, 17, 21, 22, 30, 31, 99], [0, 13, 14, 18, 19, 28, 29, 99], [0, 15, 16, 23, 24, 26, 27, 99]]
    scale_color = [["#ff0000", "#FFA500", "#E1B92A", "#008000"], ["#ff0000", "#FFA500", "#E1B92A", "#008000"], ["#ff0000", "#FFA500", "#E1B92A", "#008000"]]
    scale_title = [["Очень низкий", "Низкий", "Средний", "Высокий"], ["Очень низкий", "Низкий", "Средний", "Высокий"], ["Очень низкий", "Низкий", "Средний", "Высокий"]]


class Test_cmq:
    title = "Опросник когнтитвных ошибок CMQ"
    description = "Перед вами Опросник когнтитвных ошибок CMQ. Этот опросник разработан для использования в рамках когнитивно-поведенческой терапии и нацелен на обнаружение когнитивных искажений – ошибок суждений, связанных с неправильной интерпретацией смысловых контекстов. Как инструмент самооценки, опросник был опубликован в книге А. Фримана «Десять глупейших ошибок, которые совершают люди» для широкого круга читателей."
    short_desc = "Перед вами Опросник когнтитвных ошибок CMQ"
    questions = ["1. Я слишком бурно реагирую даже на самые мелкие проблемы.", "2. Мне говорят, что я делаю из мухи слона.",
                 "3. Я легко прихожу в возбуждение.",
                 "4. Не стоит даже пробовать, всё равно ничего не получится.",
                 "5. Я заранее знаю, что всё будет плохо.",
                 "6. Я могу точно сказать, о чем думают другие.",
                 "7. Мои близкие должны знать, чего я хочу.",
                 "8. Всегда можно определить, что думает человек, понаблюдав за его жестами и мимикой.",
                 "9. Я полагаю, что, когда люди проводят много времени вместе, они настраиваются на мысли друг друга.",
                 "10. Я расстраиваюсь из-за того, что, как мне кажется, думает другой человек, а потом оказывается, что я был не прав.",
                 "11. Я в ответе за то, чтобы любимые мною люди были счастливы.", "12. Если что-то не получается, я чувствую, что это моя вина.",
                 "13. Меня критикуют чаще, чем других людей.", "14. Я всегда могу определить, когда человек нападает именно на меня, даже если он не упоминает моего имени.",
                 "15. Я чувствую, что меня несправедливо обвиняют в том, что находится вне моего контроля.",
                 "16. Люди сознательно затрагивают именно те области, в которых я особенно чувствителен к критике.",
                 "17. В отношении критики у меня действует шестое чувство, я всегда угадываю, когда говорят обо мне.",
                 "18. Негативные замечания ранят меня по-настоящему, иногда я впадаю в депрессивное состояние.", "19. Я слышу только негативные замечания и часто не замечаю похвалы.",
                 "20. Я полагаю, что все замечания означают одно и то же, им одна негативная цена.",
                 "21. Я расстраиваюсь, если мне не удается завершить дело.",
                 "22. Если обо мне говорят, что я такой же, как все, или один из многих, я чувствую себя оскорбленным.",
                 "23. Лучше я ничего не буду делать, чем возьмусь за работу ниже моего достоинства.", "24. Для меня очень важно, чтобы люди воспринимали меня как человека, ни на йоту не отступающего от стандарта безупречности.",
                 "25. Даже самая незначительная ошибка может испортить мне весь день и даже всю жизнь.", "26. По сравнению с другими я неудачник.",
                 "27. Во мне силен дух соревнования.",
                 "28. Я расстраиваюсь, когда слышу об успехах других людей.",
                 "29. Я падаю духом оттого, что нахожусь не там, где должен быть.",
                 "30. Мне кажется, что если хочешь добиться успеха, то надо постоянно сравнивать себя с другими.", "31. Мир, знаете ли, очень опасное место.",
                 "32. Если не хочешь иметь неприятности, соблюдай осторожность в словах и делах.",
                 "33. Не люблю пользоваться случаем.",
                 "34. Я упустил хорошую возможность, потому что опасался рисковать.",
                 "35. Я избегаю предпринимать какие-то действия из-за боязни травмы и неудачи.",
                 "36. Я испытываю чувство вины из-за того, что должен был сделать что-то в прошлом, но не сделал.",
                 "37. Я считаю, что надо жить по правилам.",
                 "38. Оглядываясь на прожитую жизнь, я вижу больше неудач, нежели успехов.",
                 "39. На меня давит необходимость поступать правильно.",
                 "40. Меня угнетает необходимость сделать все дела.",
                 "41. Мне безразлично мнение окружающих.",
                 "42. Люди упрекают меня в том, что я не умею слушать.",
                 "43. Когда меня просят что-то сделать, я бываю недовольным, ершистым.",
                 "44. Я считаю, что все должно делаться по-моему или не делаться вовсе.",
                 "45. Я склонен откладывать очень важные дела и бываю очень медлительным." ]

    answers_cnt = 4
    answers = [["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],
               ["Никогда", "Иногда", "Часто", "Всегда"],]

    scales = ["Персонализация", "Чтение мыслей", "Упрямство", "Морализация", "Катастрофизация", "Выученная беспомощность", "Максимализм", "Преувеличение опасности", "Гипернормативность"]
    scale_limitation = [0, 180, 0, 180, 0, 180, 0, 180, 0, 180, 0, 180, 0, 180, 0, 180, 0, 180]

    borders_cnt = 2
    scale_border = [[0, 93, 94, 180], [0, 93, 94, 180], [0, 93, 94, 180], [0, 93, 94, 180], [0, 93, 94, 180], [0, 93, 94, 180], [0, 93, 94, 180], [0, 93, 94, 180], [0, 93, 94, 180]]
    scale_color = [["#008000", "#ff0000"], ["#008000", "#ff0000"], ["#008000", "#ff0000"], ["#008000", "#ff0000"], ["#008000", "#ff0000"],
                   ["#008000", "#ff0000"], ["#008000", "#ff0000"], ["#008000", "#ff0000"], ["#008000", "#ff0000"]]
    scale_title = [["Умеренно выражено и не мешает жить", "Есть когнтитвные ошибки"], ["Умеренно выражено и не мешает жить", "Есть когнтитвные ошибки"],
                   ["Умеренно выражено и не мешает жить", "Есть когнтитвные ошибки"], ["Умеренно выражено и не мешает жить", "Есть когнтитвные ошибки"],
                   ["Умеренно выражено и не мешает жить", "Есть когнтитвные ошибки"], ["Умеренно выражено и не мешает жить", "Есть когнтитвные ошибки"],
                   ["Умеренно выражено и не мешает жить", "Есть когнтитвные ошибки"], ["Умеренно выражено и не мешает жить", "Есть когнтитвные ошибки"],
                   ["Умеренно выражено и не мешает жить", "Есть когнтитвные ошибки"]]


class Test_bek21:
    title = "Шкала депрессии Бека"
    description = "Шкала депрессии Бека (Beck Depression Inventory, BDI) – методика диагностики депрессивных состояний, разработанная американским психотерапевтом Аароном Беком на основе клинических наблюдений, позволивших выявить ограниченный набор наиболее релевантных и значимых симптомов депрессии и наиболее часто предъявляемых пациентами жалоб."
    short_desc = "Шкала депрессии Бека, BDI"
    questions = ["1. Что лучше описывает ваше состояние за прошедшую неделю и сегодня?", "2. Что лучше описывает ваше состояние за прошедшую неделю и сегодня?",
                 "3. Что лучше описывает ваше состояние за прошедшую неделю и сегодня?",
                 "4. Что лучше описывает ваше состояние за прошедшую неделю и сегодня?",
                 "5. Что лучше описывает ваше состояние за прошедшую неделю и сегодня?",
                 "6. Что лучше описывает ваше состояние за прошедшую неделю и сегодня?",
                 "7. Что лучше описывает ваше состояние за прошедшую неделю и сегодня?",
                 "8. Что лучше описывает ваше состояние за прошедшую неделю и сегодня?", "9. Что лучше описывает ваше состояние за прошедшую неделю и сегодня?",
                 "10. Что лучше описывает ваше состояние за прошедшую неделю и сегодня?",
                 "11. Что лучше описывает ваше состояние за прошедшую неделю и сегодня?", "12. Что лучше описывает ваше состояние за прошедшую неделю и сегодня?",
                 "13. Что лучше описывает ваше состояние за прошедшую неделю и сегодня?", "14. Что лучше описывает ваше состояние за прошедшую неделю и сегодня?",
                 "15. Что лучше описывает ваше состояние за прошедшую неделю и сегодня?",
                 "16. Что лучше описывает ваше состояние за прошедшую неделю и сегодня?",
                 "17. Что лучше описывает ваше состояние за прошедшую неделю и сегодня?",
                 "18. Что лучше описывает ваше состояние за прошедшую неделю и сегодня?",
                 "19. Что лучше описывает ваше состояние за прошедшую неделю и сегодня?",
                 "20. Что лучше описывает ваше состояние за прошедшую неделю и сегодня?",
                 "21. Что лучше описывает ваше состояние за прошедшую неделю и сегодня?"]

    answers_cnt = 4
    answers = [["Я не чувствую себя несчастным", "Я чувствую себя несчастным", "Я всё время несчастен и не могу освободиться от этого чувства", "Я настолько несчастен и опечален, что не могу этого вынести"],
               ["Думая о будущем, я не чувствую себя особенно разочарованным", "Думая о будущем, я чувствую себя разочарованным", "Я чувствую, что мне нечего ждать в будущем", "Я чувствую, что будущее безнадежно и ничто не изменится к лучшему"],
               ["Я не чувствую себя неудачником", "Я чувствую, что у меня было больше неудач, чем у большинства других людей", "Когда я оглядываюсь на прожитую жизнь, всё, что я вижу, это череда неудач", "Я чувствую себя полным неудачником"],
               ["Я получаю столько же удовольствия от жизни, как и раньше", "Я не получаю столько же удовольствия от жизни, как раньше", "Я не получаю настоящего удовлетворения от чего бы то ни было", "Я всем не удовлетворен, и мне всё надоело"],
               ["Я не чувствую себя особенно виноватым", "Довольно часто я чувствую себя виноватым", "Почти всегда я чувствую себя виноватым", "Я чувствую себя виноватым всё время"],
               ["Я не чувствую, что меня за что-то наказывают", "Я чувствую, что могу быть наказан за что-то", "Я ожидаю, что меня накажут", "Я чувствую, что меня наказывают за что-то"],
               ["Я не испытываю разочарования в себе", "Я разочарован в себе", "Я внушаю себе отвращение", "Я ненавижу себя"],
               ["У меня нет чувства, что я в чем-то хуже других", "Я самокритичен и признаю свои слабости и ошибки", "Я всё время виню себя за свои ошибки", "Я виню себя за всё плохое, что происходит"],
               ["У меня нет мыслей о том, чтобы покончить с собой", "У меня есть мысли о том, чтобы покончить с собой, но я этого не сделаю", "Я хотел бы покончить жизнь самоубийством", "Я бы покончил с собой, если бы представился удобный случай"],
               ["Я плачу не больше, чем обычно", "Сейчас я плачу больше обычного", "Я теперь всё время плачу", "Раньше я еще мог плакать, но теперь не смогу, даже если захочу"],
               ["Сейчас я не более раздражен, чем обычно", "Я раздражаюсь легче, чем раньше, даже по пустякам", "Сейчас я всё время раздражен", "Меня уже ничто не раздражает, потому что всё стало безразлично"],
               ["Я не потерял интереса к другим людям", "У меня меньше интереса к другим людям, чем раньше", "Я почти утратил интерес к другим людям", "Я потерял всякий интерес к другим людям"],
               ["Я способен принимать решения так же, как всегда", "Я откладываю принятие решений чаще, чем обычно", "Я испытываю больше трудностей в принятии решений, чем прежде", "Я больше не могу принимать каких-либо решений"],
               ["Я не чувствую, что я выгляжу хуже, чем обычно", "Я обеспокоен тем, что выгляжу постаревшим или непривлекательным", "Я чувствую, что изменения, происшедшие в моей внешности, сделали меня непривлекательным", "Я уверен, что выгляжу безобразным"],
               ["Я могу работать так же, как раньше", "Мне надо приложить дополнительные усилия, чтобы начать что-либо делать", "Я с большим трудом заставляю себя что-либо делать", "Я вообще не могу работать"],
               ["Я могу спать так же хорошо, как и обычно", "Я сплю не так хорошо, как всегда", "Я просыпаюсь на 1-2 часа раньше, чем обычно и с трудом могу заснуть снова", "Я просыпаюсь на несколько часов раньше обычного и не могу снова заснуть"],
               ["Я устаю не больше обычного", "Я устаю легче обычного", "Я устаю почти от всего того, что я делаю", "Я слишком устал, чтобы делать что бы то ни было"],
               ["Мой аппетит не хуже, чем обычно", "У меня не такой хороший аппетит, как был раньше", "Сейчас мой аппетит стал намного хуже", "Я вообще потерял аппети"],
               ["Если в последнее время я и потерял в весе, то очень немного", "Я потерял в весе более 2 кг", "Я потерял в весе более 4 кг", "Я потерял в весе более 6 кг"],
               ["Я беспокоюсь о своем здоровье не больше, чем обычно", "Меня беспокоят такие проблемы, как различные боли, расстройства желудка, запоры", "Я настолько обеспокоен своим здоровьем, что мне даже трудно думать о чем-нибудь другом", "Я до такой степени обеспокоен своим здоровьем, что вообще ни о чем другом не могу думать"],
               ["Я не замечал каких-либо изменений в моих сексуальных интересах", "Я меньше, чем обычно интересуюсь сексом", "Сейчас я намного меньше интересуюсь сексом", "Я совершенно утратил интерес к сексу"]]

    scales = ["Шкала депрессии"]
    scale_limitation = [0, 63]

    borders_cnt = 5
    scale_border = [[0, 9, 10, 15, 16, 19, 20, 29, 30, 63]]
    scale_color = [["#008000", "#5BAEC0", "#FFA500", "#9B2D30", "#ff0000"]]
    scale_title = [["Отсутствие депрессивных симптомов", "Легкая депрессия (субдепрессия)", "Умеренная депрессия", "Выраженная депрессия (средней тяжести)", "Тяжелая депрессия"]]


class Test_jas:
    title = "Шкала профессиональной апатии"
    description = "Шкала профессиональной апатии (Job Apathy Scale, JAS) позволяет измерять возникающие в профессиональной деятельности апатичные мысли (отсутствие интереса и эмоциональной приверженности к работе в организации) и апатичные действия (отсутствие стремления к реализации действий, необходимых для успешного решения рабочих задач)."
    short_desc = "Шкала профессиональной апатии (Job Apathy Scale, JAS)"
    questions = ["1. Мне трудно чем-либо мотивировать себя в работе.", "2. Я безразличен к своей работе.",
                 "3. Я не испытываю интеллектуального вовлечения в свою работу.",
                 "4. Я эмоционально отстранен от своей работы.",
                 "5. Мое отношение к работе можно охарактеризовать как пассивное.",
                 "6. Если я сразу не найду чего-то, что необходимо для выполнения рабочего задания, то достаточно быстро прекращу поиски.",
                 "7. Хотя я и выполняю всё, что мне поручено, я обычно не работаю усерднее, чем необходимо.",
                 "8. Работа с результатом среднего качества кажется мне вполне допустимой.",
                 "9. Когда появляются новые рабочие задачи, я не возражаю, если за них берутся другие.",
                 "10. Обычно я не проявляю инициативу, когда начальство распределяет задания."]

    answers_cnt = 4
    answers = [["Не согласен", "Скорее не согласен", "Нечто среднее", "Скорее согласен", "Согласен"],
               ["Не согласен", "Скорее не согласен", "Нечто среднее", "Скорее согласен", "Согласен"],
               ["Не согласен", "Скорее не согласен", "Нечто среднее", "Скорее согласен", "Согласен"],
               ["Не согласен", "Скорее не согласен", "Нечто среднее", "Скорее согласен", "Согласен"],
               ["Не согласен", "Скорее не согласен", "Нечто среднее", "Скорее согласен", "Согласен"],
               ["Не согласен", "Скорее не согласен", "Нечто среднее", "Скорее согласен", "Согласен"],
               ["Не согласен", "Скорее не согласен", "Нечто среднее", "Скорее согласен", "Согласен"],
               ["Не согласен", "Скорее не согласен", "Нечто среднее", "Скорее согласен", "Согласен"],
               ["Не согласен", "Скорее не согласен", "Нечто среднее", "Скорее согласен", "Согласен"],
               ["Не согласен", "Скорее не согласен", "Нечто среднее", "Скорее согласен", "Согласен"]]

    scales = ["Шкала профессиональной апатии"]
    scale_limitation = [10, 50]

    borders_cnt = 3
    scale_border = [[10, 17, 18, 32, 33, 50]]
    scale_color = [["#008000", "#E1B92A", "#ff0000"]]
    scale_title = [["Низкий уровень", "Средний уровень", "Высокий уровень"]]
