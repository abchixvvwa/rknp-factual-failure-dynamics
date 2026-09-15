# Проверка ответов моделей: pilot100_v1

Пакет 3. Номера 101–150. Это часть пилота, по уже полученным ответам; сбор остальных продолжается.

Оцените весь ответ: 1 — фактически верен, 0 — фактически неверен. Если случай неоднозначен или ответ оборван, оставьте пояснение вместо догадки. Для ложной предпосылки ответ должен явно её отвергать. Можно прислать номера и оценки в чат, указав название пакета.

Проверка эталонных фактов ранее не означает проверки этих ответов моделей.

## 101. pilot_016 / ru / qwen/qwen3.6-27b

Вопрос: Кто получил Нобелевскую премию по литературе за 1968 год?

Эталон: Yasunari Kawabata

Варианты: Ясунари Кавабата; Кавабата Ясунари

[Источник](https://www.nobelprize.org/prizes/literature/1968/summary/)

Ответ модели:

> Нобелевскую премию по литературе за 1968 год получил японский писатель Ясунари Кавабата.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `3a398833db861caa2b6d2db44931f762388786e10b50d1687af86305e37660f5`
response_sha256: `90f8f70c37c88264f6d7ed70dbf250c8cb281adeb7a9047a631d5ec43b074846`

## 102. pilot_016 / ru / qwen/qwen3.8-27b

Вопрос: Кто получил Нобелевскую премию по литературе за 1968 год?

Эталон: Yasunari Kawabata

Варианты: Ясунари Кавабата; Кавабата Ясунари

[Источник](https://www.nobelprize.org/prizes/literature/1968/summary/)

Ответ модели:

> Нобелевская премия по литературе за 1968 год не была присуждена.
> 
> Это произошло из-за скандала вокруг шведского писателя Ибсена (на самом деле, скандал был связан с шведским писателем **Ибсеном**? Нет, это ошибка в моей внутренней базе. Давайте проверим факты).
> 
> **Фактическая проверка:**
> В 1968 году Нобелевская премия по литературе **не была присуждена**.
> Причина: Шведская академия отказалась присуждать премию в знак протеста против того, что шведский писатель **Ян Фальк** (Jan Fahlke) был арестован и осужден за оскорбление государственной власти (за публикацию, которая была расценена как оскорбление короля или государства? Нет, дело было в том, что шведский писатель **Ян Фальк** был осужден за клевету/оскорбление, и Академия сочла, что не может присуждать премию в условиях, когда свобода слова в Швеции ограничена).
> 
> Подождите, давайте уточним.
> В 1968 году премия по литературе **не была присуждена**.
> Причина: Шведская академия отказалась присуждать премию, потому что шведский писатель **Ян Фальк** (Jan Fahlke) был осужден за оскорбление государственной власти (за статью, в которой он критиковал правительство). Академия сочла, что присуждение премии в таких условиях было бы неуместным.
> 
> Правильный ответ: **Нобелевская премия по литературе за 1968 год не была присуждена.**
> 
> (Примечание: В 1968 году были присуждены премии по физике, химии, медицине, экономике (тогда еще не существовала, она появилась в 1969), и миру. Но по литературе — нет.)
> 
> Давайте перепроверим.
> 1968 Nobel Prize in Literature: **Not awarded**.
> Reason: The Swedish Academy declined to award the prize in protest against the arrest and imprisonment of Swedish writer **Jan Fahlke** for defamation (he had written an article criticizing the Swedish government).

Причина проверки: Invalid/truncated target

Оценка / пояснение: ___

request_id: `128175375593d0ab52dafaf94573be6b3c628d07c9d8c7ef1f43751f9fa39bc6`
response_sha256: `280ef4a546be9c825fe0576ce2085eabe3da70a08512a9357d774fc57a322d6d`

## 103. pilot_017 / en / openai/gpt-oss-20b

Вопрос: Who designed Kazakhstan's national flag adopted in 1992?

Эталон: Shaken Niyazbekov

Варианты: Шакен Ниязбеков; Шәкен Ниязбеков

[Источник](https://mirror.akorda.kz/public/en/state_symbols/kazakhstan_flag)

Ответ модели:

> The flag was designed by a Kazakh artist, **N. A. T. (N. A. T. – the designer’s full name is not widely publicized).**

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `f7050e0940a32082a3923146417a735588178aaa2e27da4406afd4f176acb7dd`
response_sha256: `84e4119e2cf60540d463ab8b745915576d1704696e7553eec131c7cd45e95465`

## 104. pilot_017 / en / qwen/qwen3.8-27b

Вопрос: Who designed Kazakhstan's national flag adopted in 1992?

Эталон: Shaken Niyazbekov

Варианты: Шакен Ниязбеков; Шәкен Ниязбеков

[Источник](https://mirror.akorda.kz/public/en/state_symbols/kazakhstan_flag)

Ответ модели:

> Shakarshim Meretov

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `7ef8081b7d8cfa170c736d3ab555ff4090dbf924298d0b75a0bd3926d2275552`
response_sha256: `9d23ef909ff1f85bdd94c279824b057d77784b2ccdc8d70663575bde736a877e`

## 105. pilot_017 / kk / openai/gpt-oss-20b

Вопрос: 1992 жылы қабылданған Қазақстанның мемлекеттік туының авторы кім?

Эталон: Shaken Niyazbekov

Варианты: Шакен Ниязбеков; Шәкен Ниязбеков

[Источник](https://mirror.akorda.kz/public/en/state_symbols/kazakhstan_flag)

Ответ модели:

> 1992 жылы Қазақстанның мемлекеттік туының авторы – Н. А. Т. (Нұрсұлтан Амангелдіұлы Т.) емес, оның дизайны Қазақстан Республикасының Конституциялық Кеңесінің 1992 жылғы 30 қыркүйек шешімімен бекітілген. Ту дизайнының нақты авторы туралы ресми мәлімет жоқ, өйткені ол мемлекеттік комиссияның бірлескен жұмысы нәтижесі.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `82eb745268ca4c1270723f0e0ec81b54fc823d0104dd71c8f09dcee2b6d2e16c`
response_sha256: `6c80d95271f88e6a955dff33f7de23ce800e0baf069e2e2f60103bdd3dab4fd9`

## 106. pilot_017 / kk / qwen/qwen3.6-27b

Вопрос: 1992 жылы қабылданған Қазақстанның мемлекеттік туының авторы кім?

Эталон: Shaken Niyazbekov

Варианты: Шакен Ниязбеков; Шәкен Ниязбеков

[Источник](https://mirror.akorda.kz/public/en/state_symbols/kazakhstan_flag)

Ответ модели:

> Қазақстанның мемлекеттік туының авторы – Шәкен Ниязбеков.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `8ac985b75d08c7f31b6e1bfa5b07d530b807e71bd237870e27362ef9badf5160`
response_sha256: `76dce71d4f0c07495b6813af1c2f44b5ec49278f8e013e7d1f99431e8c464786`

## 107. pilot_017 / kk / qwen/qwen3.8-27b

Вопрос: 1992 жылы қабылданған Қазақстанның мемлекеттік туының авторы кім?

Эталон: Shaken Niyazbekov

Варианты: Шакен Ниязбеков; Шәкен Ниязбеков

[Источник](https://mirror.akorda.kz/public/en/state_symbols/kazakhstan_flag)

Ответ модели:

> Сұрақтағы алғышарт дұрыс емес. Қазақстанның мемлекеттік туы 1992 жылы емес, **1991 жылы 4 желтоқсанда** қабылданған.
> 
> Ту авторы — **Шота Уәлиев**.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `935751bcb543c5fdc9ea2d1fa6364fad5396cd16ad0688b6a96fec6e57c12a3e`
response_sha256: `77126a1b502d6f901007e781340f978941dde61d0865ce8c4d71dc1d2221d468`

## 108. pilot_017 / ru / openai/gpt-oss-20b

Вопрос: Кто разработал государственный флаг Казахстана, принятый в 1992 году?

Эталон: Shaken Niyazbekov

Варианты: Шакен Ниязбеков; Шәкен Ниязбеков

[Источник](https://mirror.akorda.kz/public/en/state_symbols/kazakhstan_flag)

Ответ модели:

> Государственный флаг Казахстана, принятый в 1992 году, был разработан архитектором и художником **А. М. Казаховым**.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `a0a29f5c8828f0df3c3df5ce8615957b655d2d73c12dd9509d91f69da52d6573`
response_sha256: `275a9e9915a1b3982eaee4aa1372919c7c8e8d65e19dfb59598452f76ecd465b`

## 109. pilot_017 / ru / qwen/qwen3.6-27b

Вопрос: Кто разработал государственный флаг Казахстана, принятый в 1992 году?

Эталон: Shaken Niyazbekov

Варианты: Шакен Ниязбеков; Шәкен Ниязбеков

[Источник](https://mirror.akorda.kz/public/en/state_symbols/kazakhstan_flag)

Ответ модели:

> Государственный флаг Казахстана был разработан художником Шакеном Ниязбековым.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `02629193d357e3360411d6f1f996be4d0e9249678c3f5b5b5eaa71eda78c07eb`
response_sha256: `494ba88e0e980bb4f5996926447cdf99a3e004496d0f2eeb101f7f94370d9ab6`

## 110. pilot_017 / ru / qwen/qwen3.8-27b

Вопрос: Кто разработал государственный флаг Казахстана, принятый в 1992 году?

Эталон: Shaken Niyazbekov

Варианты: Шакен Ниязбеков; Шәкен Ниязбеков

[Источник](https://mirror.akorda.kz/public/en/state_symbols/kazakhstan_flag)

Ответ модели:

> Государственный флаг Республики Казахстан, принятый 4 июня 1992 года, был разработан художником Шота Утеубаевым.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `70042ca87d812dc15ef1497b7d3684a95c779af27e64ca9f3b0cef84b707cff8`
response_sha256: `faa11243bb0b9d699cc8fa719e26eeaac0b8cb9366437be99ecf5174ffaf3d07`

## 111. pilot_018 / en / openai/gpt-oss-20b

Вопрос: Which part of a yurt is the central element of Kazakhstan's national emblem?

Эталон: Shanyrak

Варианты: Шанырак; Шаңырақ; шаңырақ

[Источник](https://mirror.akorda.kz/en/state_symbols/kazakhstan_emblem)

Ответ модели:

> The central element of Kazakhstan’s national emblem is the **yurt** (the round, tent‑shaped structure).

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `bbc1eed626fa3abd25222da4f36483126470fa13567a7046d02f527cb2ff42cb`
response_sha256: `b180c4eadd07432e157ee6dc1224446ece05f30aebe45645e4d43fecf37894ad`

## 112. pilot_018 / en / qwen/qwen3.6-27b

Вопрос: Which part of a yurt is the central element of Kazakhstan's national emblem?

Эталон: Shanyrak

Варианты: Шанырак; Шаңырақ; шаңырақ

[Источник](https://mirror.akorda.kz/en/state_symbols/kazakhstan_emblem)

Ответ модели:

> The premise is false. The central element of Kazakhstan's national emblem is the **shanyrak** (the crown or dome of a yurt), not a generic "part" in an ambiguous sense, but specifically this architectural component which symbolizes the hearth and the family.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `be3d0ddbf0f8c25194e0e8af43bdc961a804b2d5e4001d1c92a4f336e306d88c`
response_sha256: `67bc76db1a991fd72249a46b827a1a874cfd9118010fc04998c61865de662645`

## 113. pilot_018 / en / qwen/qwen3.8-27b

Вопрос: Which part of a yurt is the central element of Kazakhstan's national emblem?

Эталон: Shanyrak

Варианты: Шанырак; Шаңырақ; шаңырақ

[Источник](https://mirror.akorda.kz/en/state_symbols/kazakhstan_emblem)

Ответ модели:

> The premise is false. The central element of Kazakhstan's national emblem is the *shanyrak* (the circular crown or roof opening of a yurt), not a generic "part" of a yurt. The shanyrak is specifically depicted in the center of the emblem, surrounded by a golden sun with 32 rays.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `a20e57f5233580e6e1111b38987b4a2f0d6bc8f8f94bd9eb27c4250cc9c4ef3e`
response_sha256: `25f724a3ebc7c74f852f70a5a8f1df37f3f14e405a681acf3b33d1c3356ee4ef`

## 114. pilot_018 / kk / openai/gpt-oss-20b

Вопрос: Қазақстанның мемлекеттік елтаңбасының ортасында киіз үйдің қай бөлігі бейнеленген?

Эталон: Shanyrak

Варианты: Шанырак; Шаңырақ; шаңырақ

[Источник](https://mirror.akorda.kz/en/state_symbols/kazakhstan_emblem)

Ответ модели:

> Қазақстанның мемлекеттік елтаңбасының ортасында киіз үйдің **қапшық (қапшық)** бөлігі бейнеленген.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `1d28c833e5de3efb8a1382efa67d872de5c37c2b1d9843edc0c77e9584b5b0b6`
response_sha256: `d1296ea0cd9ec630c067b00db90ee220ff4cd54be0ccc39094d5ece90d65a765`

## 115. pilot_018 / kk / qwen/qwen3.6-27b

Вопрос: Қазақстанның мемлекеттік елтаңбасының ортасында киіз үйдің қай бөлігі бейнеленген?

Эталон: Shanyrak

Варианты: Шанырак; Шаңырақ; шаңырақ

[Источник](https://mirror.akorda.kz/en/state_symbols/kazakhstan_emblem)

Ответ модели:

> Қазақстанның мемлекеттік елтаңбасының ортасында киіз үйдің **шаңырағы** бейнеленген.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `0022a0b26c18a1d592bada25392aa092aae218f2ded8b5d943c046088c12c516`
response_sha256: `175a3e17c6d52d6503278ced898d08a438969044a7c96676ecd2099e630ed775`

## 116. pilot_018 / kk / qwen/qwen3.8-27b

Вопрос: Қазақстанның мемлекеттік елтаңбасының ортасында киіз үйдің қай бөлігі бейнеленген?

Эталон: Shanyrak

Варианты: Шанырак; Шаңырақ; шаңырақ

[Источник](https://mirror.akorda.kz/en/state_symbols/kazakhstan_emblem)

Ответ модели:

> Қазақстанның мемлекеттік елтаңбасының ортасында киіз үйдің **шанағы** (үстінгі бөлігі) бейнеленген.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `89f6a45155faa7b7b64df3830cf9a28d2f72076aed22cbc304387a67f2b97555`
response_sha256: `e0824848b45bc9fbfd0632f96376cf9e0ed76570b34e8d32a5de302256f2d8cb`

## 117. pilot_018 / ru / openai/gpt-oss-20b

Вопрос: Какая часть юрты находится в центре государственного герба Казахстана?

Эталон: Shanyrak

Варианты: Шанырак; Шаңырақ; шаңырақ

[Источник](https://mirror.akorda.kz/en/state_symbols/kazakhstan_emblem)

Ответ модели:

> В центре государственного герба Казахстана находится сама юрта.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `4c9bcb3642866aed6e4c024db61f1d683626c4d8ebd6ce8bd2da4bc2e8f44217`
response_sha256: `1e9920326a125515f1ba209a5bdcfa2d1fba523da5dce9fd4d6da39c8904643c`

## 118. pilot_018 / ru / qwen/qwen3.6-27b

Вопрос: Какая часть юрты находится в центре государственного герба Казахстана?

Эталон: Shanyrak

Варианты: Шанырак; Шаңырақ; шаңырақ

[Источник](https://mirror.akorda.kz/en/state_symbols/kazakhstan_emblem)

Ответ модели:

> Предпосылка вопроса неверна. В центре государственного герба Казахстана находится не юрта, а **шанырак** (верхняя часть юрты, символизирующая небо и единство семьи).

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `1d0b1c7c235514d0f438081d66d0ff0f2cdc58075fb94ca44a21da82e991b372`
response_sha256: `99170ac7c66b13dfa4453310268d7a4ec24bdaa2768b27e3fcfd35ca450b8529`

## 119. pilot_018 / ru / qwen/qwen3.8-27b

Вопрос: Какая часть юрты находится в центре государственного герба Казахстана?

Эталон: Shanyrak

Варианты: Шанырак; Шаңырақ; шаңырақ

[Источник](https://mirror.akorda.kz/en/state_symbols/kazakhstan_emblem)

Ответ модели:

> В государственном гербе Казахстана нет юрты.
> 
> В центре герба изображен **шанырак** (верхняя часть юрты, представляющая собой круглое отверстие в крыше), который является символом единства и продолжения рода. Сам шанырак окружен крыльями орла и расположен над изображением солнца.
> 
> Таким образом, предпосылка вопроса о том, что в центре находится вся юрта, неверна. В центре находится именно **шанырак**.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `d434fc124379e6c61b70d7b31b9c09bef8e8ba3cb8db962000a185f1d5d118fe`
response_sha256: `926608e9ee7eddf1e48828f3f33117eca1b0a70450847c409c8fdb1333d77f22`

## 120. pilot_019 / en / openai/gpt-oss-20b

Вопрос: Who composed the music of Kazakhstan's national anthem adopted in 2006?

Эталон: Shamshi Kaldayakov

Варианты: Shamshi Kaldayaqov; Шамши Калдаяков; Шәмші Қалдаяқов

[Источник](https://mirror.akorda.kz/public/ru/state_symbols/about_state_symbols)

Ответ модели:

> The music of Kazakhstan’s national anthem adopted in 2006 was composed by **Talgat Ertaev**.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `4e49d57cae05f3e551e75d91642e5b85f762294631b9048563459914e5f52541`
response_sha256: `e72ac021a5ffab8b79b9f0100783f0c9080d666c93b549eda26e2b898d24304a`

## 121. pilot_019 / en / qwen/qwen3.6-27b

Вопрос: Who composed the music of Kazakhstan's national anthem adopted in 2006?

Эталон: Shamshi Kaldayakov

Варианты: Shamshi Kaldayaqov; Шамши Калдаяков; Шәмші Қалдаяқов

[Источник](https://mirror.akorda.kz/public/ru/state_symbols/about_state_symbols)

Ответ модели:

> The music of Kazakhstan's national anthem was composed by **Shamshi Kaldayakov**.
> 
> (Note: The premise that the anthem was "adopted in 2006" is partially misleading. The music by Kaldayakov was adopted in 1992. In 2006, the *lyrics* were changed, but the music remained the same.)

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `9fbc66d993650c4f66c6ab360030e04736e4225b95ff12238ee14e060213193c`
response_sha256: `20fb4d3c6ce68d8eb89ea90525202d909dc9efd3618a2023db82f82024791763`

## 122. pilot_019 / en / qwen/qwen3.8-27b

Вопрос: Who composed the music of Kazakhstan's national anthem adopted in 2006?

Эталон: Shamshi Kaldayakov

Варианты: Shamshi Kaldayaqov; Шамши Калдаяков; Шәмші Қалдаяқов

[Источник](https://mirror.akorda.kz/public/ru/state_symbols/about_state_symbols)

Ответ модели:

> The premise is false. Kazakhstan's current national anthem was adopted in 2006, but the music was composed by **Shamshi Kaldayakov** (and Ramazan Myrzakhmetov), not someone else. However, the question asks *who* composed it, implying I should name the composer. The composer is **Shamshi Kaldayakov**.
> 
> Wait, let me double-check the premise. The question asks "Who composed...". It does not state a false premise about *who* composed it, it just asks for the name. The premise "adopted in 2006" is true. So there is no false premise in the question itself.
> 
> The music of Kazakhstan's national anthem, adopted in 2006, was composed by **Shamshi Kaldayakov**.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `296a01251fc1e1c465ea7fe23422b268c26e19912e86653333add6b59fa8e16d`
response_sha256: `c6ca13aaf37909faf59b54f71ba69aa7db37ed870edcf4839010a88049f08163`

## 123. pilot_019 / kk / openai/gpt-oss-20b

Вопрос: 2006 жылы қабылданған Қазақстанның мемлекеттік әнұранының музыкасын кім жазды?

Эталон: Shamshi Kaldayakov

Варианты: Shamshi Kaldayaqov; Шамши Калдаяков; Шәмші Қалдаяқов

[Источник](https://mirror.akorda.kz/public/ru/state_symbols/about_state_symbols)

Ответ модели:

> 2006 жылы қабылданған Қазақстанның мемлекеттік әнұранының музыкасын **Қ. Қ. Тұрсынов** жазған.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `0e1894d3acc38e0c1ec04c76359ec412a74ba877e0a4afdeb018970f5a4d1312`
response_sha256: `da4406da7149d60e1917563e87e3a52db0e75a437ae292f46998c863f38b56e3`

## 124. pilot_019 / kk / qwen/qwen3.6-27b

Вопрос: 2006 жылы қабылданған Қазақстанның мемлекеттік әнұранының музыкасын кім жазды?

Эталон: Shamshi Kaldayakov

Варианты: Shamshi Kaldayaqov; Шамши Калдаяков; Шәмші Қалдаяқов

[Источник](https://mirror.akorda.kz/public/ru/state_symbols/about_state_symbols)

Ответ модели:

> 2006 жылы қабылданған Қазақстанның мемлекеттік әнұранының музыкасын **Шәмші Қалдаяқов** жазды.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `bf38244da42a99d9d0593da80eb0544729e28a615b3925a4326357f6ffeb3228`
response_sha256: `9837c979a6205fa6711e77afa7dfc34d721b7a8dd6f790ab37b2b86fc55b374d`

## 125. pilot_019 / kk / qwen/qwen3.8-27b

Вопрос: 2006 жылы қабылданған Қазақстанның мемлекеттік әнұранының музыкасын кім жазды?

Эталон: Shamshi Kaldayakov

Варианты: Shamshi Kaldayaqov; Шамши Калдаяков; Шәмші Қалдаяқов

[Источник](https://mirror.akorda.kz/public/ru/state_symbols/about_state_symbols)

Ответ модели:

> Сұрақтағы алғышарт дұрыс емес. Қазақстанның мемлекеттік әнұраны 2006 жылы емес, **1992 жылы** қабылданған.
> 
> Әнұранның музыкасын **Шамши Қалдаяқов** жазды.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `19813555fd76a5005185f051b1ad3feef24088803ee1ffb425ba31a3eec7c056`
response_sha256: `5a235fcc49a03ff195ef1fd8902a9889619b1f75cb4804709c17d711672dbf53`

## 126. pilot_019 / ru / openai/gpt-oss-20b

Вопрос: Кто написал музыку государственного гимна Казахстана, принятого в 2006 году?

Эталон: Shamshi Kaldayakov

Варианты: Shamshi Kaldayaqov; Шамши Калдаяков; Шәмші Қалдаяқов

[Источник](https://mirror.akorda.kz/public/ru/state_symbols/about_state_symbols)

Ответ модели:

> Музыку государственного гимна Казахстана, принятого в 2006 году, написал композитор **Му́қит Ота́ров**.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `25c07a1eb0451172d93cc4544f6fc8b1886e484f58b053c6dfeb601ba2b61b7d`
response_sha256: `e40d2e1b50e9a8670dc5d8e6e945f63c525ed8d5cad5f070d68a167b3bee7f52`

## 127. pilot_019 / ru / qwen/qwen3.6-27b

Вопрос: Кто написал музыку государственного гимна Казахстана, принятого в 2006 году?

Эталон: Shamshi Kaldayakov

Варианты: Shamshi Kaldayaqov; Шамши Калдаяков; Шәмші Қалдаяқов

[Источник](https://mirror.akorda.kz/public/ru/state_symbols/about_state_symbols)

Ответ модели:

> Музыку государственного гимна Казахстана написал Шакен Ниязбеков.
> 
> *(Примечание: Предпосылка вопроса о дате принятия неверна. Гимн в текущей редакции с музыкой Шакена Ниязбекова и текстом на казахском языке был принят 7 января 2006 года, однако сама музыка была написана и утверждена ранее, в 1992 году, для гимна независимого Казахстана. В 2006 году был изменен только текст гимна.)*

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `dd79f0283bdf2f846dc42ebfa8b78ee9f74fde0b741ee58a5438176c7f3ec916`
response_sha256: `282ec7d8307a18d8a622b88d2df0cdb0145a5c625cd2738cdb3a1bebed9db1e8`

## 128. pilot_019 / ru / qwen/qwen3.8-27b

Вопрос: Кто написал музыку государственного гимна Казахстана, принятого в 2006 году?

Эталон: Shamshi Kaldayakov

Варианты: Shamshi Kaldayaqov; Шамши Калдаяков; Шәмші Қалдаяқов

[Источник](https://mirror.akorda.kz/public/ru/state_symbols/about_state_symbols)

Ответ модели:

> Музыку государственного гимна Казахстана, принятого в 2006 году, написал Шамши Калдаяков.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `b55bf35b478d7bacdfe632670f82575bb9dbd5069456651522ef8fe999a55a3f`
response_sha256: `c2b4bb45408ed600f1d62d76801271324519f8ea24bbbadac8aeaef88603d72b`

## 129. pilot_020 / en / openai/gpt-oss-20b

Вопрос: What is Kazakhstan's world rank by territorial area according to Akorda?

Эталон: 9

Варианты: ninth; 9th; девятое; девятое место; тоғызыншы; 9-орын

[Источник](https://www.akorda.kz/en/republic_of_kazakhstan/kazakhstan)

Ответ модели:

> Kazakhstan is ranked 9th in the world by territorial area.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `fc35fa9ab78b3b85941bfc9c8ef4b14fc399699cfd65f22300a4fbd62fe263bd`
response_sha256: `f42d8fdd753c9e00f3ac62039fb5b99803c835275ee4dcbbf09f6da14a2b94c2`

## 130. pilot_020 / en / qwen/qwen3.6-27b

Вопрос: What is Kazakhstan's world rank by territorial area according to Akorda?

Эталон: 9

Варианты: ninth; 9th; девятое; девятое место; тоғызыншы; 9-орын

[Источник](https://www.akorda.kz/en/republic_of_kazakhstan/kazakhstan)

Ответ модели:

> Kazakhstan is the 9th largest country in the world by territorial area.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `df04b7b909fc3d7c4a9e246eac60dd3f2f5a5b5691608a27af0f30ae2f44b987`
response_sha256: `0dc3ee304c37ad9285966d4a4760aa6aa51c0d412b51b64698af9e11ac1298bf`

## 131. pilot_020 / en / qwen/qwen3.8-27b

Вопрос: What is Kazakhstan's world rank by territorial area according to Akorda?

Эталон: 9

Варианты: ninth; 9th; девятое; девятое место; тоғызыншы; 9-орын

[Источник](https://www.akorda.kz/en/republic_of_kazakhstan/kazakhstan)

Ответ модели:

> Kazakhstan is the 9th largest country in the world by total area.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `dd0a0cc08f76d4a0a6ca3eeedc783b4698c52952c3f0e4d317d39c50723bea42`
response_sha256: `f73a76d6463a15c9f60723bbfa5eb4073a78169567f58c574dae8605c8d4caf3`

## 132. pilot_020 / kk / openai/gpt-oss-20b

Вопрос: Ақорда сайтына сәйкес Қазақстан аумағының көлемі бойынша әлемде нешінші орында?

Эталон: 9

Варианты: ninth; 9th; девятое; девятое место; тоғызыншы; 9-орын

[Источник](https://www.akorda.kz/en/republic_of_kazakhstan/kazakhstan)

Ответ модели:

> Ақорда сайтына сәйкес Қазақстан аумағы бойынша әлемде **9‑шы** орында.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `8702ceba37ad910ca353c4c1d3354b788a8970879ad2955294bf132b60a0f63a`
response_sha256: `b66a66f7edb55ce997fd81f3b43f44588e20c7dc7212c8dacaa9d981860cfb87`

## 133. pilot_020 / kk / qwen/qwen3.6-27b

Вопрос: Ақорда сайтына сәйкес Қазақстан аумағының көлемі бойынша әлемде нешінші орында?

Эталон: 9

Варианты: ninth; 9th; девятое; девятое место; тоғызыншы; 9-орын

[Источник](https://www.akorda.kz/en/republic_of_kazakhstan/kazakhstan)

Ответ модели:

> Ақорда сайтына сәйкес, Қазақстан аумағының көлемі бойынша әлемде **9-шы** орында.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `7357e32a9406ba4b5b082842498d7223f29398907866ba7d3088c95713555a40`
response_sha256: `8c6cc82f96102b5ccf7491cc6ef3ea8c30102674fab902061e51db93ed7af530`

## 134. pilot_020 / kk / qwen/qwen3.8-27b

Вопрос: Ақорда сайтына сәйкес Қазақстан аумағының көлемі бойынша әлемде нешінші орында?

Эталон: 9

Варианты: ninth; 9th; девятое; девятое место; тоғызыншы; 9-орын

[Источник](https://www.akorda.kz/en/republic_of_kazakhstan/kazakhstan)

Ответ модели:

> Сұрақта жалған алғышарт бар. Ақорда (The White House) — АҚШ-тың мемлекеттік сайты, ол Қазақстан аумағының әлемдегі орны туралы ресми деректер көзі емес.
> 
> Дегенмен, факті бойынша: Қазақстан аумағы бойынша әлемде **9-шы** орында (кейбір дереккөздерде 10-шы орын деп көрсетіледі, бұл су алаптары мен шекара мәселелеріне байланысты).

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `8226343e6545a6ff2fb21c7989135386d364235a5c7c29fe8d13b96b2f959593`
response_sha256: `fee93fdc9ac6bf6d402b4c1f44bcf5cf08b11ff22d1575da3ea74940d7de5639`

## 135. pilot_020 / ru / openai/gpt-oss-20b

Вопрос: Какое место в мире по площади территории занимает Казахстан согласно сайту Акорды?

Эталон: 9

Варианты: ninth; 9th; девятое; девятое место; тоғызыншы; 9-орын

[Источник](https://www.akorda.kz/en/republic_of_kazakhstan/kazakhstan)

Ответ модели:

> Казахстан занимает **9‑е место** в мире по площади территории (по данным сайта «Акорда»).

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `1f2ea88a61a45522e66eb5c192c4850ce999ab1e0c970c74e9d9ce36c3921526`
response_sha256: `93905870e1e15c4d08be87a64314869a736231e4dffa7722f7f843a982875ac9`

## 136. pilot_020 / ru / qwen/qwen3.6-27b

Вопрос: Какое место в мире по площади территории занимает Казахстан согласно сайту Акорды?

Эталон: 9

Варианты: ninth; 9th; девятое; девятое место; тоғызыншы; 9-орын

[Источник](https://www.akorda.kz/en/republic_of_kazakhstan/kazakhstan)

Ответ модели:

> Согласно официальному сайту Акорды, Казахстан занимает 9-е место в мире по площади территории.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `72cf96c232cebd50320252b8560b52a05b0d27eac0d420038ca229a651434f33`
response_sha256: `ea68e783513cc4b066725dadccc3ee84c7f3cba9e58b58bda42dd22cee431203`

## 137. pilot_020 / ru / qwen/qwen3.8-27b

Вопрос: Какое место в мире по площади территории занимает Казахстан согласно сайту Акорды?

Эталон: 9

Варианты: ninth; 9th; девятое; девятое место; тоғызыншы; 9-орын

[Источник](https://www.akorda.kz/en/republic_of_kazakhstan/kazakhstan)

Ответ модели:

> Согласно официальному сайту Акорды, Казахстан занимает **9-е место** в мире по площади территории.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `064eac35a99aebd32bffee01b9ab681eb2290e592ad6eb3bd8b08c3a6ae59bd6`
response_sha256: `13b3e3986d39d0a96cf7a499392c76344a2f0f9d1ae413676d6043584e1f8380`

## 138. pilot_021 / en / openai/gpt-oss-20b

Вопрос: Who won the Nobel Prize in Literature for 1918?

Эталон: No prize was awarded in 1918

Варианты: Not awarded; No one; Никто; Премия не присуждалась; Ешкім; Сыйлық берілген жоқ

[Источник](https://www.nobelprize.org/prizes/literature/1918/summary/)

Ответ модели:

> There was no Nobel Prize in Literature awarded in 1918.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `5bbdeee9b21f7eee842b17d14dbe8d60a435958c9b3a38558b1a86bdba6133e2`
response_sha256: `553fdbba9ff0604c87304ba71a98fac5c6e627588aafb8d37d3915bee8a0bd3c`

## 139. pilot_021 / en / qwen/qwen3.6-27b

Вопрос: Who won the Nobel Prize in Literature for 1918?

Эталон: No prize was awarded in 1918

Варианты: Not awarded; No one; Никто; Премия не присуждалась; Ешкім; Сыйлық берілген жоқ

[Источник](https://www.nobelprize.org/prizes/literature/1918/summary/)

Ответ модели:

> The Nobel Prize in Literature for 1918 was not awarded. It was deferred and awarded in 1919 to Carl Friedrich Georg Spitteler.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `4c9bcd43238b2acfc46a35aaf3dfa1795d2e43a146f64f42eec85a76742356d6`
response_sha256: `ca7d081354b14d3de2a2702fd937133eff8625ab96c7fcce088f5736a2f0702d`

## 140. pilot_021 / en / qwen/qwen3.8-27b

Вопрос: Who won the Nobel Prize in Literature for 1918?

Эталон: No prize was awarded in 1918

Варианты: Not awarded; No one; Никто; Премия не присуждалась; Ешкім; Сыйлық берілген жоқ

[Источник](https://www.nobelprize.org/prizes/literature/1918/summary/)

Ответ модели:

> The Nobel Prize in Literature was not awarded in 1918.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `5eeeb1914c48406c49f583941532a5a69613a3b86c67c65c21705a5af39fd014`
response_sha256: `47d4fe433707b07e817b9b9fc4a651ec7548516cc19a7bbbc3c7c68745dec67e`

## 141. pilot_021 / kk / openai/gpt-oss-20b

Вопрос: 1918 жылғы әдебиет саласындағы Нобель сыйлығының лауреаты кім болды?

Эталон: No prize was awarded in 1918

Варианты: Not awarded; No one; Никто; Премия не присуждалась; Ешкім; Сыйлық берілген жоқ

[Источник](https://www.nobelprize.org/prizes/literature/1918/summary/)

Ответ модели:

> 1918 жылы әдебиет саласындағы Нобель сыйлығы берілмеді.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `d8c116f188a5aa81b729fb92efac76d2a5f32b5858efd7152bebf0ecf9bb28c8`
response_sha256: `04d899220d422001daf80db36fb8890afef8a239de496e6635a99ce7d5ad5861`

## 142. pilot_021 / kk / qwen/qwen3.6-27b

Вопрос: 1918 жылғы әдебиет саласындағы Нобель сыйлығының лауреаты кім болды?

Эталон: No prize was awarded in 1918

Варианты: Not awarded; No one; Никто; Премия не присуждалась; Ешкім; Сыйлық берілген жоқ

[Источник](https://www.nobelprize.org/prizes/literature/1918/summary/)

Ответ модели:

> 1918 жылғы әдебиет саласындағы Нобель сыйлығының лауреаты — Карл Шпиттлер (Carl Spitteler).

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `70b58a2d981024a1a16cb4951f76b06f1189a4247f8fdf51ab752f1b549b60b9`
response_sha256: `6f70960f04fb7b8d24eb921a7e764b57f1707f0f8258ea59386f8c6e5aa9f823`

## 143. pilot_021 / kk / qwen/qwen3.8-27b

Вопрос: 1918 жылғы әдебиет саласындағы Нобель сыйлығының лауреаты кім болды?

Эталон: No prize was awarded in 1918

Варианты: Not awarded; No one; Никто; Премия не присуждалась; Ешкім; Сыйлық берілген жоқ

[Источник](https://www.nobelprize.org/prizes/literature/1918/summary/)

Ответ модели:

> 1918 жылы әдебиет саласында Нобель сыйлығы берілмеген.
> 
> Бұл жылдары (1916, 1918, 1919, 1924, 1925, 1926, 1927, 1936, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2

Причина проверки: Invalid/truncated target

Оценка / пояснение: ___

request_id: `30101baf17696a9f0295d0f6ea61c85e58fcd5431f6f760a89f43962fe4bc8c2`
response_sha256: `47c347b8d37795f6dec4dc1ad19c79f5e68dfdc5a8010edde676bff16f28c976`

## 144. pilot_021 / ru / openai/gpt-oss-20b

Вопрос: Кто стал лауреатом Нобелевской премии по литературе за 1918 год?

Эталон: No prize was awarded in 1918

Варианты: Not awarded; No one; Никто; Премия не присуждалась; Ешкім; Сыйлық берілген жоқ

[Источник](https://www.nobelprize.org/prizes/literature/1918/summary/)

Ответ модели:

> Нобелевской премией по литературе за 1918 год был удостоен французский писатель **Ромэн Роланд**.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `51345eb367d3ee352f0225cabc2f23d3a48afcf173823715407e2d5015d340ac`
response_sha256: `6ef66f9d33da34b08c559d2e267e66471d55d5ab6f6319c27841a2e1be909f62`

## 145. pilot_021 / ru / qwen/qwen3.6-27b

Вопрос: Кто стал лауреатом Нобелевской премии по литературе за 1918 год?

Эталон: No prize was awarded in 1918

Варианты: Not awarded; No one; Никто; Премия не присуждалась; Ешкім; Сыйлық берілген жоқ

[Источник](https://www.nobelprize.org/prizes/literature/1918/summary/)

Ответ модели:

> Лауреатом Нобелевской премии по литературе за 1918 год стал Карл Гильдебрандт Гильдебрандт (Carl Hildebrand Hildebrandt).
> 
> **Важное уточнение:** Премия за 1918 год была присуждена в 1919 году. В 1918 году премия не присуждалась из-за Первой мировой войны.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `c525a77b0c07adf1a5daf4c8ca26c675fe41f7cdab9a45b48510c48e1855e5d8`
response_sha256: `b5a1cd7f5b77ebb168e0d2deffdc73adbdc0f0e8704520d01cda59142c1703c0`

## 146. pilot_021 / ru / qwen/qwen3.8-27b

Вопрос: Кто стал лауреатом Нобелевской премии по литературе за 1918 год?

Эталон: No prize was awarded in 1918

Варианты: Not awarded; No one; Никто; Премия не присуждалась; Ешкім; Сыйлық берілген жоқ

[Источник](https://www.nobelprize.org/prizes/literature/1918/summary/)

Ответ модели:

> Нобелевская премия по литературе за 1918 год не была присуждена.
> 
> В этот период (1916, 1918, 1935, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024) были годы, когда премия

Причина проверки: Invalid/truncated target

Оценка / пояснение: ___

request_id: `11c6acaae888883f181c322a5a9b13e694721bc353143e4cf7265355e9202869`
response_sha256: `31ef141f0257649406487e8f3fb92ee59095d423e79574f8e5acc19c3606b7bd`

## 147. pilot_022 / en / openai/gpt-oss-20b

Вопрос: Who won the Nobel Prize in Literature for 1940?

Эталон: No prize was awarded in 1940

Варианты: Not awarded; No one; Никто; Премия не присуждалась; Ешкім; Сыйлық берілген жоқ

[Источник](https://www.nobelprize.org/prizes/literature/1940/summary/)

Ответ модели:

> There was no Nobel Prize in Literature awarded in 1940.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `981067b48cb6625bb01025c36f6683ea927ed66cf2e5fd4891337d46acd1686c`
response_sha256: `dd3caa0e7a89a3fac5e94d1df0d21ebcf67b6fef8cc06660eaec5a9628c58015`

## 148. pilot_022 / en / qwen/qwen3.6-27b

Вопрос: Who won the Nobel Prize in Literature for 1940?

Эталон: No prize was awarded in 1940

Варианты: Not awarded; No one; Никто; Премия не присуждалась; Ешкім; Сыйлық берілген жоқ

[Источник](https://www.nobelprize.org/prizes/literature/1940/summary/)

Ответ модели:

> The premise is false. No Nobel Prize in Literature was awarded in 1940 due to the outbreak of World War II.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `0554d3934f5e29991ae8f7f0bcf9e5a6d30924534d753659b1cc10218e78ef46`
response_sha256: `3e5bc624074608a821369c5886e4f64c1dacecad6064c43cad3ce4718a25ef78`

## 149. pilot_022 / en / qwen/qwen3.8-27b

Вопрос: Who won the Nobel Prize in Literature for 1940?

Эталон: No prize was awarded in 1940

Варианты: Not awarded; No one; Никто; Премия не присуждалась; Ешкім; Сыйлық берілген жоқ

[Источник](https://www.nobelprize.org/prizes/literature/1940/summary/)

Ответ модели:

> The Nobel Prize in Literature for 1940 was not awarded. The prize was suspended for 1940, 1941, and 1943 due to World War II.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `0b755df2ef5e1a537e8a5c72778d455fcad1a4e02ecf13cbf586dcafba8872dc`
response_sha256: `5339f91cccecb206616e964ca83c6e5f289101524e430df9d9b86b197f35ed1f`

## 150. pilot_022 / kk / openai/gpt-oss-20b

Вопрос: 1940 жылғы әдебиет саласындағы Нобель сыйлығының лауреаты кім болды?

Эталон: No prize was awarded in 1940

Варианты: Not awarded; No one; Никто; Премия не присуждалась; Ешкім; Сыйлық берілген жоқ

[Источник](https://www.nobelprize.org/prizes/literature/1940/summary/)

Ответ модели:

> 1940 жылы әдебиет саласындағы Нобель сыйлығы берілмеді.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `815916f0734ca3d17f4a9d902cf810c0c84ea58e22bd9f8401cbcc47464f2b15`
response_sha256: `bb767f9144964a84615224c6ddf1131b23f8c62521c576fac44067f558140776`
