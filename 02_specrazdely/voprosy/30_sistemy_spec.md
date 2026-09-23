# Вопрос 30. Неоднородные системы. Метод специальной правой части

## Что спрашивают на экзамене

- Когда применим метод подбора для систем.
- Аналогия с таблицей для скалярных ЛНДУ (вопрос 24).
- Роль множителя $t^{s}$, где $s$ — кратность $\alpha+i\beta$ как собственного значения $A$.
- Довести пример: вид $\mathbf{x}_{\mathrm{ч}}$ → подстановка → линейная алгебраическая система на векторные коэффициенты.

## Все понятия с нуля

Система $\mathbf{x}'=A\mathbf{x}+\mathbf{g}(t)$ с **постоянной** матрицей $A$.

**Специальная правая часть** — вектор-функция вида
$$
\mathbf{g}(t)=e^{\alpha t}\bigl(\mathbf{P}_m(t)\cos\beta t+\mathbf{Q}_n(t)\sin\beta t\bigr),
$$
где $\mathbf{P}_m$, $\mathbf{Q}_n$ — вектор-многочлены (координаты — обычные многочлены).

Частные случаи:
- постоянный вектор / многочлен;
- $\mathbf{p}\,e^{\alpha t}$;
- $\mathbf{a}\cos\beta t+\mathbf{b}\sin\beta t$.

**Метод специальной правой части** — подбираем $\mathbf{x}_{\mathrm{ч}}$ того же «структурного» вида с неопределёнными векторными коэффициентами и находим их подстановкой в систему.

Если $\mathbf{g}$ не специальная — вариация (вопрос 29).

## Теория подробно

Структура: $\mathbf{x}=\mathbf{x}_{\mathrm{о}}+\mathbf{x}_{\mathrm{ч}}$, где $\mathbf{x}_{\mathrm{о}}$ — общее решение однородной $\mathbf{x}'=A\mathbf{x}$.

### Правило подбора

1. Составить $\gamma=\alpha+i\beta$ по виду $\mathbf{g}$.
2. Найти, является ли $\gamma$ собственным значением $A$, и с какой алгебраической кратностью $s$ ($s=0$, если не является).
3. Искать
$$
\mathbf{x}_{\mathrm{ч}}=t^{s}e^{\alpha t}\bigl(\mathbf{R}_l(t)\cos\beta t+\mathbf{S}_l(t)\sin\beta t\bigr),
$$
где $l=\max(m,n)$, а $\mathbf{R}_l$, $\mathbf{S}_l$ — вектор-многочлены степени $l$ с неопределёнными коэффициентами.
4. Подставить в $\mathbf{x}'=A\mathbf{x}+\mathbf{g}$, приравнять коэффициенты при $t^{k}e^{\alpha t}\cos\beta t$, $t^{k}e^{\alpha t}\sin\beta t$ и т.д.
5. Если $\mathbf{g}=\mathbf{g}_1+\mathbf{g}_2$ — суперпозиция.

### Частые шаблоны ($n=2$)

| $\mathbf{g}(t)$ | Вид $\mathbf{x}_{\mathrm{ч}}$ |
|-----------------|------------------------------|
| $\mathbf{p}$ (постоянный) | $t^{s}\mathbf{q}$ (или $t^{s}(\mathbf{a}+\mathbf{b}t)$ при многочлене), $s=$ кратность $\lambda=0$ |
| $\mathbf{p}e^{\alpha t}$ | $t^{s}\mathbf{q}e^{\alpha t}$, $s=$ кратность $\alpha$ |
| $\mathbf{a}\cos\beta t+\mathbf{b}\sin\beta t$ | $t^{s}\bigl(\mathbf{u}\cos\beta t+\mathbf{v}\sin\beta t\bigr)$, $s=$ кратность $\pm i\beta$ |

Даже если в $\mathbf{g}$ только $\cos$, в подборе держат и $\sin$ (векторы $\mathbf{u},\mathbf{v}$).

**Важный нюанс:** иногда при резонансе для систем стандартного $t^{s}$ недостаточно из‑за жордановой структуры; на типовом экзамене обычно хватает правила с алгебраической кратностью. Если система для коэффициентов неразрешима — повышают степень $t$ ещё на 1.

## Как решать / алгоритм

1. Решить однородную → $\mathbf{x}_{\mathrm{о}}$ (вопросы 26–28).
2. По $\mathbf{g}$ выбрать вид $\mathbf{x}_{\mathrm{ч}}$ с учётом $s$.
3. Вычислить $\mathbf{x}_{\mathrm{ч}}'$.
4. Подставить: $\mathbf{x}_{\mathrm{ч}}'=A\mathbf{x}_{\mathrm{ч}}+\mathbf{g}$.
5. Получить алгебраическую систему на неизвестные компоненты векторов.
6. Записать ответ $\mathbf{x}=\mathbf{x}_{\mathrm{о}}+\mathbf{x}_{\mathrm{ч}}$.

