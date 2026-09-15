# Проверка ответов моделей: pilot100_v1

Пакет 7. Номера 301–350. Это часть пилота, по уже полученным ответам; сбор остальных продолжается.

Оцените весь ответ: 1 — фактически верен, 0 — фактически неверен. Если случай неоднозначен или ответ оборван, оставьте пояснение вместо догадки. Для ложной предпосылки ответ должен явно её отвергать. Можно прислать номера и оценки в чат, указав название пакета.

Проверка эталонных фактов ранее не означает проверки этих ответов моделей.

## 301. pilot_090 / en / openai/gpt-oss-20b

Вопрос: Who won the men's 100 metres at the 1940 Summer Olympics?

Эталон: No one; the 1940 Summer Olympics were cancelled

Варианты: No one; The Games were cancelled; Никто; Игры были отменены; Ешкім; Ойындар өткізілген жоқ

[Источник](https://www.olympics.com.au/olympians/richard-garrard/)

Ответ модели:

> There were no Summer Olympics held in 1940, so no men's 100 metres champion was declared that year.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `3e963bbd44e3ebf363bc38bacb23d12953394415fd025099dc38077d53f79ba1`
response_sha256: `42ff9064f03cc50f1243ccc754ef17e28feafe653c1ff2730c8b8ce17b80261e`

## 302. pilot_090 / en / qwen/qwen3.6-27b

Вопрос: Who won the men's 100 metres at the 1940 Summer Olympics?

Эталон: No one; the 1940 Summer Olympics were cancelled

Варианты: No one; The Games were cancelled; Никто; Игры были отменены; Ешкім; Ойындар өткізілген жоқ

[Источник](https://www.olympics.com.au/olympians/richard-garrard/)

Ответ модели:

> The premise is false. The 1940 Summer Olympics were not held due to World War II.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `4e61f6fd46aad7eb48583c72b5ce30a1ecec83de3ea30046e3f32fc637e110e0`
response_sha256: `7ce75a79fbe8600f990a0c5cc9ec446b18912b2990ff3a39ae3b33e90e7113e6`

## 303. pilot_090 / en / qwen/qwen3.8-27b

Вопрос: Who won the men's 100 metres at the 1940 Summer Olympics?

Эталон: No one; the 1940 Summer Olympics were cancelled

Варианты: No one; The Games were cancelled; Никто; Игры были отменены; Ешкім; Ойындар өткізілген жоқ

[Источник](https://www.olympics.com.au/olympians/richard-garrard/)

Ответ модели:

> The premise is false. The 1940 Summer Olympics were cancelled due to World War II and never took place.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `87ecc6dc07b02799fd7a44569fe663e68df74b4d2b58841544f9f9dac4cbd21d`
response_sha256: `805119d5f6c2cec02b9482cafea72ed6cec26c6c58fe10b8b42e066fd809236d`

## 304. pilot_090 / kk / openai/gpt-oss-20b

Вопрос: 1940 жылғы жазғы Олимпиада ойындарында ерлер арасындағы 100 метрге жүгіруді кім жеңді?

Эталон: No one; the 1940 Summer Olympics were cancelled

Варианты: No one; The Games were cancelled; Никто; Игры были отменены; Ешкім; Ойындар өткізілген жоқ

[Источник](https://www.olympics.com.au/olympians/richard-garrard/)

Ответ модели:

> 1940 жылғы жазғы Олимпиада ойындары – 1940 жылы Токио (япон) және Берлин (неміс) арасында жоспарланған, бірақ екінші дүниежүзілік соғыс басталғандықтан 1940 жылы өткізілмеді. Сондықтан 1940 жылғы жазғы Олимпиадада ерлер арасындағы 100 метрге жүгіру жарығы болмады, сондықтан жеңімпаз анықталмады.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `59a48db5fdd1e6f891fb4396e3668cbe83e651202a692eee05549e5f4db0d9fe`
response_sha256: `7ab6287220bae3ab52c9ad4408b37a608588b00c750db92fa1bcc040c468273f`

## 305. pilot_090 / kk / qwen/qwen3.6-27b

Вопрос: 1940 жылғы жазғы Олимпиада ойындарында ерлер арасындағы 100 метрге жүгіруді кім жеңді?

Эталон: No one; the 1940 Summer Olympics were cancelled

Варианты: No one; The Games were cancelled; Никто; Игры были отменены; Ешкім; Ойындар өткізілген жоқ

[Источник](https://www.olympics.com.au/olympians/richard-garrard/)

Ответ модели:

> 1940 жылы жазғы Олимпиада ойындары өткізілмеді (Екінші дүниежүзілік соғысқа байланысты болдырмауға шешім қабылданды). Сондықтан бұл жарыста жеңімпаз болған жоқ.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `df39ae14c1c64cc41aa67db34ce8b449d9447e411ed15936a6aebc71c9da8e8d`
response_sha256: `f725d57b132d6e91bf91826bb1e429caf4782110ac8bd9d7dc84bec47710b0e7`

## 306. pilot_090 / kk / qwen/qwen3.8-27b

Вопрос: 1940 жылғы жазғы Олимпиада ойындарында ерлер арасындағы 100 метрге жүгіруді кім жеңді?

Эталон: No one; the 1940 Summer Olympics were cancelled

Варианты: No one; The Games were cancelled; Никто; Игры были отменены; Ешкім; Ойындар өткізілген жоқ

[Источник](https://www.olympics.com.au/olympians/richard-garrard/)

Ответ модели:

> 1940 жылғы жазғы Олимпиада ойындары өтпеді. Бұл ойындар Токиода (Жапония) өтуі тиіс болғанымен, Екінші дүниежүзілік соғыс басталуына байланысты болдырылмады. Сондықтан бұл жарыста ешкім жеңімпаз атанбады.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `177096e0c0d5fc69a9d471bd8d8492da4189a5946e291d32c3b2140aba03ee0e`
response_sha256: `df7e90da476ff4ee9cfb303242717d5cf3819e9f257f209af6df9794d4131034`

## 307. pilot_090 / ru / openai/gpt-oss-20b

Вопрос: Кто выиграл мужской бег на 100 метров на летних Олимпийских играх 1940 года?

Эталон: No one; the 1940 Summer Olympics were cancelled

Варианты: No one; The Games were cancelled; Никто; Игры были отменены; Ешкім; Ойындар өткізілген жоқ

[Источник](https://www.olympics.com.au/olympians/richard-garrard/)

Ответ модели:

> На летних Олимпийских играх 1940 года не было соревнований, потому что эти игры были отменены из‑за Второй мировой войны. Поэтому победителя в мужском беге на 100 метров в 1940 году не было.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `e3e24441a6321076340754a805c39394abb36b9664efc1df5ab1c406208915a7`
response_sha256: `9fe27ac5fb5a667bcff94caa079478d02d30a7c66e7178d5fea27832bb34eb98`

## 308. pilot_090 / ru / qwen/qwen3.6-27b

Вопрос: Кто выиграл мужской бег на 100 метров на летних Олимпийских играх 1940 года?

Эталон: No one; the 1940 Summer Olympics were cancelled

Варианты: No one; The Games were cancelled; Никто; Игры были отменены; Ешкім; Ойындар өткізілген жоқ

[Источник](https://www.olympics.com.au/olympians/richard-garrard/)

Ответ модели:

> Летние Олимпийские игры 1940 года не проводились из-за Второй мировой войны, поэтому победителя в этом виде спорта нет.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `2faadf38cb468e0742b78dca3a40f9c1e656ab9524d18ea5a1fd242384b71a90`
response_sha256: `db981f3fd1f5c693117f4f8b62cf337e98e6a3adb0a788c5bdc38965a853a31f`

## 309. pilot_090 / ru / qwen/qwen3.8-27b

Вопрос: Кто выиграл мужской бег на 100 метров на летних Олимпийских играх 1940 года?

Эталон: No one; the 1940 Summer Olympics were cancelled

Варианты: No one; The Games were cancelled; Никто; Игры были отменены; Ешкім; Ойындар өткізілген жоқ

[Источник](https://www.olympics.com.au/olympians/richard-garrard/)

Ответ модели:

> Летние Олимпийские игры 1940 года не проводились из-за Второй мировой войны. Следовательно, победителя в мужском беге на 100 метров на этих Играх не было.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `7dd41291afe833d942685814fc320785dcc65c969b72f3a220fb0cdee5dfdf4f`
response_sha256: `eefd6bb6ec984624cfb36d3f06a0298c1202f957afdbe817a47e30807689f2a9`

## 310. pilot_091 / en / openai/gpt-oss-20b

Вопрос: Who won the men's long jump at the 1944 Summer Olympics?

Эталон: No one; the 1944 Summer Olympics were cancelled

Варианты: No one; The Games were cancelled; Никто; Игры были отменены; Ешкім; Ойындар өткізілген жоқ

[Источник](https://www.olympics.com.au/olympians/richard-garrard/)

Ответ модели:

> There were no Summer Olympics held in 1944, so no men's long jump event took place that year.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `66d2c68ed7ef9d2662262ffcabc26fc97ad786cfa684bcbd0e90daf8a5adc3c5`
response_sha256: `b9f159e1f4cacf173d9c36f88ee09a3d211d05babd7a42524d1822ad493fba11`

## 311. pilot_091 / en / qwen/qwen3.6-27b

Вопрос: Who won the men's long jump at the 1944 Summer Olympics?

Эталон: No one; the 1944 Summer Olympics were cancelled

Варианты: No one; The Games were cancelled; Никто; Игры были отменены; Ешкім; Ойындар өткізілген жоқ

[Источник](https://www.olympics.com.au/olympians/richard-garrard/)

Ответ модели:

> The premise is false. The 1944 Summer Olympics were cancelled due to World War II.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `eaf80e8552757830116a4257d0f31aee0ce885e71fbd883aa6135ce94ae6bbdb`
response_sha256: `0c8a309f41f5f9aece8a0c3437e9942eed9ff0af880d1b4b0b6e52af7642ed48`

## 312. pilot_091 / en / qwen/qwen3.8-27b

Вопрос: Who won the men's long jump at the 1944 Summer Olympics?

Эталон: No one; the 1944 Summer Olympics were cancelled

Варианты: No one; The Games were cancelled; Никто; Игры были отменены; Ешкім; Ойындар өткізілген жоқ

[Источник](https://www.olympics.com.au/olympians/richard-garrard/)

Ответ модели:

> The premise is false. The 1944 Summer Olympics were cancelled due to World War II.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `0aa39b343efc056c05d92a4dffb8a6faa207bd37c33d6461dca91f92898bc0fa`
response_sha256: `0c8a309f41f5f9aece8a0c3437e9942eed9ff0af880d1b4b0b6e52af7642ed48`

## 313. pilot_091 / kk / openai/gpt-oss-20b

Вопрос: 1944 жылғы жазғы Олимпиада ойындарында ерлер арасындағы ұзындыққа секіруді кім жеңді?

Эталон: No one; the 1944 Summer Olympics were cancelled

Варианты: No one; The Games were cancelled; Никто; Игры были отменены; Ешкім; Ойындар өткізілген жоқ

[Источник](https://www.olympics.com.au/olympians/richard-garrard/)

Ответ модели:

> 1944 жылы жазғы Олимпиада ойындары өтпеді, сондықтан ерлер арасындағы ұзындыққа секіру жарығы да болмады.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `b08893f14d9a456528e640861d2ac618f52c0bf8fdcc98d2cb89fbb3895b9938`
response_sha256: `1d9ebacfcfcba63abe213faa7b5fbae686318a9ef9979cc83b11b96b3cb236f9`

## 314. pilot_091 / kk / qwen/qwen3.6-27b

Вопрос: 1944 жылғы жазғы Олимпиада ойындарында ерлер арасындағы ұзындыққа секіруді кім жеңді?

Эталон: No one; the 1944 Summer Olympics were cancelled

Варианты: No one; The Games were cancelled; Никто; Игры были отменены; Ешкім; Ойындар өткізілген жоқ

[Источник](https://www.olympics.com.au/olympians/richard-garrard/)

Ответ модели:

> 1944 жылғы жазғы Олимпиада ойындары өткізілмеді, себебі екінші дүниежүзілік соғыс болып жатты. Сондықтан бұл сұрақта жалған алғышарт бар.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `5c1c618d17fe5025b9badefae134fb967ceaad19b3334955eadda2aca72bb9be`
response_sha256: `42dd6e6c3f44b3ba279a966ad4be6404ee1f6a99ca8cc8ae55e62304682f1c5a`

## 315. pilot_091 / kk / qwen/qwen3.8-27b

Вопрос: 1944 жылғы жазғы Олимпиада ойындарында ерлер арасындағы ұзындыққа секіруді кім жеңді?

Эталон: No one; the 1944 Summer Olympics were cancelled

Варианты: No one; The Games were cancelled; Никто; Игры были отменены; Ешкім; Ойындар өткізілген жоқ

[Источник](https://www.olympics.com.au/olympians/richard-garrard/)

Ответ модели:

> 1944 жылғы Олимпиада ойындары өтпеді. Бұл ойындар Токиода өтуі тиіс болғанымен, Екінші дүниежүзілік соғыс салдарынан болдырылмады.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `8089663e3d6c9500afa848d6795226a05ffba2a5ed1ddc3fd0afb2d029a138c2`
response_sha256: `d358b7d121d0165a9dc31e3f999f827d6a383f6eaf83f5251d2a816a870ee14b`

## 316. pilot_091 / ru / openai/gpt-oss-20b

Вопрос: Кто выиграл мужские прыжки в длину на летних Олимпийских играх 1944 года?

Эталон: No one; the 1944 Summer Olympics were cancelled

Варианты: No one; The Games were cancelled; Никто; Игры были отменены; Ешкім; Ойындар өткізілген жоқ

[Источник](https://www.olympics.com.au/olympians/richard-garrard/)

Ответ модели:

> На летних Олимпийских играх 1944 года не было соревнований, так как Олимпийские игры в этом году не проводились (они были отменены из‑за Второй мировой войны). Поэтому победителя в мужских прыжках в длину в 1944 году не было.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `956f17a63fc376ea15b7632b2654ae40855ddc2929d03661326323cb9caf5efd`
response_sha256: `13e7faed3a8b54aa1a2a72e6da099c01095368ff3e761e08f6d28d3bec05dc1f`

## 317. pilot_091 / ru / qwen/qwen3.6-27b

Вопрос: Кто выиграл мужские прыжки в длину на летних Олимпийских играх 1944 года?

Эталон: No one; the 1944 Summer Olympics were cancelled

Варианты: No one; The Games were cancelled; Никто; Игры были отменены; Ешкім; Ойындар өткізілген жоқ

[Источник](https://www.olympics.com.au/olympians/richard-garrard/)

Ответ модели:

> Летние Олимпийские игры 1944 года не проводились из-за Второй мировой войны.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `8fbe585dfbf24c869631b0a729a7c48944d7c6aaca003d8d3a99eddf8861afe2`
response_sha256: `c3d7c4d332179339546d1e44ba9bca69df53812255bb063935eeffa316222792`

## 318. pilot_091 / ru / qwen/qwen3.8-27b

Вопрос: Кто выиграл мужские прыжки в длину на летних Олимпийских играх 1944 года?

Эталон: No one; the 1944 Summer Olympics were cancelled

Варианты: No one; The Games were cancelled; Никто; Игры были отменены; Ешкім; Ойындар өткізілген жоқ

[Источник](https://www.olympics.com.au/olympians/richard-garrard/)

Ответ модели:

> Летние Олимпийские игры 1944 года не проводились из-за Второй мировой войны. Следовательно, победителя в мужских прыжках в длину на этих Играх не было.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `e3d582b8c96b826247cdf9dbb7c66a924ab22755cf8a3fc3dae4b59f6c2e2de0`
response_sha256: `92c3609796df45fb6acaa742bda6391b60ab9d0bb95fb29f4eeba1aa93317cb0`

## 319. pilot_092 / en / openai/gpt-oss-20b

Вопрос: In what year did Mahatma Gandhi receive the Nobel Peace Prize?

Эталон: Never; Mahatma Gandhi was not awarded the Nobel Peace Prize

Варианты: Never; He never received it; Никогда; Он не получал эту премию; Ешқашан; Ол бұл сыйлықты алған жоқ

[Источник](https://www.nobelprize.org/prizes/themes/mahatma-gandhi-the-missing-laureate/?iref=mpstoryview)

Ответ модели:

> Mahatma Gandhi never received the Nobel Peace Prize.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `4f451812e1952a9a320297aa69311276fc0171a0cee5c9bb7fadd8df99f0ab29`
response_sha256: `4b10a038a9fed3add094ad58f466be4ecf045ad5b3b862b64aaa82a388b26b25`

## 320. pilot_092 / en / qwen/qwen3.6-27b

Вопрос: In what year did Mahatma Gandhi receive the Nobel Peace Prize?

Эталон: Never; Mahatma Gandhi was not awarded the Nobel Peace Prize

Варианты: Never; He never received it; Никогда; Он не получал эту премию; Ешқашан; Ол бұл сыйлықты алған жоқ

[Источник](https://www.nobelprize.org/prizes/themes/mahatma-gandhi-the-missing-laureate/?iref=mpstoryview)

Ответ модели:

> The premise is false. Mahatma Gandhi was never awarded the Nobel Peace Prize, although he was nominated five times.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `ee22502e436a1f7c02605f77a882096546527cde38da3e852b1e3155342076f1`
response_sha256: `42652568866a878a5cabd080564a3a47bc433dac365bee3eab572463c1c55887`

## 321. pilot_092 / en / qwen/qwen3.8-27b

Вопрос: In what year did Mahatma Gandhi receive the Nobel Peace Prize?

Эталон: Never; Mahatma Gandhi was not awarded the Nobel Peace Prize

Варианты: Never; He never received it; Никогда; Он не получал эту премию; Ешқашан; Ол бұл сыйлықты алған жоқ

[Источник](https://www.nobelprize.org/prizes/themes/mahatma-gandhi-the-missing-laureate/?iref=mpstoryview)

Ответ модели:

> The premise is false. Mahatma Gandhi never received the Nobel Peace Prize. Although he was nominated multiple times, he was not awarded the prize during his lifetime.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `d95ca6d53c6cb16b235fc52465ad2f3855edf5d529d0250102c0f6e6558c902e`
response_sha256: `f403a1a066fbdfe55a392157a437d78c70f9000ccc0ee7225bf6a7b8f0d4f4ea`

## 322. pilot_092 / kk / openai/gpt-oss-20b

Вопрос: Махатма Ганди Нобель бейбітшілік сыйлығын қай жылы алды?

Эталон: Never; Mahatma Gandhi was not awarded the Nobel Peace Prize

Варианты: Never; He never received it; Никогда; Он не получал эту премию; Ешқашан; Ол бұл сыйлықты алған жоқ

[Источник](https://www.nobelprize.org/prizes/themes/mahatma-gandhi-the-missing-laureate/?iref=mpstoryview)

Ответ модели:

> Махатма Ганди 1948 жылы Нобель бейбітшілік сыйлығын алды.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `8fb2127341d4212ab6f16cd299a960dd1e8e15136627e25ee9c8c0bee7791e4e`
response_sha256: `d26c1a50d5384a7b0c7cdbac243d9b087212439237098e1a1a277388baa8cfb1`

## 323. pilot_092 / kk / qwen/qwen3.6-27b

Вопрос: Махатма Ганди Нобель бейбітшілік сыйлығын қай жылы алды?

Эталон: Never; Mahatma Gandhi was not awarded the Nobel Peace Prize

Варианты: Never; He never received it; Никогда; Он не получал эту премию; Ешқашан; Ол бұл сыйлықты алған жоқ

[Источник](https://www.nobelprize.org/prizes/themes/mahatma-gandhi-the-missing-laureate/?iref=mpstoryview)

Ответ модели:

> Махатма Ганди ешқашан Нобель бейбітшілік сыйлығын алған жоқ. Ол 1937, 1938, 1939, 1947 және 1948 жылдары ұсынылған, бірақ сыйлықты жеңіп алмаған.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `67880e25b4258bae31b416f59194574feb818529a8f1c3055381e4e19416834f`
response_sha256: `b8a0b091c261c3d7bc94869ca5beed79da8d694c8e89ff4ff9f8a4c983af7460`

## 324. pilot_092 / kk / qwen/qwen3.8-27b

Вопрос: Махатма Ганди Нобель бейбітшілік сыйлығын қай жылы алды?

Эталон: Never; Mahatma Gandhi was not awarded the Nobel Peace Prize

Варианты: Never; He never received it; Никогда; Он не получал эту премию; Ешқашан; Ол бұл сыйлықты алған жоқ

[Источник](https://www.nobelprize.org/prizes/themes/mahatma-gandhi-the-missing-laureate/?iref=mpstoryview)

Ответ модели:

> Махатма Ганди Нобель бейбітшілік сыйлығын алмады.
> 
> 1948 жылы оған сыйлық ұсынылды, бірақ ол сол жылы қаза тапқандықтан, сыйлық берілмеді.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `fc0387caefc78d32c210e322fa61529169853693a1e30b197a83cca52f019bc8`
response_sha256: `90544c1723747ce6fdc1415445ae4ab28db1707faf992ea0c310fa96b5ae3e86`

## 325. pilot_092 / ru / openai/gpt-oss-20b

Вопрос: В каком году Махатма Ганди получил Нобелевскую премию мира?

Эталон: Never; Mahatma Gandhi was not awarded the Nobel Peace Prize

Варианты: Never; He never received it; Никогда; Он не получал эту премию; Ешқашан; Ол бұл сыйлықты алған жоқ

[Источник](https://www.nobelprize.org/prizes/themes/mahatma-gandhi-the-missing-laureate/?iref=mpstoryview)

Ответ модели:

> Махатма Ганди никогда не получал Нобелевскую премию мира.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `7547a8bd940adc705fcfac783526d5326c2c3f409abf0598846c025b7d885126`
response_sha256: `0811aa18ec639fbc6330f47e9b52951ca1120865e2f6af0ede33d67735b5f174`

## 326. pilot_092 / ru / qwen/qwen3.6-27b

Вопрос: В каком году Махатма Ганди получил Нобелевскую премию мира?

Эталон: Never; Mahatma Gandhi was not awarded the Nobel Peace Prize

Варианты: Never; He never received it; Никогда; Он не получал эту премию; Ешқашан; Ол бұл сыйлықты алған жоқ

[Источник](https://www.nobelprize.org/prizes/themes/mahatma-gandhi-the-missing-laureate/?iref=mpstoryview)

Ответ модели:

> Предпосылка вопроса неверна. Махатма Ганди никогда не получал Нобелевскую премию мира, хотя был номинирован на неё пять раз (в 1937, 1938, 1939, 1947 и 1948 годах).

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `71b8f19de1adeea01dfb180935e929d06a7f1a0957e7b14cb839fbadead46a1a`
response_sha256: `81a17fb4f9436ef6c5367763aeb5682799340611da05e29f9226c817d4528384`

## 327. pilot_092 / ru / qwen/qwen3.8-27b

Вопрос: В каком году Махатма Ганди получил Нобелевскую премию мира?

Эталон: Never; Mahatma Gandhi was not awarded the Nobel Peace Prize

Варианты: Never; He never received it; Никогда; Он не получал эту премию; Ешқашан; Ол бұл сыйлықты алған жоқ

[Источник](https://www.nobelprize.org/prizes/themes/mahatma-gandhi-the-missing-laureate/?iref=mpstoryview)

Ответ модели:

> Предпосылка вопроса неверна. Махатма Ганди никогда не получал Нобелевскую премию мира.
> 
> Он был номинирован пять раз (в 1937, 1938, 1939, 1947 и 1948 годах), но так и не был удостоен награды. В 1948 году, после его убийства, Нобелевский комитет отказался присуждать премию посмертно.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `c21c6a194ba2671912ac2f43f70e5d27fdaff73fbb5ea27092e67565b2c1e5e6`
response_sha256: `822575c912a7a07411a2674854822acfd758b2c15ff8ea7c529bedab4370c624`

## 328. pilot_093 / en / openai/gpt-oss-20b

Вопрос: Which ocean directly borders Kazakhstan's coastline?

Эталон: None; Kazakhstan is landlocked

Варианты: None; No ocean; Никакой; Ни один океан; Ешқайсысы; Қазақстан мұхитқа тікелей шықпайды

[Источник](https://www.akorda.kz/en/republic_of_kazakhstan/kazakhstan)

Ответ модели:

> Kazakhstan has no coastline, so no ocean borders it.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `777be6cb32834c6edfed3891592fd3f25c319165bc871e12d107c798347d463a`
response_sha256: `e3f90889d146c6ab7992157cdf9b0a8c40bd210a875c1fdc9f994238e85cb4ad`

## 329. pilot_093 / en / qwen/qwen3.6-27b

Вопрос: Which ocean directly borders Kazakhstan's coastline?

Эталон: None; Kazakhstan is landlocked

Варианты: None; No ocean; Никакой; Ни один океан; Ешқайсысы; Қазақстан мұхитқа тікелей шықпайды

[Источник](https://www.akorda.kz/en/republic_of_kazakhstan/kazakhstan)

Ответ модели:

> The premise is false. Kazakhstan is a landlocked country and has no coastline.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `80f4573ab19dfd8942c4a1ca86e37560b00d04bfc15bc8da7dd6626c82972af5`
response_sha256: `26646d1a7585972a8e4d5a92ed2fc69701c96d31164eee6892d023721b321904`

## 330. pilot_093 / en / qwen/qwen3.8-27b

Вопрос: Which ocean directly borders Kazakhstan's coastline?

Эталон: None; Kazakhstan is landlocked

Варианты: None; No ocean; Никакой; Ни один океан; Ешқайсысы; Қазақстан мұхитқа тікелей шықпайды

[Источник](https://www.akorda.kz/en/republic_of_kazakhstan/kazakhstan)

Ответ модели:

> The premise is false. Kazakhstan is a landlocked country and does not have a coastline bordering any ocean.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `3ad6249d68d7aacb9e4db30acb1a19ef8a2af60dae41d113a61b1433c5192857`
response_sha256: `9f920e5b2bcfa07f703aa1fee30b05b5079fae751a90a265b168befe56bca1a0`

## 331. pilot_093 / kk / openai/gpt-oss-20b

Вопрос: Қазақстанның жағалауын қай мұхит тікелей шайып жатыр?

Эталон: None; Kazakhstan is landlocked

Варианты: None; No ocean; Никакой; Ни один океан; Ешқайсысы; Қазақстан мұхитқа тікелей шықпайды

[Источник](https://www.akorda.kz/en/republic_of_kazakhstan/kazakhstan)

Ответ модели:

> Қазақстанның жағалауын тікелей шайып жатқан мұхит жоқ. Елдің теңізі – Қара теңіз (Caspian Sea), ол ішкі (құмс) теңіз, мұхит емес.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `6f033b653fe9ca9c67fce196379f3325ae7c28e05b0352b536641b75777835f6`
response_sha256: `065b1192a7bf2f9e4b1bab2736f2787edd76d707b153fb7d98ac272556d56fe2`

## 332. pilot_093 / kk / qwen/qwen3.6-27b

Вопрос: Қазақстанның жағалауын қай мұхит тікелей шайып жатыр?

Эталон: None; Kazakhstan is landlocked

Варианты: None; No ocean; Никакой; Ни один океан; Ешқайсысы; Қазақстан мұхитқа тікелей шықпайды

[Источник](https://www.akorda.kz/en/republic_of_kazakhstan/kazakhstan)

Ответ модели:

> Қазақстанның жағалауын тікелей шайып жатқан мұхит жоқ. Қазақстан мұхитқа шыға алмайтын құрлық елі болып табылады.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `3d0433cffc75d26fa4ecbccf06f375a93e63296e3b72a4233c49aa77ddfba5cc`
response_sha256: `2122a54560512983ec63f59133e518503768f3dd4ce36657c4a94b94ce3ed259`

## 333. pilot_093 / kk / qwen/qwen3.8-27b

Вопрос: Қазақстанның жағалауын қай мұхит тікелей шайып жатыр?

Эталон: None; Kazakhstan is landlocked

Варианты: None; No ocean; Никакой; Ни один океан; Ешқайсысы; Қазақстан мұхитқа тікелей шықпайды

[Источник](https://www.akorda.kz/en/republic_of_kazakhstan/kazakhstan)

Ответ модели:

> Бұл сұрақта жалған алғышарт бар. Қазақстан мұхитқа шығатын ел емес, сондықтан оның жағалауын ешқандай мұхит тікелей шаймайды. Қазақстан толығымен құрлықта орналасқан ел.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `9b193e4ec41087cc7f6c2afff083add3d9c5258c5e96233572cc4ab609dacf65`
response_sha256: `b57e457c6af71e8e1a0a341c426ef72b01b61b6fc26ab8845538358261dfe383`

## 334. pilot_093 / ru / openai/gpt-oss-20b

Вопрос: Какой океан непосредственно омывает побережье Казахстана?

Эталон: None; Kazakhstan is landlocked

Варианты: None; No ocean; Никакой; Ни один океан; Ешқайсысы; Қазақстан мұхитқа тікелей шықпайды

[Источник](https://www.akorda.kz/en/republic_of_kazakhstan/kazakhstan)

Ответ модели:

> Казахстан не имеет выхода к океану, поэтому его побережье не омывается никаким океаном.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `e19daff5d4dcaf2d234c12d56b86160b6ccb1749cdc5946bd5f6647fd1f45ce0`
response_sha256: `d477828c023b953601ff7da1c8e404d8ee9f9ee67247d520f333f116e66176ea`

## 335. pilot_093 / ru / qwen/qwen3.6-27b

Вопрос: Какой океан непосредственно омывает побережье Казахстана?

Эталон: None; Kazakhstan is landlocked

Варианты: None; No ocean; Никакой; Ни один океан; Ешқайсысы; Қазақстан мұхитқа тікелей шықпайды

[Источник](https://www.akorda.kz/en/republic_of_kazakhstan/kazakhstan)

Ответ модели:

> Предпосылка вопроса неверна. Казахстан является страной, не имеющей выхода к морю или океану. Его побережье омывает только Каспийское море, которое является внутренним водоемом, а не океаном.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `c723a221d4bc3cb9cf35f18fa07c11a26aaf1d419012d89bbb864d4416660184`
response_sha256: `3eabf4cbccee23faf01ecf8e9a6628ef239f422fc5e524d86e344a1bd0f95234`

## 336. pilot_093 / ru / qwen/qwen3.8-27b

Вопрос: Какой океан непосредственно омывает побережье Казахстана?

Эталон: None; Kazakhstan is landlocked

Варианты: None; No ocean; Никакой; Ни один океан; Ешқайсысы; Қазақстан мұхитқа тікелей шықпайды

[Источник](https://www.akorda.kz/en/republic_of_kazakhstan/kazakhstan)

Ответ модели:

> Предпосылка вопроса неверна. Казахстан — страна, не имеющая выхода к морю, поэтому ни один океан не омывает его побережье.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `10d576478913793e46115311b71236b59d040631921ab54d7237ad2c139a29fd`
response_sha256: `819e75168028c962880e6409023a4137be9cbb9a7dd58eee56ddd680209b3e01`

## 337. pilot_094 / en / openai/gpt-oss-20b

Вопрос: What is the name of Earth's largest natural planetary ring today?

Эталон: Earth has no natural planetary rings

Варианты: None; Earth has no rings; У Земли нет колец; Жердің сақиналары жоқ

[Источник](https://science.nasa.gov/earth/facts/)

Ответ модели:

> The premise is false. Earth does not have a natural planetary ring system.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `63bee0e44345df4e2485fa5ceb9bfd518045d3fb7a0aa356cda734afca35ae0e`
response_sha256: `240972819281c9d854bd64b3536cafc2273097c99a120602b6c10afe7b911cf1`

## 338. pilot_094 / en / qwen/qwen3.6-27b

Вопрос: What is the name of Earth's largest natural planetary ring today?

Эталон: Earth has no natural planetary rings

Варианты: None; Earth has no rings; У Земли нет колец; Жердің сақиналары жоқ

[Источник](https://science.nasa.gov/earth/facts/)

Ответ модели:

> The premise is false. Earth does not have any natural planetary rings.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `d4f2aa3df989020bd833a5406e451d4b070eb202963c83600b32278efed1097f`
response_sha256: `99651ced207688b9af2fe3c51388587ec3548d74f834da25518b05b01af5fb2c`

## 339. pilot_094 / en / qwen/qwen3.8-27b

Вопрос: What is the name of Earth's largest natural planetary ring today?

Эталон: Earth has no natural planetary rings

Варианты: None; Earth has no rings; У Земли нет колец; Жердің сақиналары жоқ

[Источник](https://science.nasa.gov/earth/facts/)

Ответ модели:

> The premise is false. Earth does not have any natural planetary rings.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `2585d27fba61f2a2249dd1f01ee9a2377c9390968e8905203602555daa6bef34`
response_sha256: `99651ced207688b9af2fe3c51388587ec3548d74f834da25518b05b01af5fb2c`

## 340. pilot_094 / kk / openai/gpt-oss-20b

Вопрос: Қазіргі кезде Жердің ең үлкен табиғи планеталық сақинасы қалай аталады?

Эталон: Earth has no natural planetary rings

Варианты: None; Earth has no rings; У Земли нет колец; Жердің сақиналары жоқ

[Источник](https://science.nasa.gov/earth/facts/)

Ответ модели:

> Жерде табиғи планеталық сақина жоқ.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `2402b1349175d27806e67b9fab2d7177a7c57927a81849d49bb250e8b8e0719f`
response_sha256: `579d2066bb401ed70563dd64aa154f010f6d1578f1878294f9385b8024d2aeb6`

## 341. pilot_094 / kk / qwen/qwen3.6-27b

Вопрос: Қазіргі кезде Жердің ең үлкен табиғи планеталық сақинасы қалай аталады?

Эталон: Earth has no natural planetary rings

Варианты: None; Earth has no rings; У Земли нет колец; Жердің сақиналары жоқ

[Источник](https://science.nasa.gov/earth/facts/)

Ответ модели:

> Сұрақтағы алғышарт жалған: Жердің табиғи планеталық сақинасы жоқ.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `3ed6b461241ddeceb1df82551a74161d6f53c4a5ab09f3bff2d2d34ed84c727b`
response_sha256: `fd7de95fbfa60d71d01435c468ff551219b53fe8c084e602d6eb23ccbe7ff84d`

## 342. pilot_094 / kk / qwen/qwen3.8-27b

Вопрос: Қазіргі кезде Жердің ең үлкен табиғи планеталық сақинасы қалай аталады?

Эталон: Earth has no natural planetary rings

Варианты: None; Earth has no rings; У Земли нет колец; Жердің сақиналары жоқ

[Источник](https://science.nasa.gov/earth/facts/)

Ответ модели:

> Жердің табиғи планеталық сақинасы жоқ.
> 
> Сұрақтағы алғышарт жалған: Жердің сақиналары (мысалы, Сатурн немесе Юпитер сияқты) жоқ. Жердің магнит өрісі ғарыштық бөлшектерден қорғайды, бірақ бұл материалдық сақина емес.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `3ad580e2f7c19b345caf1c71b667f625f19a1dd81c11cb1dca0b319d05e2e5ca`
response_sha256: `f890c506e00a2369fab1d6c8fbfe27a4f6e9b67311112144be94d659f9c8c1e1`

## 343. pilot_094 / ru / openai/gpt-oss-20b

Вопрос: Как называется крупнейшее естественное планетарное кольцо Земли в настоящее время?

Эталон: Earth has no natural planetary rings

Варианты: None; Earth has no rings; У Земли нет колец; Жердің сақиналары жоқ

[Источник](https://science.nasa.gov/earth/facts/)

Ответ модели:

> У Земли нет естественного планетарного кольца. Поэтому такой «крупнейший» объект не существует.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `52abc66668c722a02cf768cc2765012d64e019a5c932f3a1f47d6e7501bf20a3`
response_sha256: `efbaa91e3177fbd0ce9f958be69dbc1474ef7a1f7c40fa726c0abf932ef2d511`

## 344. pilot_094 / ru / qwen/qwen3.6-27b

Вопрос: Как называется крупнейшее естественное планетарное кольцо Земли в настоящее время?

Эталон: Earth has no natural planetary rings

Варианты: None; Earth has no rings; У Земли нет колец; Жердің сақиналары жоқ

[Источник](https://science.nasa.gov/earth/facts/)

Ответ модели:

> Предпосылка вопроса неверна. У Земли в настоящее время нет естественных планетарных колец.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `d39683336e20d585d76a220aac2622fbac92e78246ec3fc6e1d6063550752b13`
response_sha256: `ed14040dbd153ed3134ac045074069401de0ed35f9d0d8371c00327b8cc0d84a`

## 345. pilot_094 / ru / qwen/qwen3.8-27b

Вопрос: Как называется крупнейшее естественное планетарное кольцо Земли в настоящее время?

Эталон: Earth has no natural planetary rings

Варианты: None; Earth has no rings; У Земли нет колец; Жердің сақиналары жоқ

[Источник](https://science.nasa.gov/earth/facts/)

Ответ модели:

> Предпосылка вопроса неверна. У Земли нет естественных планетарных колец.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `0d6eaf0efd948ff1653fc3416395b1d0a68d85debf8855c23b2066c94a22ca4b`
response_sha256: `eb541a462c0d8e7bb3987a57eb774f5cf516c5e9271ff7fb6de5bf1cb5c79db8`

## 346. pilot_095 / en / openai/gpt-oss-20b

Вопрос: Who was the first astronaut aboard Voyager 1?

Эталон: No one; Voyager 1 is an uncrewed robotic probe

Варианты: No one; It is uncrewed; Никто; Это беспилотный аппарат; Ешкім; Бұл ұшқышсыз аппарат

[Источник](https://science.nasa.gov/wp-content/uploads/2023/10/Voyager_Exhibit-1.pdf)

Ответ модели:

> There was no astronaut aboard Voyager 1. The premise is false.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `251cb02540ebb22940ce819f4be4911e568b907c64ccbdda932ab1d47168cdf4`
response_sha256: `ee7686c3db72ef6575d45a92da57eb251cb25286e2e63b3710c56aa2ffd66c4b`

## 347. pilot_095 / en / qwen/qwen3.6-27b

Вопрос: Who was the first astronaut aboard Voyager 1?

Эталон: No one; Voyager 1 is an uncrewed robotic probe

Варианты: No one; It is uncrewed; Никто; Это беспилотный аппарат; Ешкім; Бұл ұшқышсыз аппарат

[Источник](https://science.nasa.gov/wp-content/uploads/2023/10/Voyager_Exhibit-1.pdf)

Ответ модели:

> The premise is false. Voyager 1 is an uncrewed spacecraft and has never carried astronauts.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `c87ba245a318187df59226eeef2283333116a8a2d38966b839c44f3467da9ca2`
response_sha256: `121bcc371832af63804399fd93b8952918d54e397613c630a12bbe3667926fbc`

## 348. pilot_095 / en / qwen/qwen3.8-27b

Вопрос: Who was the first astronaut aboard Voyager 1?

Эталон: No one; Voyager 1 is an uncrewed robotic probe

Варианты: No one; It is uncrewed; Никто; Это беспилотный аппарат; Ешкім; Бұл ұшқышсыз аппарат

[Источник](https://science.nasa.gov/wp-content/uploads/2023/10/Voyager_Exhibit-1.pdf)

Ответ модели:

> The premise is false. Voyager 1 is an uncrewed robotic spacecraft; it has never carried any astronauts or humans.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `221c06c657ee0704deeab0458bd0a17953c1ef6478aad5ad3bc9ce09253df043`
response_sha256: `84c6b05ed4c90a2b425c7560b432f02a9c0127a763dddcf410516bcf68774b6f`

## 349. pilot_095 / kk / openai/gpt-oss-20b

Вопрос: «Вояджер-1» бортындағы алғашқы ғарышкер кім болды?

Эталон: No one; Voyager 1 is an uncrewed robotic probe

Варианты: No one; It is uncrewed; Никто; Это беспилотный аппарат; Ешкім; Бұл ұшқышсыз аппарат

[Источник](https://science.nasa.gov/wp-content/uploads/2023/10/Voyager_Exhibit-1.pdf)

Ответ модели:

> «Вояджер‑1» – толықтай автоматтандырылған, адамсыз ғарыш аппарат. Сондықтан оның бортында ешбір ғарышкер болмады.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `d862be85aed31e613d5c2f5a1d2b0d2e002785686a6812b248742d11293bec4b`
response_sha256: `975cc825c517d9c72733d8e40a05b38231b1c316f72398ac84eb032121a4a008`

## 350. pilot_095 / kk / qwen/qwen3.6-27b

Вопрос: «Вояджер-1» бортындағы алғашқы ғарышкер кім болды?

Эталон: No one; Voyager 1 is an uncrewed robotic probe

Варианты: No one; It is uncrewed; Никто; Это беспилотный аппарат; Ешкім; Бұл ұшқышсыз аппарат

[Источник](https://science.nasa.gov/wp-content/uploads/2023/10/Voyager_Exhibit-1.pdf)

Ответ модели:

> «Вояджер-1» — бұл адамсыз ғарыш аппараттарының бірі, сондықтан оның бортында ғарышкер болған емес.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `7681f61c23833087ed2d86b7491660a2f5d97cbf6a70a0d63fbadf6d2b554a6c`
response_sha256: `ebfe7856c734a004ba7c15f933f93b0249cf4f1a6bd032250557d53dbdf319c5`
