# Вопрос 29. Неоднородные системы. Метод вариации произвольных постоянных

## Что спрашивают на экзамене

- Вид линейной неоднородной системы $\mathbf{x}'=A\mathbf{x}+\mathbf{g}(t)$ (или $A(t)$).
- Структура общего решения: $\mathbf{x}=\mathbf{x}_{\mathrm{о}}+\mathbf{x}_{\mathrm{ч}}$.
- Фундаментальная матрица $\Phi(t)$.
- Формулы вариации: $\Phi\mathbf{c}'=\mathbf{g}$, $\mathbf{c}=\int\Phi^{-1}\mathbf{g}\,dt$.
- Уметь расписать для $n=2$ систему на $C_1',C_2'$.

## Все понятия с нуля

**Неоднородная линейная система:**
$$
\mathbf{x}'=A(t)\mathbf{x}+\mathbf{g}(t),
$$
где $\mathbf{g}(t)\not\equiv\mathbf{0}$ — вектор правых частей. Часто $A$ постоянна.

**Однородная:** $\mathbf{x}'=A\mathbf{x}$. Её общее решение $\mathbf{x}_{\mathrm{о}}=\Phi(t)\mathbf{c}$, $\mathbf{c}$ — постоянный вектор.

**Фундаментальная матрица** $\Phi(t)$ — матрица, столбцы которой — линейно независимые решения однородной системы (ФСР в матричной форме). Тогда $\Phi'=A\Phi$ и $\det\Phi\neq 0$.

**Вариация постоянных:** ищем частное решение в виде $\mathbf{x}_{\mathrm{ч}}=\Phi(t)\mathbf{c}(t)$, где $\mathbf{c}(t)$ — уже **функции**.

## Теория подробно

Подставляем $\mathbf{x}=\Phi\mathbf{c}(t)$ в неоднородную систему:
$$
\Phi'\mathbf{c}+\Phi\mathbf{c}'=A\Phi\mathbf{c}+\mathbf{g}.
$$
Но $\Phi'=A\Phi$, поэтому
$$
\Phi\mathbf{c}'=\mathbf{g}\quad\Rightarrow\quad\mathbf{c}'=\Phi^{-1}\mathbf{g},\quad
\mathbf{c}(t)=\int\Phi^{-1}(t)\mathbf{g}(t)\,dt
$$
(для частного решения константу интегрирования можно взять нулевой).

Общее решение неоднородной:
$$
\mathbf{x}(t)=\Phi(t)\mathbf{c}+\Phi(t)\int\Phi^{-1}(t)\mathbf{g}(t)\,dt.
$$

### Для $n=2$ без матричной записи

Если однородное решение
$$
\begin{cases}
x=C_1 x_1(t)+C_2 x_2(t),\\
y=C_1 y_1(t)+C_2 y_2(t),
\end{cases}
$$
то варьируем $C_1(t),C_2(t)$ и ставим систему
$$
\begin{cases}
C_1' x_1+C_2' x_2=g_1(t),\\
C_1' y_1+C_2' y_2=g_2(t),
\end{cases}
$$
где $\mathbf{g}=(g_1,g_2)^{T}$. Определитель — вронскиан столбцов ФСР (равен $\det\Phi$).

Это полный аналог скалярной вариации (вопрос 22).

## Как решать / алгоритм