## Разобранный пример

$$
\begin{cases}
x'=3x-y+1, \cr
y'=4x-y+2.
\end{cases}
\qquad
A=\begin{pmatrix}
3 & -1 \cr
4 & -1
\end{pmatrix},\quad
\mathbf{g}=\begin{pmatrix}
1 \cr
2
\end{pmatrix}.
$$

**Однородная.** $\det(A-\lambda E)=(3-\lambda)(-1-\lambda)+4=\lambda^{2}-2\lambda+1=(\lambda-1)^{2}$.
$\lambda=1$ кратности 2. Это однородная часть — как в вопросе 27; для неоднородной правой части важно другое: $\gamma=0$ (постоянная $\mathbf{g}$), является ли $0$ собственным значением? $\det A=3\cdot(-1)-(-1)\cdot 4=1\neq 0$, значит $0$ **не** собственное, $s=0$.

Ищем постоянное частное $\mathbf{x}_{\mathrm{ч}}=\begin{pmatrix}a \cr b\end{pmatrix}$:
$$
\mathbf{0}=A\begin{pmatrix}
a \cr
b
\end{pmatrix}+\begin{pmatrix}
1 \cr
2
\end{pmatrix}
\Rightarrow
\begin{cases}
3a-b=-1, \cr
4a-b=-2.
\end{cases}
$$
Вычитая: $a=-1$, тогда $-3-b=-1\Rightarrow b=-2$.
$$
\mathbf{x}_{\mathrm{ч}}=\begin{pmatrix}
-1 \cr
-2
\end{pmatrix}.
$$

Общее решение: $\mathbf{x}=\mathbf{x}_{\mathrm{о}}+\mathbf{x}_{\mathrm{ч}}$, где $\mathbf{x}_{\mathrm{о}}$ — общее однородной с $\lambda=1$ (кратный случай).

**Резонансный пример-схема:** если $\mathbf{g}=\mathbf{p}e^{t}$, а $\lambda=1$ — собственное кратности $s$, ищем $\mathbf{x}_{\mathrm{ч}}=t^{s}(\mathbf{q}+\ldots)e^{t}$ (часто $s=1$ или $2$).

## Практика

1. Для $\mathbf{x}'=\begin{pmatrix}0&1 \cr 1&0\end{pmatrix}\mathbf{x}+\begin{pmatrix}e^{2t} \cr 0\end{pmatrix}$ какой вид $\mathbf{x}_{\mathrm{ч}}$? ($s=$?)
2. $\mathbf{g}=\begin{pmatrix}\cos t \cr \sin t\end{pmatrix}$, собственные значения $A$ равны $\pm 2i$. Какой $s$?
3. Почему при $\mathbf{g}=\mathbf{a}\cos\beta t$ всё равно вводят $\mathbf{u}\cos+\mathbf{v}\sin$?
4. Когда метод специальной правой части неприменим?

**Ответы:** 1) $\lambda=\pm 1$, для $\alpha=2$ имеем $s=0$, $\mathbf{x}_{\mathrm{ч}}=\mathbf{q}e^{2t}$; 2) $\pm i$ не совпадают с $\pm 2i$, $s=0$; 3) производные смешивают $\sin$ и $\cos$; 4) если $\mathbf{g}$ не специальная (например $1/t$, $\mathrm{tg}\,t$).

## Что сказать устно за 1 минуту

При постоянной $A$ и специальной правой части $e^{\alpha t}(\mathbf{P}\cos\beta t+\mathbf{Q}\sin\beta t)$ частное решение ищут тем же видом, умноженным на $t^{s}$, где $s$ — кратность $\alpha+i\beta$ среди собственных значений $A$. Неопределённые векторные коэффициенты находят подстановкой в систему. Если правая часть не специальная — только вариация произвольных постоянных.

## Источник

- [Системы дифференциальных уравнений (mathprofi)](https://mathprofi.ru/sistemy_differencialnyh_uravnenij.html)
- [Как решить систему ДУ (mathprofi)](https://mathprofi.ru/kak_reshit_sistemu_differencialnyh_uravnenii.html)
- [Неоднородные уравнения второго порядка (mathprofi)](https://mathprofi.ru/kak_reshit_neodnorodnoe_uravnenie_vtorogo_poryadka.html)
