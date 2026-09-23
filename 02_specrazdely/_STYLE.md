# Стиль конспектов спецразделов (обязателен)

Цель: объяснить просто **и** строго. Сейчас было слишком коротко и мутно — каждый файл должен быть развёрнутым учебным текстом.

## Структура каждого вопроса (`voprosy/NN_*.md`)

1. `# Вопрос N. …`
2. `## Зачем это в жизни и на экзамене` — 1 абзац «зачем» + bullet «что спросят»
3. `## Интуиция на пальцах` — без формул или с минимумом; аналогия из мира
4. `## Все понятия с нуля` — каждый термин: интуиция → определение → как проверить/найти → ([урок](url))
5. `## Теория подробно` — формулы, теоремы с пояснением «что это значит словами»
6. `## Примеры из практики (мир)` — 2–4 реальных применения (физика, экономика, компьютерная графика, инженерия, биология…) с короткой математической моделью
7. `## Алгоритм «как решать на экзамене»` — нумерованные шаги
8. `## Разобранный пример` — полный расчёт
9. `## Практика` — 3–5 задач с ответами
10. `## Что сказать устно за 1–2 минуты`
11. `## Источник` — ссылки Mathprofi

## Математика для GitHub (жёстко)

- Только `$...$` и `$$...$$` (не `\(...\)`, не `align*`)
- `\mathrm{rang}`, `\mathrm{def}`, не `\operatorname`
- Сопряжение: `A^{\ast}` (не `A^*`)
- Транспонирование: `A^{\top}` (не `A^T`)
- Матрицы и системы — в **отдельных** блоках `$$...$$`, не внутри пунктов списка inline
- Разрыв строк матрицы: в файле четыре слэша `\\\\` внутри одного `$$...$$` в одну строку, ИЛИ многострочный `$$` без пустых строк внутри
- Не начинать inline-формулу с `$(` — пиши словами или выноси в `$$`
- Не использовать `\cr`

## Тон

- Пиши по-русски, обращайся на «ты» или безлично («берем», «получаем»)
- После каждой формулы — одно предложение: «это значит, что…»
- Не сокращай определения до одной строки
- Связывай с другими вопросами: «см. вопрос N»

## Mathprofi URL (только эти)

- https://mathprofi.ru/linejnye_preobrazovanija.html
- https://mathprofi.ru/sobstvennye_znachenija_i_sobstvennye_vektory.html
- https://mathprofi.ru/kvadratichnye_formy.html
- https://mathprofi.ru/kak_privesti_kf_k_kanonicheskomu_vidu.html
- https://mathprofi.ru/metod_ortogonalnogo_preobrazovaniya_kf.html
- https://mathprofi.ru/kak_privesti_uravnenie_linii_2_poryadka_k_kanonicheskomu_vidu.html
- https://mathprofi.ru/svoistva_operacij_nad_matricami_matrichnye_vyrazheniya.html
- https://mathprofi.ru/rang_matricy.html
- https://mathprofi.ru/odnorodnye_sistemy_lineinyh_uravnenij.html
- https://mathprofi.ru/kak_vychislit_opredelitel.html
- https://mathprofi.ru/dejstviya_s_matricami.html
- https://mathprofi.ru/obratnaya_matrica_metod_zhordana_gaussa.html
- https://mathprofi.ru/vektory_dlya_chainikov.html
- https://mathprofi.ru/lineinaya_zavisimost_vektorov_bazis.html
- https://mathprofi.ru/skalyarnoe_proizvedenie_vektorov.html
- https://mathprofi.ru/differencialnye_uravnenija_primery_reshenii.html
- https://mathprofi.ru/odnorodnye_diffury_pervogo_poryadka.html
- https://mathprofi.ru/du_svodjashiesja_k_odnorodnym.html
- https://mathprofi.ru/lineinye_differencialnye_uravnenija.html
- https://mathprofi.ru/differencialnye_uravnenija_v_polnyh_differencialah.html
- https://mathprofi.ru/differencialnoe_uravnenie_bernulli.html
- https://mathprofi.ru/differencialnye_uravnenija_dopuskajushie_ponizhenie_poryadka.html
- https://mathprofi.ru/differencialnye_uravnenija_vtorogo_poryadka.html
- https://mathprofi.ru/kak_reshit_neodnorodnoe_uravnenie_vtorogo_poryadka.html
- https://mathprofi.ru/linejnye_diffury_vysshih_porjadkov.html
- https://mathprofi.ru/metod_variacii_proizvolnyh_postoyannyh.html
- https://mathprofi.ru/sistemy_differencialnyh_uravnenij.html
- https://mathprofi.ru/kak_reshit_sistemu_differencialnyh_uravnenii.html