1. Решить однородную $\mathbf{x}'=A\mathbf{x}$ → два (или $n$) независимых решений → собрать $\Phi$.
2. Вычислить $\Phi^{-1}$ (или решить $\Phi\mathbf{c}'=\mathbf{g}$ по Крамеру).
3. Найти $\mathbf{c}'$, проинтегрировать $\mathbf{c}(t)$.
4. $\mathbf{x}_{\mathrm{ч}}=\Phi\mathbf{c}(t)$.
5. $\mathbf{x}=\Phi\mathbf{c}_{\mathrm{const}}+\mathbf{x}_{\mathrm{ч}}$.
6. При Коши — определить постоянный вектор $\mathbf{c}$.

## Разобранный пример

$$
\begin{cases}
x'=y,\\
y'=-x+e^{t},
\end{cases}
\qquad
A=\begin{pmatrix}0 & 1\\ -1 & 0\end{pmatrix},\quad
\mathbf{g}=\begin{pmatrix}0\\ e^{t}\end{pmatrix}.
$$

Однородная $\mathbf{x}'=A\mathbf{x}$: $\lambda=\pm i$, ФСР
$$
\mathbf{x}_1=\begin{pmatrix}\cos t\\ -\sin t\end{pmatrix},\quad
\mathbf{x}_2=\begin{pmatrix}\sin t\\ \cos t\end{pmatrix}.
$$
$$
\Phi=\begin{pmatrix}\cos t & \sin t\\ -\sin t & \cos t\end{pmatrix},\quad
\det\Phi=1,\quad
\Phi^{-1}=\begin{pmatrix}\cos t & -\sin t\\ \sin t & \cos t\end{pmatrix}.
$$

$$
\mathbf{c}'=\Phi^{-1}\mathbf{g}=\begin{pmatrix}-\sin t\cdot e^{t}\\ \cos t\cdot e^{t}\end{pmatrix}.
$$

Интегрируя (формулы $\int e^{t}\sin t\,dt$, $\int e^{t}\cos t\,dt$):
$$
c_1=\int(-e^{t}\sin t)\,dt=\frac{e^{t}}{2}(\cos t-\sin t),\qquad
c_2=\int e^{t}\cos t\,dt=\frac{e^{t}}{2}(\sin t+\cos t)
$$
(без произвольных постоянных).

$$
\mathbf{x}_{\mathrm{ч}}=\Phi\begin{pmatrix}c_1\\ c_2\end{pmatrix}
=\frac{e^{t}}{2}\begin{pmatrix}
\cos t(\cos t-\sin t)+\sin t(\sin t+\cos t)\\
-\sin t(\cos t-\sin t)+\cos t(\sin t+\cos t)
\end{pmatrix}
=\frac{e^{t}}{2}\begin{pmatrix}1\\ 1\end{pmatrix}.
$$

Проверка: $x_{\mathrm{ч}}=\frac12 e^{t}$, $y_{\mathrm{ч}}=\frac12 e^{t}$,
$$
x_{\mathrm{ч}}'= \tfrac12 e^{t}=y_{\mathrm{ч}},\qquad
y_{\mathrm{ч}}'=\tfrac12 e^{t}=-x_{\mathrm{ч}}+e^{t}.
$$

Общее решение:
$$
\begin{cases}
x=C_1\cos t+C_2\sin t+\dfrac12 e^{t},\\
y=-C_1\sin t+C_2\cos t+\dfrac12 e^{t}.
\end{cases}
$$

## Практика

1. Выписать систему на $C_1',C_2'$ для $\mathbf{g}=(t,1)^{T}$, если $\Phi=\begin{pmatrix}e^{t}&e^{-t}\\ e^{t}&-e^{-t}\end{pmatrix}$.
2. Чему равно $\Phi'$, если столбцы — решения $\mathbf{x}'=A\mathbf{x}$?
3. Чем вариация для систем отличается от скалярной?
4. Когда выгоднее метод специальной правой части (вопрос 30)?

**Ответы:** 1) $\Phi\mathbf{c}'=\mathbf{g}$; 2) $\Phi'=A\Phi$; 3) те же идеи, векторная запись; 4) когда $\mathbf{g}$ специальная и $A$ постоянна — быстрее подбор.

## Что сказать устно за 1 минуту

Для $\mathbf{x}'=A\mathbf{x}+\mathbf{g}$ сначала решаем однородную, собираем фундаментальную матрицу $\Phi$. Частное ищем как $\Phi\mathbf{c}(t)$; из уравнения следует $\Phi\mathbf{c}'=\mathbf{g}$, откуда $\mathbf{c}=\int\Phi^{-1}\mathbf{g}\,dt$. Общее решение — $\Phi\mathbf{c}+\mathbf{x}_{\mathrm{ч}}$. Для $n=2$ это система двух уравнений на $C_1',C_2'$.

## Источник

- [Системы дифференциальных уравнений (mathprofi)](https://mathprofi.ru/sistemy_differencialnyh_uravnenij.html)
- [Метод вариации произвольных постоянных (mathprofi)](https://mathprofi.ru/metod_variacii_proizvolnyh_postoyannyh.html)
- [Как решить систему ДУ (mathprofi)](https://mathprofi.ru/kak_reshit_sistemu_differencialnyh_uravnenii.html)
