# Практика по спецразделам

Сложность та же, что у теста на 60 по матану: конкретная матрица 2×2 / 3×3 или конкретное ДУ, довести до числа / явной функции.

Главный задачник по диффурам — **Филиппов**. Главный задачник по операторам — **Проскуряков** (или Кузнецов, линейная алгебра). Разборы — Mathprofi + решебники ниже.

## Как тренироваться

На операторы: один день = 4 матрицы до диагонального вида.

На ДУ: один день = 6 уравнений, каждое другого типа. Сначала определи тип, потом решай. Если сразу хватаешься за формулу Бернулли на разделяющихся — тип не видишь, на экзамене это смерть.

Проверка ДУ: подставь ответ в уравнение и в начальные условия.

---

## Операторы и формы — план

| День | Что решать | Урок | Решебник |
|---|---|---|---|
| 1 | матрица оператора, ядро, ранг, \(A'=T^{-1}AT\) | [собственные значения](https://mathprofi.ru/sobstvennye_znacheniya_i_sobstvennye_vektory.html) | Проскуряков, линейные преобразования; [примеры ядра/образа](https://mathprofi.ru/) |
| 2 | собственные числа и векторы 2×2 и 3×3 | тот же урок | 6 матриц до базиса из собственных векторов |
| 3 | квадратичная форма, Лагранж | [квадратичные формы](https://mathprofi.ru/kvadratichnye_formy.html) | привести 4 формы к каноническому виду |
| 4 | Сильвестр | тот же урок, конец | 5 форм: определённые / нет |
| 5 | кривая 2 порядка к канону | [линии 2 порядка](https://mathprofi.ru/kak_privesti_uravnenie_linii_2_poryadka_k_kanonicheskomu_vidu.html) | эллипс / гипербола / парабола, по одной |

Мини-набор (сначала сам):

1. Оператор в базисе имеет матрицу \(A=\begin{pmatrix}1&2\\0&3\end{pmatrix}\). Найти собственные числа, векторы, диагональный вид.
2. \(A=\begin{pmatrix}2&1\\1&2\end{pmatrix}\). Построить ортогональный собственный базис (симметричная).
3. \(Q=x^2+4xy+y^2\). Сильвестр и канонический вид.
4. \(Q=x^2+y^2-z^2+2xy\). Знакоопределённость.
5. \(x^2+4xy+4y^2+2x=0\) привести к канону.

Wolfram: запрос `eigenvalues {{1,2},{0,3}}`.

---

## Диффуры — план по Филиппову

Решебник: [taskall.ru/Filippov](https://taskall.ru/Filippov/index.htm), список номеров с решениями: [mat-an.ru/filippov.php](http://mat-an.ru/filippov.php).

Уроки Mathprofi — в таблице. Бери из каждого параграфа Филиппова **по 5 номеров**, не все подряд.

| День | Тема | Филиппов | Урок |
|---|---|---|---|
| 1 | поле направлений, разделяющиеся | §1–3, номера из решебника 51–100 | [ДУ 1 порядка](https://mathprofi.ru/differencialnye_uravneniya_primery_reshenij.html) |
| 2 | однородные | §4, 101–120 | [однородные](https://mathprofi.ru/odnorodnye_differencialnye_uravneniya_pervogo_poryadka.html) |
| 3 | линейные 1 порядка | §5, 136–155 | [линейные 1 порядка](https://mathprofi.ru/lineinye_differencialnye_uravneniya.html) |
| 4 | полные дифференциалы, Бернулли | §6, 186–205 | [полные](https://mathprofi.ru/differencialnye_uravneniya_v_polnyh_differencialah.html), [Бернулли](https://mathprofi.ru/uravnenie_bernulli.html) |
| 5 | понижение порядка | §10, 421–440 | [понижение порядка](https://mathprofi.ru/differencialnye_uravneniya_vtorogo_poryadka_ponizhenie.html) |
| 6 | ЛОДУ с пост. коэфф. | §11, 511–540 | [однородные 2 порядка](https://mathprofi.ru/odnorodnye_du_vtorogo_poryadka.html) |
| 7 | ЛНДУ, неопределённые коэффициенты | §11, 548–570 | [неоднородные 2 порядка](https://mathprofi.ru/neodnorodnye_du_vtorogo_poryadka.html) |
| 8 | вариация постоянных | §11, 575–590 | [вариация](https://mathprofi.ru/metod_variacii_proizvolnyh_postoyannyh.html) |
| 9 | системы, простые корни | §14, 786–820 | [системы ДУ](https://mathprofi.ru/kak_reshit_sistemu_differencialnyh_uravnenii.html) |
| 10 | кратные и комплексные, неоднородные системы | §14 дальше | тот же урок + [операционное исчисление](https://mathprofi.ru/reshenie_du_metodom_operacionnogo_ischisleniya.html) как запасной метод |

Кузнецов §5 — те же типы, удобно как «вариант контрольной». Решения: [mat-an.ru/kuznecov.php](http://mat-an.ru/kuznecov.php) §5.

---

## Разобранные задачи уровня экзамена

### А. Собственные числа

\(A=\begin{pmatrix}1&2\\0&3\end{pmatrix}\).

\(\det(A-\lambda I)=(1-\lambda)(3-\lambda)=0\), \(\lambda=1,3\).

\(\lambda=1\): \((A-I)v=\begin{pmatrix}0&2\\0&2\end{pmatrix}v=0\Rightarrow v=(1,0)\).

\(\lambda=3\): \(\begin{pmatrix}-2&2\\0&0\end{pmatrix}v=0\Rightarrow v=(1,1)\).

\(T=\begin{pmatrix}1&1\\0&1\end{pmatrix}\), \(A'=T^{-1}AT=\operatorname{diag}(1,3)\).

### Б. Сильвестр

\(Q=x^2+4xy+y^2\), матрица \(\begin{pmatrix}1&2\\2&1\end{pmatrix}\).

Угловые миноры: \(\Delta_1=1>0\), \(\Delta_2=1-4=-3<0\). Не определённая (знакопеременная). Собственные числа \(1\pm 2\), то есть \(3\) и \(-1\), подтверждает.

### В. Линейное ДУ 1 порядка

\(y'+y=e^x\), \(y(0)=0\).

Интегрирующий множитель \(e^{\int dx}=e^x\), \((ye^x)'=e^{2x}\), \(ye^x=\frac12 e^{2x}+C\), \(y=\frac12 e^x+Ce^{-x}\).

\(y(0)=0\Rightarrow C=-1/2\), \(y=\frac12(e^x-e^{-x})=\sinh x\).

### Г. ЛНДУ 2 порядка

\(y''-3y'+2y=e^{3x}\).

Характеристическое \(k^2-3k+2=0\), \(k=1,2\). Однородное: \(C_1e^x+C_2e^{2x}\).

Правая часть \(e^{3x}\), \(3\) не корень \(\Rightarrow y_ч=Ae^{3x}\). Подстановка: \(9A-9A+2A=1\), \(A=1/2\).

\(y=\frac12 e^{3x}+C_1e^x+C_2e^{2x}\).

### Д. Система, простые корни

\(x'=3x+y\), \(y'=x+3y\). Матрица \(\begin{pmatrix}3&1\\1&3\end{pmatrix}\), \(\lambda=4,2\).

\(\lambda=4\): вектор \((1,1)\). \(\lambda=2\): \((1,-1)\).

$$
\begin{pmatrix}x\\y\end{pmatrix}=C_1 e^{4t}\begin{pmatrix}1\\1\end{pmatrix}+C_2 e^{2t}\begin{pmatrix}1\\-1\end{pmatrix}.
$$

---

## Если совсем не идёт

1. Открой Mathprofi по типу уравнения и **перереши все примеры урока на бумаге**.
2. Только потом Филиппов.
3. Не прыгай к системам, пока не ставишь ФСР для \(y''+py'+qy=0\) за 40 секунд.
