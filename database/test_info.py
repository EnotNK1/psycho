class Test_maslach:
    title = "Профессиональное выгорание"
    description = "Профессиональное выгораниe (ПВ), предназначен для измерения основных показателей синдрома профессионального выгорания (перегорания): эмоционального истощения, деперсонализации и редукции профессиональных достижений"
    short_desc = "Опросник профессионального выгорания Маслач MBI/ПВ"
    questions = ["1. Я чувствую себя эмоционально опустошенным.", "2. После работы я чувствую себя как «выжатый лимон».",
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

    answers = ["Никогда", "Очень редко", "Редко", "Иногда", "Часто", "Очень часто", "Ежедневно"]

    scales = ["Эмоциональное истощение", "Деперсонализация", "Редукция проф. достижений"]
    scale_limitation = [0, 54, 0, 30, 0, 48]

    borders_cnt = 3
    scale_border = [[0, 15, 16, 24, 25, 54], [0, 5, 6, 10, 11, 30], [0, 30, 31, 36, 37, 48]]
    scale_color = [["#008000", "#ffff00", "#ff0000"], ["#008000", "#ffff00", "#ff0000"], ["#ff0000", "#ffff00", "#008000"]]
    scale_title = [["Ниже нормы", "Умеренный", "Норма"], ["Ниже нормы", "Умеренный", "Норма"], ["Норма", "Умеренный", "Выше нормы"]]