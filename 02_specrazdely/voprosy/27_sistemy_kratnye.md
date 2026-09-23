# Вопрос 27. Линейные однородные системы: кратные действительные собственные значения

## Что спрашивают на экзамене

- Что меняется, когда $\lambda$ имеет алгебраическую кратность $m>1$.
- Случай полного набора собственных векторов (диагонализируемость).
- Случай дефицита: присоединённые векторы, решения вида $(\mathbf{h}t+\mathbf{g})e^{\lambda t}$.
- Уметь разобрать $n=2$ с двукратным $\lambda$.

## Все понятия с нуля

**Алгебраическая кратность** $\lambda$ — кратность корня характеристического многочлена.

**Геометрическая кратность** — $\dim\ker(A-\lambda E)$ = число независимых собственных векторов.

Всегда геометрическая $\le$ алгебраической. Если строго меньше — матрица **не диагонализируема**, нужны **присоединённые (обобщённые) векторы**.

**Присоединённый вектор** $\mathbf{g}$ к собственному $\mathbf{h}$ (для жордановой клетки $2\times 2$):
$$
(A-\lambda E)\mathbf{g}=\mathbf{h},\qquad (A-\lambda E)\mathbf{h}=\mathbf{0}.
$$

## Теория подробно

Система $\mathbf{x}'=A\mathbf{x}$, $\lambda$ — действительный корень кратности $m$.

### Случай 1. Достаточно собственных векторов

Если есть $m$ независимых собственных векторов $\mathbf{h}_1,\ldots,\mathbf{h}_m$, то вклад в общее решение такой же, как при простых корнях:
$$
(C_1\mathbf{h}_1+\cdots+C_m\mathbf{h}_m)e^{\lambda t}.
$$
Для $n=2$ и $\lambda_1=\lambda_2=\lambda$ это бывает, когда $A=\lambda E$ (тогда любой вектор — собственный).

### Случай 2. Один собственный вектор при $m=2$ (типичный экзамен)

Пусть $n=2$, $\lambda$ двукратный, $\ker(A-\lambda E)$ одномерен, базис — $\mathbf{h}$.

Ищем второе решение в виде
$$
\mathbf{x}_2(t)=(\mathbf{h}\,t+\mathbf{g})e^{\lambda t}.
$$
Подстановка даёт:
$$
(A-\lambda E)\mathbf{h}=\mathbf{0},\qquad (A-\lambda E)\mathbf{g}=\mathbf{h}.
$$
Первое решение: $\mathbf{x}_1=\mathbf{h}\,e^{\lambda t}$.

Общее:
$$
\mathbf{x}=C_1\mathbf{h}\,e^{\lambda t}+C_2(\mathbf{h}\,t+\mathbf{g})e^{\lambda t}
=\bigl((C_1+C_2 t)\mathbf{h}+C_2\mathbf{g}\bigr)e^{\lambda t}.
$$

Покоординатно часто получается вид
$$
x=(a_1+b_1 t)e^{\lambda t},\quad y=(a_2+b_2 t)e^{\lambda t}
$$
со связанными константами.

Для $n>2$ строят жордановы цепочки большей длины; на экзамене обычно хватает $n=2$.

## Как решать / алгоритм ($n=2$, кратный $\lambda$)

1. Найти $\lambda$ из $\det(A-\lambda E)=0$; убедиться, что кратность 2.
2. Решить $(A-\lambda E)\mathbf{h}=0$. Если два независимых $\mathbf{h}$ — случай 1.
3. Иначе найти $\mathbf{g}$ из $(A-\lambda E)\mathbf{g}=\mathbf{h}$ (система совместна).
4. Записать $\mathbf{x}=C_1\mathbf{h}e^{\lambda t}+C_2(\mathbf{h}t+\mathbf{g})e^{\lambda t}$.
5. Проверить подстановкой в исходную систему.

## Разобранный пример

$$
A=\begin{pmatrix}2 & -1\\ 1 & 0\end{pmatrix}.
$$

$$
\det\begin{pmatrix}2-\lambda & -1\\ 1 & -\lambda\end{pmatrix}
=\lambda^{2}-2\lambda+1=(\lambda-1)^{2}=0.
$$
$\lambda=1$ кратности 2.

$(A-E)\mathbf{h}=\begin{pmatrix}1 & -1\\ 1 & -1\end{pmatrix}\mathbf{h}=0$ ⇒ $h_1=h_2$. Берём $\mathbf{h}=\begin{pmatrix}1\\ 1\end{pmatrix}$.

Второй независимый собственный вектор нет (ранг $A-E$ равен 1).

Ищем $\mathbf{g}=\begin{pmatrix}g_1\\ g_2\end{pmatrix}$:
$$
\begin{pmatrix}1 & -1\\ 1 & -1\end{pmatrix}\begin{pmatrix}g_1\\ g_2\end{pmatrix}=\begin{pmatrix}1\\ 1\end{pmatrix}
\Rightarrow g_1-g_2=1.
$$
Берём $g_2=0$, $g_1=1$, то есть $\mathbf{g}=\begin{pmatrix}1\\ 0\end{pmatrix}$.

Общее решение:
$$
\mathbf{x}=C_1\begin{pmatrix}1\\ 1\end{pmatrix}e^{t}
+C_2\left(\begin{pmatrix}1\\ 1\end{pmatrix}t+\begin{pmatrix}1\\ 0\end{pmatrix}\right)e^{t},
$$
$$
\begin{cases}
x=(C_1+C_2 t+C_2)e^{t}=(C_1+C_2+C_2 t)e^{t},\\
y=(C_1+C_2 t)e^{t}.
\end{cases}
$$
(Переобозначение констант допустимо: $x=(A+Bt)e^{t}$, $y=(A-B+Bt)e^{t}$ и т.п. — главное согласовать связь.)

## Практика

1. $A=\begin{pmatrix}1 & 1\\ 0 & 1\end{pmatrix}$ — найти общее решение.
2. $A=\begin{pmatrix}3 & 0\\ 0 & 3\end{pmatrix}$ — какой случай?
3. Почему уравнение $(A-\lambda E)\mathbf{g}=\mathbf{h}$ обязательно совместно, если $\mathbf{h}$ — собственный и клетка жорданова?
4. Сравнить вид решения с кратным корнем у скалярного ДУ $y''-2y'+y=0$.

**Ответы:** 1) $\lambda=1$, $\mathbf{h}=(1,0)$, $\mathbf{g}=(0,1)$ (проверить), $x=(C_1+C_2 t)e^{t}$, $y=C_2 e^{t}$; 2) диагонализируемый, $x=C_1 e^{3t}$, $y=C_2 e^{3t}$; 3) $\mathbf{h}\in\mathrm{Im}(A-\lambda E)$ в жордановой теории; 4) множитель $t$ появляется и там, и там.

## Что сказать устно за 1 минуту

При кратном действительном $\lambda$ смотрим число собственных векторов. Если их столько, сколько кратность — решение как обычно, с $e^{\lambda t}$. Если не хватает — строим присоединённый вектор из $(A-\lambda E)\mathbf{g}=\mathbf{h}$ и добавляем решение $(\mathbf{h}t+\mathbf{g})e^{\lambda t}$. Для $2\times 2$ это стандартная жорданова клетка.

## Источник

- [Системы дифференциальных уравнений (mathprofi)](https://mathprofi.ru/sistemy_differencialnyh_uravnenij.html)
- [Как решить систему ДУ (mathprofi)](https://mathprofi.ru/kak_reshit_sistemu_differencialnyh_uravnenii.html)
