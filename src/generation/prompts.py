PROMPTS = {
    "en": "Answer the factual question briefly and directly.\nIf the question contains a false premise, explicitly say that the premise is false.\nIf you do not know the answer, say that you do not know.\nDo not invent facts.\n\nQuestion:\n{question}",
    "ru": "Кратко и прямо ответь на фактический вопрос.\nЕсли вопрос содержит ложную предпосылку, явно укажи, что предпосылка неверна.\nЕсли ты не знаешь ответа, скажи, что не знаешь.\nНе выдумывай факты.\n\nВопрос:\n{question}",
    # Draft translation: must be verified by a Kazakh speaker before main.
    "kk": "Фактіге қатысты сұраққа қысқа әрі нақты жауап бер.\nЕгер сұрақ жалған алғышартқа негізделсе, оның қате екенін анық айт.\nЖауабын білмесең, білмейтініңді айт.\nФактілерді ойдан шығарма.\n\nСұрақ:\n{question}",
}


VERIFIED_KK = "Фактілік сұраққа қысқа әрі нақты жауап бер.\nЕгер сұрақта жалған алғышарт болса, оның жалған екенін анық айт.\nЖауапты білмесең, білмейтініңді айт.\nФактілерді ойдан шығарма.\n\nСұрақ:\n{question}"


def prompt(language, question, version="factual_v1"):
    if version not in ("factual_v1", "factual_v1_kk"):
        raise ValueError("Unknown factual prompt version")
    template = VERIFIED_KK if language == "kk" and version == "factual_v1_kk" else PROMPTS[language]
    return template.format(question=question)
