# Проверка ответов моделей: pilot100_v1

Пакет 1. Номера 1–50. Это часть пилота, по уже полученным ответам; сбор остальных продолжается.

Оцените весь ответ: 1 — фактически верен, 0 — фактически неверен. Если случай неоднозначен или ответ оборван, оставьте пояснение вместо догадки. Для ложной предпосылки ответ должен явно её отвергать. Можно прислать номера и оценки в чат, указав название пакета.

Проверка эталонных фактов ранее не означает проверки этих ответов моделей.

## 1. pilot_001 / en / openai/gpt-oss-20b

Вопрос: Who commanded Apollo 11?

Эталон: Neil Armstrong

Варианты: Нил Армстронг; Ніл Армстронг

[Источник](https://www.nasa.gov/the-apollo-program/)

Ответ модели:

> The commander of Apollo 11 was Neil Armstrong.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `de0c0acaa7064bcd57304418fc326b1a1962e2e61ffbb42db51d71e177c687d4`
response_sha256: `2a7f036535a8f79da420a530f043f3b3643b76159dd5a99fa0734b235c061fd0`

## 2. pilot_001 / kk / openai/gpt-oss-20b

Вопрос: «Аполлон-11» миссиясының командирі кім болды?

Эталон: Neil Armstrong

Варианты: Нил Армстронг; Ніл Армстронг

[Источник](https://www.nasa.gov/the-apollo-program/)

Ответ модели:

> Аполлон‑11 миссиясының командирі Ніл Армстронг болды.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `8379f80a18c506d6db7d193bbbc1b787466095741bae3422b1ef9c8e7f1fdee5`
response_sha256: `c9699538e82b2942ea705e8deae9825f51fffd3f24a64e27f9254130d7645d9c`

## 3. pilot_001 / kk / qwen/qwen3.6-27b

Вопрос: «Аполлон-11» миссиясының командирі кім болды?

Эталон: Neil Armstrong

Варианты: Нил Армстронг; Ніл Армстронг

[Источник](https://www.nasa.gov/the-apollo-program/)

Ответ модели:

> «Аполлон-11» миссиясының командирі Нил Армстронг болды.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `69f640be971ae51159e08c37747d2983f48741139825e9d52d582d778a4bc13e`
response_sha256: `4942474e5ce751c12ae304168dc5d1f89ca05a98fd40781a999dfce04964e35c`

## 4. pilot_001 / kk / qwen/qwen3.8-27b

Вопрос: «Аполлон-11» миссиясының командирі кім болды?

Эталон: Neil Armstrong

Варианты: Нил Армстронг; Ніл Армстронг

[Источник](https://www.nasa.gov/the-apollo-program/)

Ответ модели:

> «Аполлон-11» миссиясының командирі Нил Армстронг болды.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `7866a71831e515b98893cc6ce1a87a49ccf835b13002edffc1ad7f58e6484477`
response_sha256: `4942474e5ce751c12ae304168dc5d1f89ca05a98fd40781a999dfce04964e35c`

## 5. pilot_001 / ru / openai/gpt-oss-20b

Вопрос: Кто командовал миссией «Аполлон-11»?

Эталон: Neil Armstrong

Варианты: Нил Армстронг; Ніл Армстронг

[Источник](https://www.nasa.gov/the-apollo-program/)

Ответ модели:

> Командовал миссией «Аполлон‑11» астронавт Нейл А. Армстронг.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `57e78e53ad5f09fcab282c379f746f38f17d4870fc7fb3e1d7224a7245db2c01`
response_sha256: `5be40ab79deaf5f5395b68619c8eee4b5f1c8bd507f13a8ed6d055e78c713a3d`

## 6. pilot_001 / ru / qwen/qwen3.6-27b

Вопрос: Кто командовал миссией «Аполлон-11»?

Эталон: Neil Armstrong

Варианты: Нил Армстронг; Ніл Армстронг

[Источник](https://www.nasa.gov/the-apollo-program/)

Ответ модели:

> Миссией «Аполлон-11» командовал Нил Армстронг.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `50b1c3f67083fae284c06e071fa38423efa5ae790705e82ac325fa9bd221451c`
response_sha256: `5f89d009268381fe9d2aea5ae05603fdea5c69f8b8851a26bfeb27485f95fe4e`

## 7. pilot_001 / ru / qwen/qwen3.8-27b

Вопрос: Кто командовал миссией «Аполлон-11»?

Эталон: Neil Armstrong

Варианты: Нил Армстронг; Ніл Армстронг

[Источник](https://www.nasa.gov/the-apollo-program/)

Ответ модели:

> Командиром миссии «Аполлон-11» был Нил Армстронг.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `f8bdcf2804ddcec56711efde7b2b63839c9dd0602e4412cc4cb3b539c03e25a5`
response_sha256: `de8007ea6e0539b778511ea6a2cf58754c63804621aa983ff55cf3d6b7e68a56`

## 8. pilot_002 / en / openai/gpt-oss-20b

Вопрос: Which Apollo mission was the first to carry a crew?

Эталон: Apollo 7

Варианты: Apollo-7; Аполлон-7; Аполлон 7

[Источник](https://www.nasa.gov/the-apollo-program/)

Ответ модели:

> The first Apollo mission to carry a crew was **Apollo 7**.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `bb3d782948ba557edd3db52c59c367ba6c8bf5cfd2df7bd6cba1b7be87e2ff1e`
response_sha256: `8af71c446b9993c8d6c1766ca82c577c181c94c65a6ca02d9159ee778e86eceb`

## 9. pilot_002 / kk / openai/gpt-oss-20b

Вопрос: «Аполлон» бағдарламасының қай миссиясы алғаш рет экипажбен ұшты?

Эталон: Apollo 7

Варианты: Apollo-7; Аполлон-7; Аполлон 7

[Источник](https://www.nasa.gov/the-apollo-program/)

Ответ модели:

> Аполлон бағдарламасының алғашқы экипажбен ұшуы **Apollo 7** болды.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `626fbc9a74e05a46522de37e8256ba5a89ec304c9b250ff1f282589340af5d4a`
response_sha256: `e785ea601246b6f495c3a307cdeaf93f31060e2c12be2f79081db8a9a9e9cec0`

## 10. pilot_002 / kk / qwen/qwen3.6-27b

Вопрос: «Аполлон» бағдарламасының қай миссиясы алғаш рет экипажбен ұшты?

Эталон: Apollo 7

Варианты: Apollo-7; Аполлон-7; Аполлон 7

[Источник](https://www.nasa.gov/the-apollo-program/)

Ответ модели:

> «Аполлон-7» миссиясы.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `f9bc7d0c42aa3c4e9b3607abc47808bb9759ad46cb71356d3cbb61df28848996`
response_sha256: `20937d75a8d0017f2ea8d035721ed17a7534858ab0ee2e1fb5e9b2f27213cde7`

## 11. pilot_002 / kk / qwen/qwen3.8-27b

Вопрос: «Аполлон» бағдарламасының қай миссиясы алғаш рет экипажбен ұшты?

Эталон: Apollo 7

Варианты: Apollo-7; Аполлон-7; Аполлон 7

[Источник](https://www.nasa.gov/the-apollo-program/)

Ответ модели:

> «Аполлон 7» миссиясы.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `156da1801ddeaddae32e830e71ee9d06bc78f88cd449d21cbcdb7b7c0219c547`
response_sha256: `6c5bacec49e17d83f2dff346b03bf6efe3f7152560baa2b5cf54639c438cc4a3`

## 12. pilot_002 / ru / openai/gpt-oss-20b

Вопрос: Какая миссия программы «Аполлон» первой полетела с экипажем?

Эталон: Apollo 7

Варианты: Apollo-7; Аполлон-7; Аполлон 7

[Источник](https://www.nasa.gov/the-apollo-program/)

Ответ модели:

> Первая пилотируемая миссия программы «Аполлон» — это **Apollo 7** (полёт 11 октября 1968 г.).

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `1ed87945aa40891072db8bc2a1afbd0f56554b62aed306569f7236cb22f2525b`
response_sha256: `d04baa7de511b36eaf81f3616b1b8c06ee4580426551d3c89c8bfe5fa1f4faf1`

## 13. pilot_002 / ru / qwen/qwen3.6-27b

Вопрос: Какая миссия программы «Аполлон» первой полетела с экипажем?

Эталон: Apollo 7

Варианты: Apollo-7; Аполлон-7; Аполлон 7

[Источник](https://www.nasa.gov/the-apollo-program/)

Ответ модели:

> Миссия «Аполлон-7».

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `db5c33f3db77fbea1f9d11e2a1bb96508476879c7142bc1e0acb8b95ad9e9860`
response_sha256: `7e42c39eb3dd7c716dab6814a16d50814eab98e0161cd39658dee2be7e1c108f`

## 14. pilot_003 / en / openai/gpt-oss-20b

Вопрос: Which Apollo mission first carried humans to the vicinity of the Moon?

Эталон: Apollo 8

Варианты: Apollo-8; Аполлон-8; Аполлон 8

[Источник](https://www.nasa.gov/the-apollo-program/)

Ответ модели:

> The first Apollo mission to carry humans to the vicinity of the Moon was **Apollo 8**.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `0dd36444e283294473c03dd0ea75d7b4105d38c215915620f4d4578d243fc694`
response_sha256: `d26f14c4ab9a8cecc60a9d61fc1ca21fecc7390f0df05ad9a3d70d17daba5120`

## 15. pilot_003 / kk / openai/gpt-oss-20b

Вопрос: «Аполлон» бағдарламасының қай миссиясы адамдарды алғаш рет Ай маңына жеткізді?

Эталон: Apollo 8

Варианты: Apollo-8; Аполлон-8; Аполлон 8

[Источник](https://www.nasa.gov/the-apollo-program/)

Ответ модели:

> Аполлон 11 миссиясы адамдарды алғаш рет Ай маңына жеткізді.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `2ff701fed4caa33ccd9cac56950630249bd07dd2e3a2e5d87b2ad5e5fbfdcf66`
response_sha256: `713ded58e3633766ef6e29c309c20cb5f85b3ba8708da1201538b458d1df0bc1`

## 16. pilot_003 / kk / qwen/qwen3.6-27b

Вопрос: «Аполлон» бағдарламасының қай миссиясы адамдарды алғаш рет Ай маңына жеткізді?

Эталон: Apollo 8

Варианты: Apollo-8; Аполлон-8; Аполлон 8

[Источник](https://www.nasa.gov/the-apollo-program/)

Ответ модели:

> «Аполлон-8» миссиясы.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `eaa4aac095ea7ff24f0081a0ed7f0b8f49a2f305a56ed9f6c70598ddb7421de0`
response_sha256: `e8119c1d5177b599e3f51f9e539f07326bd8a73a5dc411d0ed8533e8a0a84fd2`

## 17. pilot_003 / kk / qwen/qwen3.8-27b

Вопрос: «Аполлон» бағдарламасының қай миссиясы адамдарды алғаш рет Ай маңына жеткізді?

Эталон: Apollo 8

Варианты: Apollo-8; Аполлон-8; Аполлон 8

[Источник](https://www.nasa.gov/the-apollo-program/)

Ответ модели:

> «Аполлон-8» миссиясы.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `a117cb8752c2060f43f7305a5aec790ea3d21cc2493353fcb4a3cd4bdc3bf469`
response_sha256: `e8119c1d5177b599e3f51f9e539f07326bd8a73a5dc411d0ed8533e8a0a84fd2`

## 18. pilot_003 / ru / openai/gpt-oss-20b

Вопрос: Какая миссия «Аполлон» впервые доставила людей в окрестности Луны?

Эталон: Apollo 8

Варианты: Apollo-8; Аполлон-8; Аполлон 8

[Источник](https://www.nasa.gov/the-apollo-program/)

Ответ модели:

> Миссия «Аполлон‑8» (1972 г.) была первой, которая доставила людей в окрестности Луны.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `0d37b3e0c971eec794164a3493356611b74746c134ada8d563fa5cb3b0898651`
response_sha256: `4e10fc57edda7557fc9430d09169c78af13cd03378f1549ef8d2be788fc22b68`

## 19. pilot_003 / ru / qwen/qwen3.6-27b

Вопрос: Какая миссия «Аполлон» впервые доставила людей в окрестности Луны?

Эталон: Apollo 8

Варианты: Apollo-8; Аполлон-8; Аполлон 8

[Источник](https://www.nasa.gov/the-apollo-program/)

Ответ модели:

> Предпосылка вопроса неверна. Ни одна миссия «Аполлон» не доставляла людей в «окрестности» Луны без посадки или высадки, так как все пилотируемые миссии этой программы (с «Аполлона-8» по «Аполлон-17») либо совершали облет Луны, либо прилунялись.
> 
> Если под «окрестностями» подразумевается первый облет Луны с возвращением на Землю, то это была миссия **«Аполлон-8»** (декабрь 1968 года).
> 
> Если же имеется в виду первая высадка людей на поверхность Луны, то это была миссия **«Аполлон-11»** (июль 1969 года).

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `bd5b308706db4f6363e24537f242bb3d7b72abfe3afb9a2aa1f72ba339d7a229`
response_sha256: `6ee0bd0b50d3a4f93680912bb4fc277faa4e1ddd488aeaa523ec18caca0db1df`

## 20. pilot_004 / en / openai/gpt-oss-20b

Вопрос: Which Apollo mission first used the Lunar Roving Vehicle on the Moon?

Эталон: Apollo 15

Варианты: Apollo-15; Аполлон-15; Аполлон 15

[Источник](https://www.nasa.gov/the-apollo-program/)

Ответ модели:

> The Apollo mission that first used the Lunar Roving Vehicle on the Moon was **Apollo 15**.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `9ca96dfac71baa2e162b5e0ea2a061ab2e1429efe8995cf790434a7f83efcb8b`
response_sha256: `77a1dfd4fc2808be934ac4f33eded1d2cb761fc897e4abd3515f5748e8e81e06`

## 21. pilot_004 / kk / openai/gpt-oss-20b

Вопрос: Ай бетінде Ай көлігі (Lunar Roving Vehicle) алғаш рет «Аполлон» бағдарламасының қай миссиясында қолданылды?

Эталон: Apollo 15

Варианты: Apollo-15; Аполлон-15; Аполлон 15

[Источник](https://www.nasa.gov/the-apollo-program/)

Ответ модели:

> Ай көлігі (Lunar Roving Vehicle) алғаш рет **Аполлон‑15** миссиясында қолданылды.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `64b38a60e03334ee5bf3df3c0dfd3e6c555c5ef45b9ab71a09a29c20f0d86071`
response_sha256: `a74fafafe19083de277fb40e6945b1ff9dcb53000c3ee2e942d6605e4d264349`

## 22. pilot_004 / kk / qwen/qwen3.6-27b

Вопрос: Ай бетінде Ай көлігі (Lunar Roving Vehicle) алғаш рет «Аполлон» бағдарламасының қай миссиясында қолданылды?

Эталон: Apollo 15

Варианты: Apollo-15; Аполлон-15; Аполлон 15

[Источник](https://www.nasa.gov/the-apollo-program/)

Ответ модели:

> Аполлон-15 миссиясында.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `9c95f009a528a65b2cf646e20553d13fdff5cfe24331bdfdcd51fcebea1caceb`
response_sha256: `10945f907bd3a7ade731a204deab648b7c9b1f48741cdc68dd37773e41b1636a`

## 23. pilot_004 / kk / qwen/qwen3.8-27b

Вопрос: Ай бетінде Ай көлігі (Lunar Roving Vehicle) алғаш рет «Аполлон» бағдарламасының қай миссиясында қолданылды?

Эталон: Apollo 15

Варианты: Apollo-15; Аполлон-15; Аполлон 15

[Источник](https://www.nasa.gov/the-apollo-program/)

Ответ модели:

> Ай көлігі (Lunar Roving Vehicle) алғаш рет «Аполлон-15» миссиясында қолданылды.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `a24d928ff29cb3f00099a3d05b626dec134d33c4078557fffcd1e05ec83cc8d2`
response_sha256: `5e1b902e6451dbac2be60814aedb51a726bf3409d6c58a2450a3025465a8e589`

## 24. pilot_004 / ru / openai/gpt-oss-20b

Вопрос: В какой миссии «Аполлон» впервые использовали лунный автомобиль на Луне?

Эталон: Apollo 15

Варианты: Apollo-15; Аполлон-15; Аполлон 15

[Источник](https://www.nasa.gov/the-apollo-program/)

Ответ модели:

> Миссия **Аполлон‑15** (1971 г.) была первой, где на Луне использовали лунный автомобиль (Lunar Roving Vehicle).

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `7216c6062d274f6ec8123281e8ffa45b03a83500267efeca0ea5edb945a9b8cc`
response_sha256: `8a75636b6cae0e99e354103e9d2f82de71dda4ca6767abbe26892ad1e7ba4392`

## 25. pilot_004 / ru / qwen/qwen3.8-27b

Вопрос: В какой миссии «Аполлон» впервые использовали лунный автомобиль на Луне?

Эталон: Apollo 15

Варианты: Apollo-15; Аполлон-15; Аполлон 15

[Источник](https://www.nasa.gov/the-apollo-program/)

Ответ модели:

> Лунный автомобиль (Lunar Roving Vehicle) впервые использовали в миссии **«Аполлон-15»**.
> 
> *Примечание: В миссии «Аполлон-14» автомобиль не использовался, а в «Аполлон-15» он был доставлен на Луну и применен впервые.*

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `e1e414aaeacb700949870cdeed795211fd2b68361fb7531ec2c00220862accbb`
response_sha256: `b02baf97f0e39545bf13f4b1333e867b8a9c66d5a21c07aa18c334126c73aa35`

## 26. pilot_005 / en / openai/gpt-oss-20b

Вопрос: In which city is the Taj Mahal?

Эталон: Agra

Варианты: Агра

[Источник](https://whc.unesco.org/en/list/252/)

Ответ модели:

> The Taj Mahal is located in the city of Agra, India.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `d82cb69ce7589a5b82c6a2b974822617c7f49e8fb3f7426e9b28ff41d90e423f`
response_sha256: `534de900391d4e0d749ef6c2e5cd7809577aafa15673ca372917c8f8b1757445`

## 27. pilot_005 / kk / openai/gpt-oss-20b

Вопрос: Тәж-Махал қай қалада орналасқан?

Эталон: Agra

Варианты: Агра

[Источник](https://whc.unesco.org/en/list/252/)

Ответ модели:

> Тәж-Махал Аградта орналасқан.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `d140594e06c22c31003d42ba2045c15f190b70d854b5ace9fbcb3c2a8fd1a5bf`
response_sha256: `9fb4edddc330b8c68bbcb65f98ac805565763dca7977d09554e15d7214ac849b`

## 28. pilot_005 / kk / qwen/qwen3.6-27b

Вопрос: Тәж-Махал қай қалада орналасқан?

Эталон: Agra

Варианты: Агра

[Источник](https://whc.unesco.org/en/list/252/)

Ответ модели:

> Тәж-Махал Агра қаласында орналасқан.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `0165d3fe5ef0b6b94d34b5ec904169f3b43947e80bb0447418a7ea96a26acb23`
response_sha256: `8269dbeefe7e4566408f88d0f88b50b5fc205a13673a576dc92ad21504cf99c8`

## 29. pilot_005 / kk / qwen/qwen3.8-27b

Вопрос: Тәж-Махал қай қалада орналасқан?

Эталон: Agra

Варианты: Агра

[Источник](https://whc.unesco.org/en/list/252/)

Ответ модели:

> Тәж-Махал Агра қаласында (Үндістан) орналасқан.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `5ba6fcff5dc9fe2c830b901cf0abce79a5b60a68679512d0bd8262a8b7ca7dc3`
response_sha256: `9b04e2d53bfebd2ef475c60dd13ae8057e39ac72278420227556ee0b4cd31ca4`

## 30. pilot_005 / ru / openai/gpt-oss-20b

Вопрос: В каком городе расположен Тадж-Махал?

Эталон: Agra

Варианты: Агра

[Источник](https://whc.unesco.org/en/list/252/)

Ответ модели:

> Тадж‑Махал расположен в городе Агра, Индия.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `f2ebfe4caba017cf828daa35c19b839642ac110a5e76ae4e2b34628ec7026e41`
response_sha256: `7bc9d91f3494bb6962048c6335018dfcc48e4fa1806ce474ad38413eecf9d688`

## 31. pilot_005 / ru / qwen/qwen3.6-27b

Вопрос: В каком городе расположен Тадж-Махал?

Эталон: Agra

Варианты: Агра

[Источник](https://whc.unesco.org/en/list/252/)

Ответ модели:

> Тадж-Махал расположен в городе Агра (Индия).

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `b0f13014fe1dbbdbf1ba33544210659074bc4bae1372c35e8bed74ae2f8b3357`
response_sha256: `e3208ff57b0f5217324c175a63ed35842e81e4c864ae9b89fa514a8f1f08b9d9`

## 32. pilot_005 / ru / qwen/qwen3.8-27b

Вопрос: В каком городе расположен Тадж-Махал?

Эталон: Agra

Варианты: Агра

[Источник](https://whc.unesco.org/en/list/252/)

Ответ модели:

> Тадж-Махал расположен в городе Агра (Индия).

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `6046e9c7724023db121310c38cc3eba059412e783d84036a887dc2a010789c22`
response_sha256: `e3208ff57b0f5217324c175a63ed35842e81e4c864ae9b89fa514a8f1f08b9d9`

## 33. pilot_006 / en / openai/gpt-oss-20b

Вопрос: In which country is Machu Picchu?

Эталон: Peru

Варианты: Перу

[Источник](https://whc.unesco.org/en/list/274/)

Ответ модели:

> Machu Picchu is in Peru.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `c67f81445a58449fdf8a8d82c8dd902d660cd812ef27c08051498f9baf92313d`
response_sha256: `6d7ecd0c02f8eec18127b878ff2cd004c3c23afe1f7f0c2214c9ab73fb61f1ac`

## 34. pilot_006 / kk / openai/gpt-oss-20b

Вопрос: Мачу-Пикчу қай елде орналасқан?

Эталон: Peru

Варианты: Перу

[Источник](https://whc.unesco.org/en/list/274/)

Ответ модели:

> Мачу-Пикчу Перу елінде орналасқан.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `7e6380e5c2d4fafbef78d81fa268f51da8fb2c72e38bc6b00e9250eaec9978ee`
response_sha256: `a3b3631b9ec843113c89bedbf05d767d8d301fce1d4830e2e9712ac72c148151`

## 35. pilot_006 / kk / qwen/qwen3.6-27b

Вопрос: Мачу-Пикчу қай елде орналасқан?

Эталон: Peru

Варианты: Перу

[Источник](https://whc.unesco.org/en/list/274/)

Ответ модели:

> Мачу-Пикчу Перу елінде орналасқан.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `32a75202549e9e65f6737b73d414b1f707168245562572861172ee585400583e`
response_sha256: `a3b3631b9ec843113c89bedbf05d767d8d301fce1d4830e2e9712ac72c148151`

## 36. pilot_006 / kk / qwen/qwen3.8-27b

Вопрос: Мачу-Пикчу қай елде орналасқан?

Эталон: Peru

Варианты: Перу

[Источник](https://whc.unesco.org/en/list/274/)

Ответ модели:

> Мачу-Пикчу Перу елінде орналасқан.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `3b7e436d70ef590b3c211a342f07db37d63e9bbc528518693593f03e6985b75b`
response_sha256: `a3b3631b9ec843113c89bedbf05d767d8d301fce1d4830e2e9712ac72c148151`

## 37. pilot_006 / ru / openai/gpt-oss-20b

Вопрос: В какой стране расположен Мачу-Пикчу?

Эталон: Peru

Варианты: Перу

[Источник](https://whc.unesco.org/en/list/274/)

Ответ модели:

> Мачу-Пикчу расположен в Перу.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `db59d30d89256d6d23c4822bc95b4f3283cf103998fe93470ef5b9d5b9ae2006`
response_sha256: `613418f380cc9c35b7920dd7edbdc25375a0ae6c5bb03fe3e5b35c3421d6afb5`

## 38. pilot_007 / en / openai/gpt-oss-20b

Вопрос: Off the coast of which country is the Great Barrier Reef?

Эталон: Australia

Варианты: Австралия; Аустралия

[Источник](https://whc.unesco.org/en/list/154/)

Ответ модели:

> The Great Barrier Reef lies off the coast of Australia.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `540de3bdb75b1a58623625c189c0c49038169e3da1a2be5dde4e4392abea0a43`
response_sha256: `899bf71b39fdcd5b8343f3cbe75051404c3e86a089a011f55dd4b5911b44b2e8`

## 39. pilot_007 / kk / openai/gpt-oss-20b

Вопрос: Үлкен тосқауыл рифі қай елдің жағалауында орналасқан?

Эталон: Australia

Варианты: Австралия; Аустралия

[Источник](https://whc.unesco.org/en/list/154/)

Ответ модели:

> Үлкен тосқауыл рифі (Great Barrier Reef) Австралияның шығыс жағалауында орналасқан.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `65d1dd07e60a86aa580d4c1f68711ffb6c148861d14f1cedd3aeb9379a1b8ab3`
response_sha256: `128562ace9a3424906871cf88d75a305a62aa6c2636b08f76010621fed42202a`

## 40. pilot_007 / kk / qwen/qwen3.8-27b

Вопрос: Үлкен тосқауыл рифі қай елдің жағалауында орналасқан?

Эталон: Australia

Варианты: Австралия; Аустралия

[Источник](https://whc.unesco.org/en/list/154/)

Ответ модели:

> Үлкен тосқауыл рифі Австралияның солтүстік-шығыс жағалауында орналасқан.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `a8551d52f1b632e2827112ace3123e5d971a812695c802529680f4780f5acda3`
response_sha256: `f50fdf1d16447cf6f623814c305876c43a6691bd93434a9bec42427ac4fd34dd`

## 41. pilot_007 / ru / openai/gpt-oss-20b

Вопрос: У побережья какой страны расположен Большой Барьерный риф?

Эталон: Australia

Варианты: Австралия; Аустралия

[Источник](https://whc.unesco.org/en/list/154/)

Ответ модели:

> Большой Барьерный риф расположен у побережья Австралии.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `757049a65b397e0b647b8d019365564ff72a2bcbd83eae723b252adac94f69fe`
response_sha256: `b6790e59b850a15452ac5c1f7c6b8188c3ea14666e455bafa5e39cbc686cc224`

## 42. pilot_007 / ru / qwen/qwen3.6-27b

Вопрос: У побережья какой страны расположен Большой Барьерный риф?

Эталон: Australia

Варианты: Австралия; Аустралия

[Источник](https://whc.unesco.org/en/list/154/)

Ответ модели:

> Австралии.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `e471dca3f747746d9f41896e46ee2c9883ed8304006b77e34b4b280d88d2c6c8`
response_sha256: `dd611f913fa62aeae18fe26076521bcc9ef25a25643328ab0ee27bab6d663939`

## 43. pilot_008 / en / openai/gpt-oss-20b

Вопрос: In which country is Angkor?

Эталон: Cambodia

Варианты: Камбоджа

[Источник](https://whc.unesco.org/en/list/668/)

Ответ модели:

> Angkor is in Cambodia.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `a55ea689d73b69b7d095efd2194cb715387901cc73c92b497fdeaa301d275eb9`
response_sha256: `1df62e861c8ada7018c4371762f152f6be0527d79f8c795c165a0cfcb90c0243`

## 44. pilot_008 / kk / openai/gpt-oss-20b

Вопрос: Ангкор қай елде орналасқан?

Эталон: Cambodia

Варианты: Камбоджа

[Источник](https://whc.unesco.org/en/list/668/)

Ответ модели:

> Ангкор – Камбоджа елінде орналасқан.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `ed30ae94c3f5d950b6ac802d2b9df84d79da6d6208b5c27477d0b66dc208a2f4`
response_sha256: `16b59b3d7396dac167b195444a788b6982df3c3084789e581d69e7e2a7c18d4f`

## 45. pilot_008 / kk / qwen/qwen3.6-27b

Вопрос: Ангкор қай елде орналасқан?

Эталон: Cambodia

Варианты: Камбоджа

[Источник](https://whc.unesco.org/en/list/668/)

Ответ модели:

> Ангкор Камбоджада орналасқан.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `b90b5b12efe28e5d6a33343e2c3e27d309b24529c04630a2b17444ee85a22eef`
response_sha256: `4b73a85e18bbe70ece66761b658bcd381a6b19ce602d947e4f772c143b902a81`

## 46. pilot_008 / kk / qwen/qwen3.8-27b

Вопрос: Ангкор қай елде орналасқан?

Эталон: Cambodia

Варианты: Камбоджа

[Источник](https://whc.unesco.org/en/list/668/)

Ответ модели:

> Ангкор Камбоджада орналасқан.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `f5d360b5b2f16f8aa9e5f699304a4de1fed454c4c24b79cba385ac26fdccfe9f`
response_sha256: `4b73a85e18bbe70ece66761b658bcd381a6b19ce602d947e4f772c143b902a81`

## 47. pilot_008 / ru / openai/gpt-oss-20b

Вопрос: В какой стране расположен Ангкор?

Эталон: Cambodia

Варианты: Камбоджа

[Источник](https://whc.unesco.org/en/list/668/)

Ответ модели:

> Ангкор находится в КАМБОДЖЕ.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `8026e4e7f0ccda0be58bfb06bed3cd6670ef4f3f21b2af4fadb7fce31d575cbb`
response_sha256: `21156e11a3ec2486c34f1bd61efafa82fab3e012b1f2941488db113ad5a2d662`

## 48. pilot_008 / ru / qwen/qwen3.6-27b

Вопрос: В какой стране расположен Ангкор?

Эталон: Cambodia

Варианты: Камбоджа

[Источник](https://whc.unesco.org/en/list/668/)

Ответ модели:

> Ангкор расположен в Камбодже.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `8eb371745887441ef1f5cb831fe3cbaddabff751e6fed796aed2f7f14af12098`
response_sha256: `d485b99ce119983962b2ab33db0bffda061697d09a72591dc8e361d4d48fcc8f`

## 49. pilot_008 / ru / qwen/qwen3.8-27b

Вопрос: В какой стране расположен Ангкор?

Эталон: Cambodia

Варианты: Камбоджа

[Источник](https://whc.unesco.org/en/list/668/)

Ответ модели:

> Ангкор расположен в Камбодже.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `b51f32e3e75a78d31d3c56177ec88c28f4d0cc393ea06253c85169a5d61f0621`
response_sha256: `d485b99ce119983962b2ab33db0bffda061697d09a72591dc8e361d4d48fcc8f`

## 50. pilot_009 / en / openai/gpt-oss-20b

Вопрос: Which planet has the highest surface temperature in the Solar System?

Эталон: Venus

Варианты: Венера; Шолпан

[Источник](https://science.nasa.gov/venus/venus-facts/)

Ответ модели:

> The planet with the highest surface temperature in the Solar System is **Venus**.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `ffda41a4a793e4758c2c3ddb2819c6ab0b7963f29306e86f7a472160bdf425ce`
response_sha256: `e00ae081f5597b94ca21dbe85d7e4fdb987e34562b9d1fe5036efc53fb46debb`
