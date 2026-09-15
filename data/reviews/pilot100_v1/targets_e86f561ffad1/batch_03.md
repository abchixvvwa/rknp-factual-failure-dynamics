# Проверка ответов моделей: pilot100_v1

Пакет 3. Номера 101–150. Это часть пилота, по уже полученным ответам; сбор остальных продолжается.

Оцените весь ответ: 1 — фактически верен, 0 — фактически неверен. Если случай неоднозначен или ответ оборван, оставьте пояснение вместо догадки. Для ложной предпосылки ответ должен явно её отвергать. Можно прислать номера и оценки в чат, указав название пакета.

Проверка эталонных фактов ранее не означает проверки этих ответов моделей.

## 101. pilot_065 / ru / openai/gpt-oss-20b

Вопрос: Кто написал картину «Постоянство памяти»?

Эталон: Salvador Dali

Варианты: Salvador Dalí; Dali; Dalí; Сальвадор Дали; Дали

[Источник](https://www.moma.org/collection/works/79018)

Ответ модели:

> Картина «Постоянство памяти» (The Persistence of Memory) написана испанским художником Сальвадором Дали.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `6fe8a8040f05775410d48571162bc19f6bc56757ead5162d1b4e2a60fa509dba`
response_sha256: `ff3cc72ca9b167eec70b60bcb9dd15a234ac6e605855dd39cc8418f5f9ae8b17`

## 102. pilot_065 / ru / qwen/qwen3.6-27b

Вопрос: Кто написал картину «Постоянство памяти»?

Эталон: Salvador Dali

Варианты: Salvador Dalí; Dali; Dalí; Сальвадор Дали; Дали

[Источник](https://www.moma.org/collection/works/79018)

Ответ модели:

> Картину «Постоянство памяти» написал Сальвадор Дали.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `fb807339428c9cd0a8bb8512401929d099e7e991cb31616f78a55064a5d3954d`
response_sha256: `02bdd693c8b8edd2bd99888055c040d6010d9535452724471726563ce3c8350a`

## 103. pilot_066 / en / openai/gpt-oss-20b

Вопрос: Who painted The Night Watch?

Эталон: Rembrandt van Rijn

Варианты: Rembrandt; Рембрандт; Рембрандт ван Рейн

[Источник](https://www.rijksmuseum.nl/en/stories/10-things/story/10-things-about-rembrandt-s-night-watch)

Ответ модели:

> The Night Watch was painted by Rembrandt van Rijn.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `e60b9636458e11329ca533f9ae09923296f3e21f7224d304d61bed9c0a116679`
response_sha256: `b6862b7f37c63945a050952ec9f00fa0ee6a1c8c4e806e84b040c34b7953f935`

## 104. pilot_066 / kk / openai/gpt-oss-20b

Вопрос: «Түнгі күзет» картинасын кім салған?

Эталон: Rembrandt van Rijn

Варианты: Rembrandt; Рембрандт; Рембрандт ван Рейн

[Источник](https://www.rijksmuseum.nl/en/stories/10-things/story/10-things-about-rembrandt-s-night-watch)

Ответ модели:

> «Түнгі күзет» (орыс тілінде *Ночной дозор*) картинасын 1642‑жылда Рембрандт ван Рейен (Rembrandt van Rijn) салған.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `5535549bc299df611f5640c8c7e844618e237e9c6444728e44f0614e20d09760`
response_sha256: `efb6cac4c5ebd86ffc6bf5a8632b2bcd8ae8c4dd8f82f1d8441b9f95d155a936`

## 105. pilot_066 / kk / qwen/qwen3.6-27b

Вопрос: «Түнгі күзет» картинасын кім салған?

Эталон: Rembrandt van Rijn

Варианты: Rembrandt; Рембрандт; Рембрандт ван Рейн

[Источник](https://www.rijksmuseum.nl/en/stories/10-things/story/10-things-about-rembrandt-s-night-watch)

Ответ модели:

> «Түнгі күзет» картинасын голландиялық суретші Ян Вермеер салған.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `57367eb1f15f2de8c8f5f95e14392526da7e9e27f7fe0e9520ffee8bdd76e9db`
response_sha256: `732fb91aec36a7acfd2a845f124c8babc1d106a6ee14b87e589eb1ea7be79c60`

## 106. pilot_066 / kk / qwen/qwen3.8-27b

Вопрос: «Түнгі күзет» картинасын кім салған?

Эталон: Rembrandt van Rijn

Варианты: Rembrandt; Рембрандт; Рембрандт ван Рейн

[Источник](https://www.rijksmuseum.nl/en/stories/10-things/story/10-things-about-rembrandt-s-night-watch)

Ответ модели:

> Бұл сұрақта жалған алғышарт бар. «Түнгі күзет» (немесе «Түнгі сақшы») деп аталатын әйгілі, жалпыға белгілі бір шедевр жоқ.
> 
> Ең ықтимал жағдайда, сіз **Винсент ван Гогтың** «Түнгі кафе» (The Night Café) немесе **Рембрандттың** «Түнгі күзет» (The Night Watch) картинасын меңзеп тұрсыз.
> 
> *   Егер **«Түнгі күзет» (The Night Watch)** туралы болса, оны **Рембрандт ван Рейн** салған.
> *   Егер **«Түнгі кафе»** туралы болса, оны **Винсент ван Гог** салған.
> 
> Нақты атауы «Түнгі күзет» болғандықтан, жауап: **Рембрандт ван Рейн**.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `9166e9965f94afa2f61d52407e1e3a770e707376e0badb45db9f709af9c7685e`
response_sha256: `bff96fc94cf2ec19af30bd86518530cd25277caf44e7e5988e218bbab2094c3a`

## 107. pilot_066 / ru / openai/gpt-oss-20b

Вопрос: Кто написал картину «Ночной дозор»?

Эталон: Rembrandt van Rijn

Варианты: Rembrandt; Рембрандт; Рембрандт ван Рейн

[Источник](https://www.rijksmuseum.nl/en/stories/10-things/story/10-things-about-rembrandt-s-night-watch)

Ответ модели:

> Картина «Ночной дозор» написана Рембрандтом ван Рейном.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `3362522dd6900b5d4b43262509d8076d6e9eb9c44b070195f448de6eec1a9e97`
response_sha256: `b448822db243c089b4c396398ea9fa6167e44eee138848dc29f913699e9c4269`

## 108. pilot_066 / ru / qwen/qwen3.6-27b

Вопрос: Кто написал картину «Ночной дозор»?

Эталон: Rembrandt van Rijn

Варианты: Rembrandt; Рембрандт; Рембрандт ван Рейн

[Источник](https://www.rijksmuseum.nl/en/stories/10-things/story/10-things-about-rembrandt-s-night-watch)

Ответ модели:

> Картину «Ночной дозор» написал Ян Вермеер.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `f3c1d732234c9c4d97c1d33739734456d409fcb8c39a583315d9ce73230eb98b`
response_sha256: `a16cbaa56cd23fb86b7ca0223499d11ad74b220757c505615ab9fca7ad8b50dd`

## 109. pilot_066 / ru / qwen/qwen3.8-27b

Вопрос: Кто написал картину «Ночной дозор»?

Эталон: Rembrandt van Rijn

Варианты: Rembrandt; Рембрандт; Рембрандт ван Рейн

[Источник](https://www.rijksmuseum.nl/en/stories/10-things/story/10-things-about-rembrandt-s-night-watch)

Ответ модели:

> Картина «Ночной дозор» написана Рембрандтом Харменс ван Рейном.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `d4d81e657c799aec5d3c87a85181c0473c531e0b9196ace71e6448e0db4cc066`
response_sha256: `ab553641bf2767ad206a6c02c2333731353cab3ffb5746c2ab8b83af846139e8`

## 110. pilot_067 / en / openai/gpt-oss-20b

Вопрос: Who painted the Birth of Venus held by the Uffizi?

Эталон: Sandro Botticelli

Варианты: Botticelli; Сандро Боттичелли; Боттичелли

[Источник](https://www.uffizi.it/en/artworks/birth-of-venus)

Ответ модели:

> The *Birth of Venus* in the Uffizi Gallery was painted by Sandro Botticelli.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `2c53db08035c56a0c88bcf38a2f0a79a1248edde5a4b31b29a69c358e7d19a26`
response_sha256: `e34911af33651df59acc7fa7bef32160112bcd3e3680f7bd70d0bd0c0f6b7fbc`

## 111. pilot_067 / en / qwen/qwen3.8-27b

Вопрос: Who painted the Birth of Venus held by the Uffizi?

Эталон: Sandro Botticelli

Варианты: Botticelli; Сандро Боттичелли; Боттичелли

[Источник](https://www.uffizi.it/en/artworks/birth-of-venus)

Ответ модели:

> The premise is false. The *Birth of Venus* is not held by the Uffizi Gallery; it is housed in the Uffizi's neighboring gallery, the **Galleria degli Uffizi** is incorrect, it is in the **Uffizi**? No, wait. Let me double-check.
> 
> Actually, the famous *Birth of Venus* by **Sandro Botticelli** is held by the **Uffizi Gallery** in Florence. My initial hesitation was unfounded. The painting is indeed in the Uffizi.
> 
> So, the answer is: **Sandro Botticelli**.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `b707069dbc129d71b60d41143d57f30a86eb91a70e66003670c75acdfc058631`
response_sha256: `f481b9410159143df79c62b08c21345ea4fbcd1cdcfe905a0fe068137b880405`

## 112. pilot_067 / kk / openai/gpt-oss-20b

Вопрос: Уффици галереясындағы «Венераның тууы» картинасын кім салған?

Эталон: Sandro Botticelli

Варианты: Botticelli; Сандро Боттичелли; Боттичелли

[Источник](https://www.uffizi.it/en/artworks/birth-of-venus)

Ответ модели:

> «Венераның тууы» (The Birth of Venus) – Сандро Боттичелли (Sandro Botticelli) атты итальян суретшісі салған.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `987e4c8a7be396f600802acab44a77e6ca6efbefcda23cc02dc6b1714a60b081`
response_sha256: `6816a5de5f5c7965d206ed44e4dc64fe914add338dfb1e469a2b36fb5c771212`

## 113. pilot_067 / kk / qwen/qwen3.6-27b

Вопрос: Уффици галереясындағы «Венераның тууы» картинасын кім салған?

Эталон: Sandro Botticelli

Варианты: Botticelli; Сандро Боттичелли; Боттичелли

[Источник](https://www.uffizi.it/en/artworks/birth-of-venus)

Ответ модели:

> «Венераның тууы» картинасын Сандро Боттичелли салған.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `785312963c9528c46d85db524a58302c7e70716a0d28445c8315838365e5f5b5`
response_sha256: `b40e78f3ca41b68cfaf01a85679c23d0d61d91c689702f1f4728f3bea7dbbf0e`

## 114. pilot_067 / kk / qwen/qwen3.8-27b

Вопрос: Уффици галереясындағы «Венераның тууы» картинасын кім салған?

Эталон: Sandro Botticelli

Варианты: Botticelli; Сандро Боттичелли; Боттичелли

[Источник](https://www.uffizi.it/en/artworks/birth-of-venus)

Ответ модели:

> Бұл сұрақта жалған алғышарт бар. Уффици галереясында «Венераның тууы» атты картина жоқ.
> 
> Бұл атаумен ең танымал картина — **Сандро Боттичелли** салған «Венераның тууы», ол Флоренциядағы **Уффици галереясында** сақталады.
> 
> Егер сіз басқа галереяны (мысалы, Лувр немесе Прадо) меңзеген болсаңыз, онда жауап өзгеше болуы мүмкін, бірақ Уффици контекстінде дұрыс жауап: **Сандро Боттичелли**.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `f6d4ab3355a9c0e71228f6ec16a23e021153965386606a75688c7760a07fff09`
response_sha256: `f4d9441131e59055ed5ab32830960c3aae55e850695c242e8be18e0d48391874`

## 115. pilot_067 / ru / openai/gpt-oss-20b

Вопрос: Кто написал картину «Рождение Венеры», хранящуюся в Уффици?

Эталон: Sandro Botticelli

Варианты: Botticelli; Сандро Боттичелли; Боттичелли

[Источник](https://www.uffizi.it/en/artworks/birth-of-venus)

Ответ модели:

> Картина «Рождение Венеры», хранящаяся в Уффици, написана Сандро Боттичелли.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `22e14936059cc827911bfe531b77170babc24d66c38c66661b44744f76cd7d6b`
response_sha256: `bf3e3a952247d4ad769e7a4ebfd49afe23f53f81b50923f6b7b6d3346a629035`

## 116. pilot_067 / ru / qwen/qwen3.6-27b

Вопрос: Кто написал картину «Рождение Венеры», хранящуюся в Уффици?

Эталон: Sandro Botticelli

Варианты: Botticelli; Сандро Боттичелли; Боттичелли

[Источник](https://www.uffizi.it/en/artworks/birth-of-venus)

Ответ модели:

> Картину «Рождение Венеры» написал Сандро Боттичелли.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `aa4def51a139c5e089193e3dada5ec104709ca3ef2a06348c5686f7fc5ef2ba7`
response_sha256: `a542cc145ea58b5a5b70b03bc52b60a8db7e3bee72f81957cb6f5d17afcc96ea`

## 117. pilot_068 / en / openai/gpt-oss-20b

Вопрос: Who created the sculpture The Thinker?

Эталон: Auguste Rodin

Варианты: Rodin; Огюст Роден; Роден

[Источник](https://www.musee-rodin.fr/en/musee/collections/oeuvres/thinker)

Ответ модели:

> The sculpture *The Thinker* was created by Auguste Rodin.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `62c93225d3bf7e1c417fdc1f22f33ac5e6059cd4729629ecd7a0b212ce91e736`
response_sha256: `46623b455f6de73ff6b1e56cd5411544d95519ffa252a796577a19b317a0cd0e`

## 118. pilot_068 / kk / openai/gpt-oss-20b

Вопрос: «Ойшыл» мүсінін кім жасаған?

Эталон: Auguste Rodin

Варианты: Rodin; Огюст Роден; Роден

[Источник](https://www.musee-rodin.fr/en/musee/collections/oeuvres/thinker)

Ответ модели:

> «Ойшыл» мүсіні – Қазақстанның белгілі скульпторы **Ойсан Құмаров** (Oysan Qumarov) жасаған.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `21aa9026c7d55d8c0c667b735b4e37a13f5bc318c6981b73565c60234580c327`
response_sha256: `1109be24467ce7aae6903ec8fe3c5b22591c0d301c694ea3a4bf98dd21d733c7`

## 119. pilot_068 / kk / qwen/qwen3.6-27b

Вопрос: «Ойшыл» мүсінін кім жасаған?

Эталон: Auguste Rodin

Варианты: Rodin; Огюст Роден; Роден

[Источник](https://www.musee-rodin.fr/en/musee/collections/oeuvres/thinker)

Ответ модели:

> «Ойшыл» мүсінін қазақ мүсіншісі **Мұрат Әуезов** жасаған.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `5ec03120f2347b6d9c1a38bea86c716dd3b8b541b3ff7af66cb7bd47b6c79342`
response_sha256: `e1b6ae5ef54e7947d864a6a6a34527e0a16ff43580867251d349091368594697`

## 120. pilot_068 / kk / qwen/qwen3.8-27b

Вопрос: «Ойшыл» мүсінін кім жасаған?

Эталон: Auguste Rodin

Варианты: Rodin; Огюст Роден; Роден

[Источник](https://www.musee-rodin.fr/en/musee/collections/oeuvres/thinker)

Ответ модели:

> «Ойшыл» (Le Penseur) мүсінін француз скульпторы **Огюст Роден** жасаған.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `5644cdd2cf6aa1d28f85f717792b35bf502049da1fadcc32a8c478bf07b9dd67`
response_sha256: `6894353cd46d85a5d08ad3c37995150ad80638da51d787411dce232908a4c81b`

## 121. pilot_068 / ru / openai/gpt-oss-20b

Вопрос: Кто создал скульптуру «Мыслитель»?

Эталон: Auguste Rodin

Варианты: Rodin; Огюст Роден; Роден

[Источник](https://www.musee-rodin.fr/en/musee/collections/oeuvres/thinker)

Ответ модели:

> Скульптуру «Мыслитель» создал французский скульптор Огюст Роден.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `7c6a057bcf14806d73645a05e04d8cf68e0907fba6ff7c0237dccd73e141954c`
response_sha256: `21533288b9241cd7ab4b6670155df52806c2aa579c8caeaec898ce9c9f207ee1`

## 122. pilot_068 / ru / qwen/qwen3.6-27b

Вопрос: Кто создал скульптуру «Мыслитель»?

Эталон: Auguste Rodin

Варианты: Rodin; Огюст Роден; Роден

[Источник](https://www.musee-rodin.fr/en/musee/collections/oeuvres/thinker)

Ответ модели:

> Скульптуру «Мыслитель» создал Огюст Роден.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `8dfa1faab232fa363d1e5fc6c856cff84969a843721b7efd65c08850ace6cd61`
response_sha256: `e3d757f99e593059aa742a30727a139bfde6b06b8cdaf213c5f202e3651be142`

## 123. pilot_069 / en / openai/gpt-oss-20b

Вопрос: Who created the print The Great Wave off Kanagawa?

Эталон: Katsushika Hokusai

Варианты: Hokusai; Кацусика Хокусай; Хокусай

[Источник](https://www.metmuseum.org/art/collection/search/45434?mod=article_inline)

Ответ модели:

> The print *The Great Wave off Kanagawa* was created by the Japanese artist Katsushika Hokusai.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `ee67eda4764c1a3e577b8955384bb87f2d0e83b767ec81171061b52b25a036bf`
response_sha256: `e869a3d511ed47991246bbea8f5c682cb323cdb1c994336a3b2008ea70fd2141`

## 124. pilot_069 / en / qwen/qwen3.6-27b

Вопрос: Who created the print The Great Wave off Kanagawa?

Эталон: Katsushika Hokusai

Варианты: Hokusai; Кацусика Хокусай; Хокусай

[Источник](https://www.metmuseum.org/art/collection/search/45434?mod=article_inline)

Ответ модели:

> The print *The Great Wave off Kanagawa* was created by the Japanese ukiyo-e artist **Katsushika Hokusai**.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `e0b3037655d7f28ea580694fbd3dbc9eaaa0888790906c7677a278f286081aee`
response_sha256: `a334f1bfeb2106d3856f35b357abde545123764b9991e6ad2e9b6ef409b3adab`

## 125. pilot_069 / kk / openai/gpt-oss-20b

Вопрос: «Канагавадағы үлкен толқын» гравюрасын кім жасаған?

Эталон: Katsushika Hokusai

Варианты: Hokusai; Кацусика Хокусай; Хокусай

[Источник](https://www.metmuseum.org/art/collection/search/45434?mod=article_inline)

Ответ модели:

> «Канагавадағы үлкен толқын» (The Great Wave off Kanagawa) гравюрасы – Кацусика Хокусай (Katsushika Hokusai) жасаған.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `96289b96e7d8114b08e1b37a2dc5494cfdf9a1b6d860d5871d807c3ef1bb2c5b`
response_sha256: `7ba40a39a1b40d6f9c97313e68bcb7cea3f2a366d95154c4a52b0197541eec4e`

## 126. pilot_069 / kk / qwen/qwen3.6-27b

Вопрос: «Канагавадағы үлкен толқын» гравюрасын кім жасаған?

Эталон: Katsushika Hokusai

Варианты: Hokusai; Кацусика Хокусай; Хокусай

[Источник](https://www.metmuseum.org/art/collection/search/45434?mod=article_inline)

Ответ модели:

> «Канагавадағы үлкен толқын» гравюрасын япон суретшісі **Кацусика Хокусай** жасаған.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `10789d7b42050cf65bed83e97e1d05ba8f303cb21237fef24c385d7264d271ce`
response_sha256: `17f8b0971b2c6ce77e368b4464d077e8823f9e8535911d748cf61d112da1eab9`

## 127. pilot_069 / kk / qwen/qwen3.8-27b

Вопрос: «Канагавадағы үлкен толқын» гравюрасын кім жасаған?

Эталон: Katsushika Hokusai

Варианты: Hokusai; Кацусика Хокусай; Хокусай

[Источник](https://www.metmuseum.org/art/collection/search/45434?mod=article_inline)

Ответ модели:

> «Канагавадағы үлкен толқын» гравюрасын **Хокусай Кацусика** жасаған.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `dae28c0bfdee50c421afda3deae9aa814fc7bd966d67cbebc31c57e4bd7491bf`
response_sha256: `ed3134bde3723721b0aa02c859e75dd37adc88cf79a6ed98e66e66f6a7787232`

## 128. pilot_069 / ru / openai/gpt-oss-20b

Вопрос: Кто создал гравюру «Большая волна в Канагаве»?

Эталон: Katsushika Hokusai

Варианты: Hokusai; Кацусика Хокусай; Хокусай

[Источник](https://www.metmuseum.org/art/collection/search/45434?mod=article_inline)

Ответ модели:

> Гравюру «Большая волна в Канагаве» создал японский художник Кацусика Хокусай.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `b11871f5839d644da05910cebaf2a3a902bae144ccb092fb895d25bec29960f1`
response_sha256: `6853f3d698b6345dbd6917f7a879a39913a00ec16f135ec5814bf2f540c41d74`

## 129. pilot_069 / ru / qwen/qwen3.6-27b

Вопрос: Кто создал гравюру «Большая волна в Канагаве»?

Эталон: Katsushika Hokusai

Варианты: Hokusai; Кацусика Хокусай; Хокусай

[Источник](https://www.metmuseum.org/art/collection/search/45434?mod=article_inline)

Ответ модели:

> Гравюру «Большая волна у Канагавы» создал японский художник Кацусика Хокусай.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `06c889673dfc7534362e7feb6865e07249ab57dc7ce03a48779fc09947166697`
response_sha256: `e5c9d9abf44c7f5f1a9d50a1cc41b1dec0ac2f4e68f6b32a49899f714206ec42`

## 130. pilot_069 / ru / qwen/qwen3.8-27b

Вопрос: Кто создал гравюру «Большая волна в Канагаве»?

Эталон: Katsushika Hokusai

Варианты: Hokusai; Кацусика Хокусай; Хокусай

[Источник](https://www.metmuseum.org/art/collection/search/45434?mod=article_inline)

Ответ модели:

> Гравюру «Большая волна в Канагаве» создал японский художник-укиё-э **Кацусика Хокусай**.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `61b50fbf39115e11dc4cca2f592e4c49db2e19459ee83513e98f61a680c04a61`
response_sha256: `8bb5a11e41e7ecc61143747103188810525192374adedad229c4e5dd90f18c8c`

## 131. pilot_070 / en / openai/gpt-oss-20b

Вопрос: Who painted American Gothic?

Эталон: Grant Wood

Варианты: Грант Вуд

[Источник](https://archive.artic.edu/ryerson/3110)

Ответ модели:

> American Gothic was painted by Grant Wood.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `10e2d54816e9083558eb1d5e25d1763b87e2c2c203e7101c38deda43bb23528d`
response_sha256: `21e12c2810af3e8c49c827f747978dbae069ec6f76677981cc424b132be35fb1`

## 132. pilot_070 / kk / openai/gpt-oss-20b

Вопрос: «Америкалық готика» картинасын кім салған?

Эталон: Grant Wood

Варианты: Грант Вуд

[Источник](https://archive.artic.edu/ryerson/3110)

Ответ модели:

> «Америкалық готика» картинасын 1930‑жылдары американдық суретші Грант Ууд (Grant Wood) салған.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `b2cb071be76b363fb641580827b14d91c655c2b60d0cb18c3d751413807dc9a5`
response_sha256: `2b07631bda55acb4a04505efb0df1c3fc00addf2547a503a3485ddef92f11995`

## 133. pilot_070 / kk / qwen/qwen3.6-27b

Вопрос: «Америкалық готика» картинасын кім салған?

Эталон: Grant Wood

Варианты: Грант Вуд

[Источник](https://archive.artic.edu/ryerson/3110)

Ответ модели:

> «Америкалық готика» картинасын Грент Вуд салған.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `958a8ed3ecba86df269e0c4437034e320473f85f7cb879bd6cb0637d93c5df5b`
response_sha256: `84634b174407acf628682f9b9542eea12a09aeb9e33bb79106541659205031fb`

## 134. pilot_070 / kk / qwen/qwen3.8-27b

Вопрос: «Америкалық готика» картинасын кім салған?

Эталон: Grant Wood

Варианты: Грант Вуд

[Источник](https://archive.artic.edu/ryerson/3110)

Ответ модели:

> «Америкалық готика» картинасын Грент Вуд салған.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `3a2cdbc5fdd7c0e4f2de0df54ce771694216970ad9d717d2da024b0bbf084758`
response_sha256: `84634b174407acf628682f9b9542eea12a09aeb9e33bb79106541659205031fb`

## 135. pilot_070 / ru / openai/gpt-oss-20b

Вопрос: Кто написал картину «Американская готика»?

Эталон: Grant Wood

Варианты: Грант Вуд

[Источник](https://archive.artic.edu/ryerson/3110)

Ответ модели:

> Картина «Американская готика» написана американским художником Грантом Уудом.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `33ba6e27a16872598f2cec80028fdec766667357cb1aca0e8ed7638eb5285d64`
response_sha256: `74dd3cddd70403f28ed834b1bded086362618824cfcb48a8ee0f71018efdbc56`

## 136. pilot_070 / ru / qwen/qwen3.6-27b

Вопрос: Кто написал картину «Американская готика»?

Эталон: Grant Wood

Варианты: Грант Вуд

[Источник](https://archive.artic.edu/ryerson/3110)

Ответ модели:

> Картину «Американская готика» написал Грант Вуд.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `dd94654345c3d1095e934659c1232682a6169a81aedee16a584d6496d3b3f605`
response_sha256: `8cccd798ddf994fe5b1cd108b07a5c4215ba879e44762e109bc1b49f549e6d36`

## 137. pilot_070 / ru / qwen/qwen3.8-27b

Вопрос: Кто написал картину «Американская готика»?

Эталон: Grant Wood

Варианты: Грант Вуд

[Источник](https://archive.artic.edu/ryerson/3110)

Ответ модели:

> Картина «Американская готика» была написана американским художником Грантом Вудом в 1930 году.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `94d3f0e3b8641815527273206285bbfad9d5ccfc86c18118c438104874b2bc4f`
response_sha256: `e353ca0071b16ffc9613a23439d5fc219964b3176efca52252f06238af630eeb`

## 138. pilot_071 / en / openai/gpt-oss-20b

Вопрос: Which artist created The Scream?

Эталон: Edvard Munch

Варианты: Munch; Эдвард Мунк; Мунк

[Источник](https://www.munch.no/en/The-Scream/)

Ответ модели:

> The artist who created *The Scream* is Edvard Munch.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `45bb7b1df9a96de48e96e853ef6ebb942dde657f540ecfac38e125df0332372f`
response_sha256: `2cd69ca6c3b24320476ce4d10689caa595fe671da02d5b05e3247baa64fa7668`

## 139. pilot_071 / kk / openai/gpt-oss-20b

Вопрос: «Айқай» туындысын қай суретші жасаған?

Эталон: Edvard Munch

Варианты: Munch; Эдвард Мунк; Мунк

[Источник](https://www.munch.no/en/The-Scream/)

Ответ модели:

> «Айқай» (орысша «Крик») – Эдвард Мунк (Edvard Munch) атты норвегиялық суретші жасаған.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `93d8e1c3f8a6faaed5f17a766dcbd05b2ade0cde2c2c03843ce9b324e8eb2714`
response_sha256: `41fe4c7569a4e9df1f5fbf725354f886211c0cefb54678354b22466de826fbe6`

## 140. pilot_071 / kk / qwen/qwen3.6-27b

Вопрос: «Айқай» туындысын қай суретші жасаған?

Эталон: Edvard Munch

Варианты: Munch; Эдвард Мунк; Мунк

[Источник](https://www.munch.no/en/The-Scream/)

Ответ модели:

> «Айқай» туындысын норвег суретшісі Эдвард Мунк жасаған.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `e1b54261d3a9ce07a59255b659d09829558c8bb20ae90535daa74c20193c945e`
response_sha256: `b62f2761eb418620c22a6300d67a289044f488aae15e875bbe1899c066b904e5`

## 141. pilot_071 / kk / qwen/qwen3.8-27b

Вопрос: «Айқай» туындысын қай суретші жасаған?

Эталон: Edvard Munch

Варианты: Munch; Эдвард Мунк; Мунк

[Источник](https://www.munch.no/en/The-Scream/)

Ответ модели:

> Сұрақтағы алғышарт дұрыс емес. «Айқай» — бұл сурет емес, 1998 жылы шыққан қазақстандық қысқа метражды анимациялық фильм. Оны **Айдарбек Қуанышбаев** режиссер ретінде жасаған (суретші емес).

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `e4b1ee353de4919037361a8b560c000ba582d3c0d16ecd24509db731a13a5ba2`
response_sha256: `9871199fcbf6de438073bd3e38a0d9eae269808e9069c179b92f356e92ea534f`

## 142. pilot_071 / ru / openai/gpt-oss-20b

Вопрос: Какой художник создал «Крик»?

Эталон: Edvard Munch

Варианты: Munch; Эдвард Мунк; Мунк

[Источник](https://www.munch.no/en/The-Scream/)

Ответ модели:

> Художник, создавший «Крик», — Эдвард Мунк.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `9fd44ffa6efa72ccf9faf14f422e769fe8403ba31c033d2040e66aa29d2ec1d7`
response_sha256: `f9baeb057675a2653ffb16030b5110fe8e2d35cccc76d360f8ac9fcd0cea31bb`

## 143. pilot_071 / ru / qwen/qwen3.6-27b

Вопрос: Какой художник создал «Крик»?

Эталон: Edvard Munch

Варианты: Munch; Эдвард Мунк; Мунк

[Источник](https://www.munch.no/en/The-Scream/)

Ответ модели:

> «Крик» создал норвежский художник Эдвард Мунк.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `ec68b3f91ca54e6b99b4d53984e305ed36c12749d22ac92fa33d4cd6ced0cce4`
response_sha256: `b6cae82a9e5e95217b2c26f66749cdf52aa0c9fc821252e5e2ac134d009db1ee`

## 144. pilot_072 / en / openai/gpt-oss-20b

Вопрос: Who painted the Water Lilies cycle displayed at the Musee de l'Orangerie?

Эталон: Claude Monet

Варианты: Monet; Клод Моне; Моне

[Источник](https://www.musee-orangerie.fr/en/node/197502)

Ответ модели:

> Claude Monet painted the Water Lilies cycle displayed at the Musée de l'Orangerie.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `95bbed6c043f6f335c0d3be30550ae92e4d332e53e6a1e097d76efe4147869aa`
response_sha256: `84a1563d900949c5f7616e4000bb10bfefbb55e8dfb10d281fb8fd7225f2073f`

## 145. pilot_072 / kk / openai/gpt-oss-20b

Вопрос: Оранжери музейіндегі «Тұңғиықтар» (Water Lilies) картиналар топтамасын кім салған?

Эталон: Claude Monet

Варианты: Monet; Клод Моне; Моне

[Источник](https://www.musee-orangerie.fr/en/node/197502)

Ответ модели:

> Оранжери музейіндегі «Тұңғиықтар» (Water Lilies) картиналар топтамасын **Клод Моне** салған.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `90ca45f2e2fa3992256ead6a7ff8e0aa6c905df9a15e50888596055f3416fae7`
response_sha256: `32fa24d8fc4cdf8b0bbc17c87d535f79894731b64078389eebfc651bf17a2385`

## 146. pilot_072 / ru / openai/gpt-oss-20b

Вопрос: Кто написал цикл «Кувшинки», представленный в музее Оранжери?

Эталон: Claude Monet

Варианты: Monet; Клод Моне; Моне

[Источник](https://www.musee-orangerie.fr/en/node/197502)

Ответ модели:

> Цикл «Кувшинки», представленный в музее Оранжери, написал французский художник Клод Моне.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `c61f57b42d28683d00cd72fc4a08e26d365183dce496791353ae669768b4f797`
response_sha256: `e54d42ec3e56bad3c14783f6f3774b9b92990b55a66f01932019c5b39f6c1571`

## 147. pilot_072 / ru / qwen/qwen3.6-27b

Вопрос: Кто написал цикл «Кувшинки», представленный в музее Оранжери?

Эталон: Claude Monet

Варианты: Monet; Клод Моне; Моне

[Источник](https://www.musee-orangerie.fr/en/node/197502)

Ответ модели:

> Цикл картин «Кувшинки», представленный в музее Оранжери, написал французский художник-импрессионист **Клод Моне**.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `e403aebd5da94419c8dff1812706edd8f268215819913280198e3e9016d54091`
response_sha256: `7208d326918ef0e496f881efb013cc77c004bcb85c87a10376f716b07f0adb26`

## 148. pilot_073 / en / openai/gpt-oss-20b

Вопрос: In which Kazakh city is the Mausoleum of Khoja Ahmed Yasawi?

Эталон: Turkestan

Варианты: Turkistan; Туркестан; Түркістан

[Источник](https://whc.unesco.org/en/list/1103/)

Ответ модели:

> The Mausoleum of Khoja Ahmed Yasawi is located in the city of Turkistan, Kazakhstan.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `32846f75e431d2f803c49854e8d6629ba6d19e716b08c9b8bc1cb51a75ec9625`
response_sha256: `651a825472dd47c8ca33642c7683a3356da299980bd159993b7ed72696a4b969`

## 149. pilot_073 / kk / openai/gpt-oss-20b

Вопрос: Қожа Ахмет Ясауи кесенесі Қазақстанның қай қаласында орналасқан?

Эталон: Turkestan

Варианты: Turkistan; Туркестан; Түркістан

[Источник](https://whc.unesco.org/en/list/1103/)

Ответ модели:

> Қожа Ахмет Ясауи кесенесі Қазақстанның **Түркістан** қаласында орналасқан.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `d2ab6f38b0607b79741f44aafbcd377566c702ffe20765a6812257393f802695`
response_sha256: `19eb70af57b8febf3a7ac2e99d8490b37cda643f81122f18fa4448ae113582a2`

## 150. pilot_073 / kk / qwen/qwen3.6-27b

Вопрос: Қожа Ахмет Ясауи кесенесі Қазақстанның қай қаласында орналасқан?

Эталон: Turkestan

Варианты: Turkistan; Туркестан; Түркістан

[Источник](https://whc.unesco.org/en/list/1103/)

Ответ модели:

> Түркістан қаласында.

Причина проверки: Needs human review; non-match alone does not establish incorrectness

Оценка / пояснение: ___

request_id: `72bbb453800d8bb04e091db4562be39f1ca1b28768112221124addb87b62be12`
response_sha256: `70a367f226c2faa2975e488ae0cd58a828827503f7808ca617370febeb2a9b55`
