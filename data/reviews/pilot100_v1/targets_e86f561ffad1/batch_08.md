# Проверка ответов моделей: pilot100_v1

Пакет 8. Номера 351–388. Это часть пилота, по уже полученным ответам; сбор остальных продолжается.

Оцените весь ответ: 1 — фактически верен, 0 — фактически неверен. Если случай неоднозначен или ответ оборван, оставьте пояснение вместо догадки. Для ложной предпосылки ответ должен явно её отвергать. Можно прислать номера и оценки в чат, указав название пакета.

Проверка эталонных фактов ранее не означает проверки этих ответов моделей.

## 351. pilot_096 / ru / qwen/qwen3.6-27b

Вопрос: Как называется самая высокая гора на твёрдой поверхности Солнца?

Эталон: None; the Sun has no solid surface

Варианты: None; The Sun has no solid surface; У Солнца нет твёрдой поверхности; Күннің қатты беті жоқ

[Источник](https://science.nasa.gov/sun/facts/)

Ответ модели:

> Предпосылка вопроса неверна. У Солнца нет твёрдой поверхности, поэтому на нём не может быть гор.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `f67efce64d8d494c5d9fb30ac44b17bc652f3a2565779fa94777633dcee15438`
response_sha256: `cbcc178528b1a8bfe633c7b4daaff48785c142897cbfac3b27bb9336a92d5d4f`

## 352. pilot_096 / ru / qwen/qwen3.8-27b

Вопрос: Как называется самая высокая гора на твёрдой поверхности Солнца?

Эталон: None; the Sun has no solid surface

Варианты: None; The Sun has no solid surface; У Солнца нет твёрдой поверхности; Күннің қатты беті жоқ

[Источник](https://science.nasa.gov/sun/facts/)

Ответ модели:

> Предпосылка вопроса неверна. У Солнца нет твёрдой поверхности; это звезда, состоящая из плазмы. Поэтому на Солнце не существует гор.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `e306b58ddc75e75ae5a987a8fb261d0bce746451a5e4cefd16a53bbf16dd62d6`
response_sha256: `74897de031e8691388b122f8194a1a56d468c5e7fadd0006c4b21e8a7b8f98c1`

## 353. pilot_097 / en / openai/gpt-oss-20b

Вопрос: In which season do bats lay their eggs?

Эталон: Bats do not lay eggs; they give birth to live young

Варианты: They do not lay eggs; Летучие мыши не откладывают яйца; Жарқанаттар жұмыртқа салмайды

[Источник](https://www.nps.gov/grba/learn/nature/bats.htm)

Ответ модели:
  
> Bats are mammals, so they give birth to live young rather than laying eggs. The premise that bats lay eggs is false.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `2f6df1c7c5c31c95a150ad48d7fac55769101cb0a9fa7db3e1cc9d9ec99dea51`
response_sha256: `237feb8e6cb0bdca58264caba1725c10b692d5ffb0764f575988d80608ce1475`

## 354. pilot_097 / en / qwen/qwen3.6-27b

Вопрос: In which season do bats lay their eggs?

Эталон: Bats do not lay eggs; they give birth to live young

Варианты: They do not lay eggs; Летучие мыши не откладывают яйца; Жарқанаттар жұмыртқа салмайды

[Источник](https://www.nps.gov/grba/learn/nature/bats.htm)

Ответ модели:

> The premise is false. Bats are mammals and do not lay eggs; they give birth to live young.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `04eb265224862ab73efeecd4a4ffd396389f81602b89b1b0d9fe9d4dbddb3bd2`
response_sha256: `403627ac4a0cc0be022cfb92a4463866f8ba61e3ec5872839fbab69d259f2694`

## 355. pilot_097 / en / qwen/qwen3.8-27b

Вопрос: In which season do bats lay their eggs?

Эталон: Bats do not lay eggs; they give birth to live young

Варианты: They do not lay eggs; Летучие мыши не откладывают яйца; Жарқанаттар жұмыртқа салмайды

[Источник](https://www.nps.gov/grba/learn/nature/bats.htm)

Ответ модели:

> The premise is false. Bats are mammals, not birds or reptiles, and therefore do not lay eggs. They give birth to live young.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `822168e4e1d81088647495b3551cd81a03a84dc230760fab17a55c987bf2ef5f`
response_sha256: `d3b9cb11635b2d785e23ee5e64020e5a9a5b9dc140b01f9f04885339ed5e82c7`

## 356. pilot_097 / kk / openai/gpt-oss-20b

Вопрос: Жарқанаттар жылдың қай мезгілінде жұмыртқа салады?

Эталон: Bats do not lay eggs; they give birth to live young

Варианты: They do not lay eggs; Летучие мыши не откладывают яйца; Жарқанаттар жұмыртқа салмайды

[Источник](https://www.nps.gov/grba/learn/nature/bats.htm)

Ответ модели:

> Жарқанаттар (құстар) жұмыртқа салады – жыл бойы, бірақ көбінесе көктемде (апрель‑маусым) жұмыртқаның саны көбеюде.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `a1c7870ee4cd6a5b82f2cee811c52a3d7913e2cd4ce23d5e93f6c23744054ef0`
response_sha256: `4eccc05bb8769e4e2489887175bcf682a7e8bca9054e59bfdb3025f7a5d73668`

## 357. pilot_097 / kk / qwen/qwen3.6-27b

Вопрос: Жарқанаттар жылдың қай мезгілінде жұмыртқа салады?

Эталон: Bats do not lay eggs; they give birth to live young

Варианты: They do not lay eggs; Летучие мыши не откладывают яйца; Жарқанаттар жұмыртқа салмайды

[Источник](https://www.nps.gov/grba/learn/nature/bats.htm)

Ответ модели:

> Жарқанаттар жұмыртқа салмайды, олар сүтқоректі жануарлар болғандықтан тірі туады.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `c75f83ccee6ecd8027c0ffd941d86d9ad74c39ad0f9ee61577b8d7e7a535df80`
response_sha256: `eb37e242348b66245d152bd9e3cdca0db6d7e4dff6af6c47de9d9f5cdc95526b`

## 358. pilot_097 / kk / qwen/qwen3.8-27b

Вопрос: Жарқанаттар жылдың қай мезгілінде жұмыртқа салады?

Эталон: Bats do not lay eggs; they give birth to live young

Варианты: They do not lay eggs; Летучие мыши не откладывают яйца; Жарқанаттар жұмыртқа салмайды

[Источник](https://www.nps.gov/grba/learn/nature/bats.htm)

Ответ модели:

> Жарқанаттар (бұл сөз қазақ тілінде кеңінен қолданылмайтын немесе қате аударылған термин болуы мүмкін, бірақ контекст бойынша "құстар" немесе нақты бір құс түрін білдіруі мүмкін) деген нақты бір құс түрін білдірмейді. Егер сіз **қарлығаш** (swallow) немесе **құс** туралы сұрап тұрсаңыз:
> 
> Қарлығаштар жыл сайын **көктемде** (әдетте сәуір-мамыр айларында) жұмыртқа салады.
> 
> Егер "жарқанат" деген сөзбен нақты бір құс түрін (мысалы, жарқанат құсы) меңзеген болсаңыз, бұл термин қазақ орнитологиясында стандартты емес. Нақтырақ айтсаңыз, дәлірек жауап бере аламын.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `66a4869ceed10e92ca4a49d6022e0d4b87c18590e50f62c30a9f1096e92b00d2`
response_sha256: `7dad4a6bdb1a662bb6d48e735ff18767d90bc02f975b82599e589306ae178055`

## 359. pilot_097 / ru / openai/gpt-oss-20b

Вопрос: В какое время года летучие мыши откладывают яйца?

Эталон: Bats do not lay eggs; they give birth to live young

Варианты: They do not lay eggs; Летучие мыши не откладывают яйца; Жарқанаттар жұмыртқа салмайды

[Источник](https://www.nps.gov/grba/learn/nature/bats.htm)

Ответ модели:

> Летучие мыши не откладывают яйца – это млекопитающие, которые рождают живых детёнышей.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `2cb990c5ab6beedd7b164a3405768082cb82851ea7db1d549e64be6d773bca0b`
response_sha256: `efe396a88a945605ec6d016761a37bdd2a79fd64be8ac43f9f409b3d3b70636a`

## 360. pilot_097 / ru / qwen/qwen3.6-27b

Вопрос: В какое время года летучие мыши откладывают яйца?

Эталон: Bats do not lay eggs; they give birth to live young

Варианты: They do not lay eggs; Летучие мыши не откладывают яйца; Жарқанаттар жұмыртқа салмайды

[Источник](https://www.nps.gov/grba/learn/nature/bats.htm)

Ответ модели:

> Предпосылка вопроса неверна. Летучие мыши — это млекопитающие, они не откладывают яйца, а рождают живых детенышей.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `ad960a68232b1e20b5e9922db66b32f0c773542c77c74c79667a3e06480eddd2`
response_sha256: `54c6b43573bc04c5517c65506ddf4cb5a5e17a612b6ed7afa43ec9ecdae41a48`

## 361. pilot_097 / ru / qwen/qwen3.8-27b

Вопрос: В какое время года летучие мыши откладывают яйца?

Эталон: Bats do not lay eggs; they give birth to live young

Варианты: They do not lay eggs; Летучие мыши не откладывают яйца; Жарқанаттар жұмыртқа салмайды

[Источник](https://www.nps.gov/grba/learn/nature/bats.htm)

Ответ модели:

> Предпосылка вопроса неверна. Летучие мыши — это млекопитающие, а не птицы или рептилии, поэтому они не откладывают яйца. Они рождают живых детёнышей.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `2f6a637a23b8f1ee3ab767cf255b603fcc9f690c53d15a8a593233e760ce73b7`
response_sha256: `c10e320551a56904184e56ce2d3885938239634df0fcde463935fcdb9c7e959d`

## 362. pilot_098 / en / openai/gpt-oss-20b

Вопрос: What is the name of Venus's widest natural planetary ring?

Эталон: Venus has no planetary rings

Варианты: None; Venus has no rings; У Венеры нет колец; Шолпанның сақиналары жоқ

[Источник](https://science.nasa.gov/venus/venus-facts/)

Ответ модели:

> Venus does not have any natural planetary rings, so the premise is false.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `c030c822a6e20b2e97eea76c19de5a492cd540d0e060d388a64f400832e5ddc8`
response_sha256: `f61a9b8c1e621c9e54d389fab530709d73c5f147af6f9de38d1f73e93435d2b8`

## 363. pilot_098 / en / qwen/qwen3.6-27b

Вопрос: What is the name of Venus's widest natural planetary ring?

Эталон: Venus has no planetary rings

Варианты: None; Venus has no rings; У Венеры нет колец; Шолпанның сақиналары жоқ

[Источник](https://science.nasa.gov/venus/venus-facts/)

Ответ модели:

> The premise is false. Venus does not have any natural planetary rings.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `385571a8a5cbd5d81cd81fef32a2c7936f0c8b189bf892477b56ea8226b54721`
response_sha256: `8795ed480b0b3786af6c47d083b75eb609373a1cd32ae677025f5c9a11a9b0a1`

## 364. pilot_098 / en / qwen/qwen3.8-27b

Вопрос: What is the name of Venus's widest natural planetary ring?

Эталон: Venus has no planetary rings

Варианты: None; Venus has no rings; У Венеры нет колец; Шолпанның сақиналары жоқ

[Источник](https://science.nasa.gov/venus/venus-facts/)

Ответ модели:

> The premise is false. Venus does not have any natural planetary rings.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `112c68e97028e861f9d0e4dd86854630ceec7456ae1d41ca1eeea3ebb2c99d20`
response_sha256: `8795ed480b0b3786af6c47d083b75eb609373a1cd32ae677025f5c9a11a9b0a1`

## 365. pilot_098 / kk / openai/gpt-oss-20b

Вопрос: Шолпанның ең жалпақ табиғи планеталық сақинасы қалай аталады?

Эталон: Venus has no planetary rings

Варианты: None; Venus has no rings; У Венеры нет колец; Шолпанның сақиналары жоқ

[Источник](https://science.nasa.gov/venus/venus-facts/)

Ответ модели:

> Шолпан – бұл планета емес, сондықтан оның табиғи планеталық сақиналары жоқ. Алгебралық немесе ғылыми тұрғыдан шолпанға қатысты «ең жалпақ» табиғи сақина деген ұғым жоқ.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `0477ad99f20735d70bbf52afbaf46c41e5644b871c54cfbff372110ed3f41ab5`
response_sha256: `182f5393e9ebf8f17a517950451aa11b69dc7749aebdf33dc20398084961173b`

## 366. pilot_098 / kk / qwen/qwen3.6-27b

Вопрос: Шолпанның ең жалпақ табиғи планеталық сақинасы қалай аталады?

Эталон: Venus has no planetary rings

Варианты: None; Venus has no rings; У Венеры нет колец; Шолпанның сақиналары жоқ

[Источник](https://science.nasa.gov/venus/venus-facts/)

Ответ модели:

> Шолпан (Венера) планетасында табиғи сақиналар жоқ. Сондықтан оның «ең жалпақ сақинасы» деген ұғым қате, себебі бұл планетаның сақина жүйесі мүлдем болмайды.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `57039eff34557a4457ceb201a7e57c2a8f7887f60f6a0040ecb6608387c4d119`
response_sha256: `7b81b6b770e54ac25c858a3f1c3c876cfbf09cabeed2fe890cfe61dbbe593726`

## 367. pilot_098 / kk / qwen/qwen3.8-27b

Вопрос: Шолпанның ең жалпақ табиғи планеталық сақинасы қалай аталады?

Эталон: Venus has no planetary rings

Варианты: None; Venus has no rings; У Венеры нет колец; Шолпанның сақиналары жоқ

[Источник](https://science.nasa.gov/venus/venus-facts/)

Ответ модели:

> Сұрақта жалған алғышарт бар. Шолпан (Венера) планетасының табиғи сақиналары жоқ. Сондықтан оның "ең жалпақ сақинасы" деген ұғым өзінен-өзі қате.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `b678b87bf1266288a4fb7b182ec1863ac1f2145476324058eae78b1c768f12b7`
response_sha256: `80334ff0cc10b6c4c06f9b3646d708e028baeddb0404e67e83a14ca02a0921f4`

## 368. pilot_098 / ru / openai/gpt-oss-20b

Вопрос: Как называется самое широкое естественное планетарное кольцо Венеры?

Эталон: Venus has no planetary rings

Варианты: None; Venus has no rings; У Венеры нет колец; Шолпанның сақиналары жоқ

[Источник](https://science.nasa.gov/venus/venus-facts/)

Ответ модели:

> Венера не имеет естественных планетарных колец. Поэтому вопрос основан на неверной предпосылке.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `1702197160a5acb3cd0a0855011e4cefef0b585a6403940cc7216711729626d8`
response_sha256: `9a01441909f56f035598bed5169a3a449bb9e4a96054c8810ac1e706583cd7ca`

## 369. pilot_098 / ru / qwen/qwen3.6-27b

Вопрос: Как называется самое широкое естественное планетарное кольцо Венеры?

Эталон: Venus has no planetary rings

Варианты: None; Venus has no rings; У Венеры нет колец; Шолпанның сақиналары жоқ

[Источник](https://science.nasa.gov/venus/venus-facts/)

Ответ модели:

> Предпосылка вопроса неверна: у Венеры нет естественных планетарных колец.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `1c653135c2dd3e7fafcbbdb21f0a19d7aad36772c490f3763e63a0c3cc44d205`
response_sha256: `bb354bef03241e1411a762d4bed10bd401b55fa2341790ac9ade64734adcbffa`

## 370. pilot_098 / ru / qwen/qwen3.8-27b

Вопрос: Как называется самое широкое естественное планетарное кольцо Венеры?

Эталон: Venus has no planetary rings

Варианты: None; Venus has no rings; У Венеры нет колец; Шолпанның сақиналары жоқ

[Источник](https://science.nasa.gov/venus/venus-facts/)

Ответ модели:

> Предпосылка вопроса неверна. У Венеры нет естественных планетарных колец.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `4ad37389bdc2fa98e482da4c250d0f595cc499d15415a9fa2244e70020dd5465`
response_sha256: `f3d50005b4924bb079fba6935a9782108b8fdcc6f0bac9b62738ec51b0da0b38`

## 371. pilot_099 / en / openai/gpt-oss-20b

Вопрос: Which species of polar bear is native to Antarctica?

Эталон: None; polar bears are not native to Antarctica

Варианты: None; There are no polar bears in Antarctica; В Антарктиде нет белых медведей; Антарктидада ақ аюлар жоқ

[Источник](https://www.bas.ac.uk/blogpost/halley-diary-march-2013/)

Ответ модели:

> There is no species of polar bear native to Antarctica. Polar bears are found only in the Arctic region.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `be93a6cf35f1fb96b40c101192e11e3cf403184e82dafc5375a5e91ca6cb0179`
response_sha256: `d329499222dacbc5dcbec3de10e1cfa4b62d17f762b8886643992ba0b03bf70e`

## 372. pilot_099 / en / qwen/qwen3.6-27b

Вопрос: Which species of polar bear is native to Antarctica?

Эталон: None; polar bears are not native to Antarctica

Варианты: None; There are no polar bears in Antarctica; В Антарктиде нет белых медведей; Антарктидада ақ аюлар жоқ

[Источник](https://www.bas.ac.uk/blogpost/halley-diary-march-2013/)

Ответ модели:

> The premise is false. Polar bears are native to the Arctic region in the Northern Hemisphere, not Antarctica in the Southern Hemisphere. There are no wild polar bears in Antarctica.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `b1dccd8c356dc108742c36bb91f53789f8c4c45004c34cbdfe91cbde5e96500d`
response_sha256: `e437e0aa2ab70d6f3bf978d3bb354c70ad9fb95b0a9145ef24e609b6eefb9a82`

## 373. pilot_099 / en / qwen/qwen3.8-27b

Вопрос: Which species of polar bear is native to Antarctica?

Эталон: None; polar bears are not native to Antarctica

Варианты: None; There are no polar bears in Antarctica; В Антарктиде нет белых медведей; Антарктидада ақ аюлар жоқ

[Источник](https://www.bas.ac.uk/blogpost/halley-diary-march-2013/)

Ответ модели:

> The premise is false. Polar bears are native to the Arctic region (the North Pole), not Antarctica. There are no wild polar bears in Antarctica.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `2435ea335727bd384de14e935fde8e474f9b1e8e757315f7fad4516fdb947a8c`
response_sha256: `335fbdb9117e67852af6fe903f866a6736107f2c99203bc21cfdcb1a8973aef9`

## 374. pilot_099 / kk / openai/gpt-oss-20b

Вопрос: Ақ аюдың қай түрі Антарктидада табиғи түрде мекендейді?

Эталон: None; polar bears are not native to Antarctica

Варианты: None; There are no polar bears in Antarctica; В Антарктиде нет белых медведей; Антарктидада ақ аюлар жоқ

[Источник](https://www.bas.ac.uk/blogpost/halley-diary-march-2013/)

Ответ модели:

> Ақ аю (Ursus arctos) – Антарктидада табиғи түрде мекендейтін түрі жоқ.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `6de8489396840a056e07a69ea66158543ad2af3964434ddd0b4d37573ac4e8b3`
response_sha256: `339c80800ed10b10ad584e7d21abfb22a543a04854359249e1785dcaa3ad5b0e`

## 375. pilot_099 / kk / qwen/qwen3.6-27b

Вопрос: Ақ аюдың қай түрі Антарктидада табиғи түрде мекендейді?

Эталон: None; polar bears are not native to Antarctica

Варианты: None; There are no polar bears in Antarctica; В Антарктиде нет белых медведей; Антарктидада ақ аюлар жоқ

[Источник](https://www.bas.ac.uk/blogpost/halley-diary-march-2013/)

Ответ модели:

> Ақ аюлар Антарктидада табиғи түрде мекендемейді. Бұл сұрақта жалған алғышарт бар. Ақ аюлар тек Солтүстік мұзды мұхит аймағында (Арктикада) тіршілік етеді.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `4eaef249330a3a609772a192ff7e7fa7eca5edc1fa015fa84bc19a1309bb14f2`
response_sha256: `70a926d6bd6dfa3260b4f03fbb0d88450fe98fecf7de188f399f7db2bd7ed8f1`

## 376. pilot_099 / kk / qwen/qwen3.8-27b

Вопрос: Ақ аюдың қай түрі Антарктидада табиғи түрде мекендейді?

Эталон: None; polar bears are not native to Antarctica

Варианты: None; There are no polar bears in Antarctica; В Антарктиде нет белых медведей; Антарктидада ақ аюлар жоқ

[Источник](https://www.bas.ac.uk/blogpost/halley-diary-march-2013/)

Ответ модели:

> Сұрақтағы алғышарт жалған. Ақ аюлар (белуга немесе басқа түрлері) Антарктидада табиғи түрде мекендемейді. Антарктидада аюлар жоқ, ал ақ аюлар (белуга) Солтүстік Поляр аймағында, яғни Арктикада мекендейді.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `ae38ea058ab4060fe6fa023289c10f37a885379993b6db283080119398128244`
response_sha256: `77b9d018351ae644ff8f4f4b8486844d4fa28256609953e62c463d77abe51998`

## 377. pilot_099 / ru / openai/gpt-oss-20b

Вопрос: Какой вид белого медведя является коренным для Антарктиды?

Эталон: None; polar bears are not native to Antarctica

Варианты: None; There are no polar bears in Antarctica; В Антарктиде нет белых медведей; Антарктидада ақ аюлар жоқ

[Источник](https://www.bas.ac.uk/blogpost/halley-diary-march-2013/)

Ответ модели:

> В Антарктиде нет белых медведей. Это неверная предпосылка.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `ecb6420ca6766220841ac53cb7f86eccd3b3b338942c5f5a536fca27b545dbfd`
response_sha256: `13d2f999eead1b93c312561741a8d29db6f458baf014b714430d8438914358fd`

## 378. pilot_099 / ru / qwen/qwen3.6-27b

Вопрос: Какой вид белого медведя является коренным для Антарктиды?

Эталон: None; polar bears are not native to Antarctica

Варианты: None; There are no polar bears in Antarctica; В Антарктиде нет белых медведей; Антарктидада ақ аюлар жоқ

[Источник](https://www.bas.ac.uk/blogpost/halley-diary-march-2013/)

Ответ модели:

> Предпосылка вопроса неверна. Белые медведи не обитают в Антарктиде; их естественная среда обитания — Арктика (Северное полушарие). В Антарктиде (Южное полушарие) белые медведи не встречаются.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `e71af3fac4cdf65ef9751678bd82bbaae052b5295182e7f3e4d5932786871f11`
response_sha256: `16d4ca36b688a14c99cf716ba8bbed11d1b929c6ef42f2869aaf92b00843a5ef`

## 379. pilot_099 / ru / qwen/qwen3.8-27b

Вопрос: Какой вид белого медведя является коренным для Антарктиды?

Эталон: None; polar bears are not native to Antarctica

Варианты: None; There are no polar bears in Antarctica; В Антарктиде нет белых медведей; Антарктидада ақ аюлар жоқ

[Источник](https://www.bas.ac.uk/blogpost/halley-diary-march-2013/)

Ответ модели:

> Предпосылка вопроса неверна. Белые медведи не обитают в Антарктиде. Их естественная среда обитания — Арктика (Северный полюс и прилегающие к нему территории). В Антарктиде нет медведей вообще.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `b46a94337e9bfbe114f77fc141ed71706fdd0b25b790b5a0651e305d2abd82bf`
response_sha256: `7e482d4f39d709e8365d8dc9993eaa9285edf4fd422257f12ae0c7c0d3d85649`

## 380. pilot_100 / en / openai/gpt-oss-20b

Вопрос: In what year did Marie Curie win the Nobel Prize in Literature?

Эталон: Never; Marie Curie's Nobel Prizes were in Physics and Chemistry

Варианты: Never; She did not win a Literature prize; Никогда; Она не получала премию по литературе; Ешқашан; Ол әдебиет сыйлығын алған жоқ

[Источник](https://www.nobelprize.org/nomination/archive/show_people.php?id=2051&lang=en)

Ответ модели:

> Marie Curie never won a Nobel Prize in Literature. She received the Nobel Prize in Physics in 1903 and the Nobel Prize in Chemistry in 1911.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `be14b27f5e582362506fe9284c5c8e5aa49cd3269bbaccdf65da21c44bd3f742`
response_sha256: `e1204f02ecf1750f0023e821bd35dee043d09c12784499359bbaad61dac1683e`

## 381. pilot_100 / en / qwen/qwen3.6-27b

Вопрос: In what year did Marie Curie win the Nobel Prize in Literature?

Эталон: Never; Marie Curie's Nobel Prizes were in Physics and Chemistry

Варианты: Never; She did not win a Literature prize; Никогда; Она не получала премию по литературе; Ешқашан; Ол әдебиет сыйлығын алған жоқ

[Источник](https://www.nobelprize.org/nomination/archive/show_people.php?id=2051&lang=en)

Ответ модели:

> The premise is false. Marie Curie never won the Nobel Prize in Literature. She won the Nobel Prize in Physics in 1903 and the Nobel Prize in Chemistry in 1911.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `081420e64206939772a239c4023d8853a532e8267bd71fe9e4f4d7f9c2391c68`
response_sha256: `ef63bf23792372b8aec5010c78ab7c458e39974df2c8c842c8964640a1a5b21f`

## 382. pilot_100 / en / qwen/qwen3.8-27b

Вопрос: In what year did Marie Curie win the Nobel Prize in Literature?

Эталон: Never; Marie Curie's Nobel Prizes were in Physics and Chemistry

Варианты: Never; She did not win a Literature prize; Никогда; Она не получала премию по литературе; Ешқашан; Ол әдебиет сыйлығын алған жоқ

[Источник](https://www.nobelprize.org/nomination/archive/show_people.php?id=2051&lang=en)

Ответ модели:

> The premise is false. Marie Curie never won the Nobel Prize in Literature. She won the Nobel Prize in Physics in 1903 and the Nobel Prize in Chemistry in 1911.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `ba0f15211ac16cb553941cfdba4944e01efb13423a7094f090ab7cda7aa91dc1`
response_sha256: `ef63bf23792372b8aec5010c78ab7c458e39974df2c8c842c8964640a1a5b21f`

## 383. pilot_100 / kk / openai/gpt-oss-20b

Вопрос: Мария Кюри әдебиет саласындағы Нобель сыйлығын қай жылы алды?

Эталон: Never; Marie Curie's Nobel Prizes were in Physics and Chemistry

Варианты: Never; She did not win a Literature prize; Никогда; Она не получала премию по литературе; Ешқашан; Ол әдебиет сыйлығын алған жоқ

[Источник](https://www.nobelprize.org/nomination/archive/show_people.php?id=2051&lang=en)

Ответ модели:

> Мария Кюри әдебиет саласындағы Нобель сыйлығын ешқашан алған жоқ. Ол 1903 жылы физика, 1911 жылы химия саласында Нобель сыйлығын жеңіп алды.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `18b0574d7eb6ecd207167ffefe1818cd0807fe527bd40541c722efa625afed97`
response_sha256: `33feee8edf8d8ddba25a565adc5f43fcbe2a84024bf40cb074a273b7de912836`

## 384. pilot_100 / kk / qwen/qwen3.6-27b

Вопрос: Мария Кюри әдебиет саласындағы Нобель сыйлығын қай жылы алды?

Эталон: Never; Marie Curie's Nobel Prizes were in Physics and Chemistry

Варианты: Never; She did not win a Literature prize; Никогда; Она не получала премию по литературе; Ешқашан; Ол әдебиет сыйлығын алған жоқ

[Источник](https://www.nobelprize.org/nomination/archive/show_people.php?id=2051&lang=en)

Ответ модели:

> Мария Кюри әдебиет саласында Нобель сыйлығын алған жоқ. Ол физика (1903) және химия (1911) салалары бойынша Нобель сыйлығын алған алғашқы әйел ғалым.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `33697470ff835ae54583fd40fc59e187bf52f4629256486d9e6ee007d54ec2c9`
response_sha256: `916b3905895642f43f0f17deaf38675afce9843791896d7f0e6cf7abaae3e523`

## 385. pilot_100 / kk / qwen/qwen3.8-27b

Вопрос: Мария Кюри әдебиет саласындағы Нобель сыйлығын қай жылы алды?

Эталон: Never; Marie Curie's Nobel Prizes were in Physics and Chemistry

Варианты: Never; She did not win a Literature prize; Никогда; Она не получала премию по литературе; Ешқашан; Ол әдебиет сыйлығын алған жоқ

[Источник](https://www.nobelprize.org/nomination/archive/show_people.php?id=2051&lang=en)

Ответ модели:

> Сұрақтағы алғышарт жалған. Мария Кюри әдебиет саласында Нобель сыйлығын алмаған. Ол 1903 жылы физика және 1911 жылы химия салаларында Нобель сыйлығын иеленген.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `9842fcb7f97c35843b4310a4b0c820fb4856d3ca1d4133c3d8f83a13335e988f`
response_sha256: `c0bfccd8c13c5f067d38a8e0220dc000a90bd9f3cb685cbb08b1af005ef5ff6a`

## 386. pilot_100 / ru / openai/gpt-oss-20b

Вопрос: В каком году Мария Кюри получила Нобелевскую премию по литературе?

Эталон: Never; Marie Curie's Nobel Prizes were in Physics and Chemistry

Варианты: Never; She did not win a Literature prize; Никогда; Она не получала премию по литературе; Ешқашан; Ол әдебиет сыйлығын алған жоқ

[Источник](https://www.nobelprize.org/nomination/archive/show_people.php?id=2051&lang=en)

Ответ модели:

> Мария Кюри никогда не получала Нобелевскую премию по литературе. Она была удостоена Нобелевских премий по физике (1903) и химии (1911).

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `ff53448cddb1eaab14720e0c2f5d986dfb3f72a0af2b1e436239088241d327ed`
response_sha256: `60d44abfa1e2b2b42ab36bfa33f369bdcdc58e0b3a4873b22b629fb13fad3c73`

## 387. pilot_100 / ru / qwen/qwen3.6-27b

Вопрос: В каком году Мария Кюри получила Нобелевскую премию по литературе?

Эталон: Never; Marie Curie's Nobel Prizes were in Physics and Chemistry

Варианты: Never; She did not win a Literature prize; Никогда; Она не получала премию по литературе; Ешқашан; Ол әдебиет сыйлығын алған жоқ

[Источник](https://www.nobelprize.org/nomination/archive/show_people.php?id=2051&lang=en)

Ответ модели:

> Предпосылка вопроса неверна. Мария Кюри никогда не получала Нобелевскую премию по литературе.
> 
> Она дважды лауреат Нобелевской премии по физике (1903 год) и по химии (1911 год).

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `45e4568129fe2ef87c4e41bdb334b9b2f60a5240fbd914968f364e0a8de56c9d`
response_sha256: `aa3ac0e38cb7bdff1f30b8d7f783514046c3c243e3d9180d2282a41be940124f`

## 388. pilot_100 / ru / qwen/qwen3.8-27b

Вопрос: В каком году Мария Кюри получила Нобелевскую премию по литературе?

Эталон: Never; Marie Curie's Nobel Prizes were in Physics and Chemistry

Варианты: Never; She did not win a Literature prize; Никогда; Она не получала премию по литературе; Ешқашан; Ол әдебиет сыйлығын алған жоқ

[Источник](https://www.nobelprize.org/nomination/archive/show_people.php?id=2051&lang=en)

Ответ модели:

> Предпосылка вопроса неверна. Мария Кюри никогда не получала Нобелевскую премию по литературе.
> 
> Она дважды получала Нобелевскую премию:
> 1. В 1903 году — по физике (совместно с Пьером Кюри и Анри Беккерелем).
> 2. В 1911 году — по химии.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `7fe5d8309ec6500283ac7d812dff4f8d42c16632808945d139e21a6279ecbae1`
response_sha256: `b7ed4df7e7171be5958ae4c1cb5eb80f69c51350c96ff68f17fa2891db6de360`
