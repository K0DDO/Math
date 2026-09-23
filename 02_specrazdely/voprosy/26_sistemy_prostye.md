# Вопрос 26. Линейные однородные системы. Запись $X'=AX$. Простые (различные) собственные значения

## Что спрашивают на экзамене

- Векторно-матричная запись линейной однородной системы с постоянными коэффициентами.
- Характеристическое уравнение $\det(A-\lambda E)=0$.
- Построение общего решения при **различных** собственных значениях.
- Связь с собственными векторами.

## Все понятия с нуля

**Линейная однородная система с постоянными коэффициентами:**

$$\begin{cases} x_1'=a_{11}x_1+\cdots+a_{1n}x_n, \\\\ \vdots \\\\ x_n'=a_{n1}x_1+\cdots+a_{nn}x_n, \end{cases}$$

или коротко

$$\mathbf{x}'=A\mathbf{x},$$

где $A=(a_{ij})$ — постоянная матрица $n\times n$, $\mathbf{x}=(x_1,\ldots,x_n)^{T}$. ([урок](https://mathprofi.ru/sistemy_differencialnyh_uravnenij.html))

**Собственное значение** $\lambda$ и **собственный вектор** $\mathbf{h}\neq\mathbf{0}$:

$$A\mathbf{h}=\lambda\mathbf{h}\quad\Leftrightarrow\quad (A-\lambda E)\mathbf{h}=\mathbf{0}.$$

([урок](https://mathprofi.ru/sobstvennye_znachenija_i_sobstvennye_vektory.html))

**Простые (различные) корни** — все $\lambda_1,\ldots,\lambda_n$ попарно различны. Тогда автоматически есть $n$ линейно независимых собственных векторов. ([урок](https://mathprofi.ru/kak_reshit_sistemu_differencialnyh_uravnenii.html))

## Теория подробно

Ищем решение вида $\mathbf{x}=\mathbf{h}\,e^{\lambda t}$ ($\mathbf{h}$ — постоянный вектор). Подстановка:

$$\lambda\mathbf{h}\,e^{\lambda t}=A\mathbf{h}\,e^{\lambda t}\Rightarrow (A-\lambda E)\mathbf{h}=\mathbf{0}.$$

Ненулевое $\mathbf{h}$ существует $\Leftrightarrow$ $\det(A-\lambda E)=0$ — **характеристическое уравнение** матрицы $A$. ([урок](https://mathprofi.ru/sobstvennye_znachenija_i_sobstvennye_vektory.html))

Если $\lambda_1,\ldots,\lambda_n$ различны и $\mathbf{h}_1,\ldots,\mathbf{h}_n$ — соответствующие собственные векторы, то

$$\mathbf{x}_i(t)=\mathbf{h}_i e^{\lambda_i t}$$

— ФСР системы, общее решение:

$$\mathbf{x}(t)=C_1\mathbf{h}_1 e^{\lambda_1 t}+\cdots+C_n\mathbf{h}_n e^{\lambda_n t}.$$

([урок](https://mathprofi.ru/kak_reshit_sistemu_differencialnyh_uravnenii.html))
Для $n=2$:

$$\mathbf{x}(t)=C_1\begin{pmatrix} h_{11} \\\\ h_{21} \end{pmatrix}e^{\lambda_1 t} +C_2\begin{pmatrix} h_{12} \\\\ h_{22} \end{pmatrix}e^{\lambda_2 t}.$$

Альтернатива на практике — метод исключения (сведение к одному уравнению 2-го порядка), см. mathprofi; матричный путь короче для устного ответа.

## Как решать / алгоритм

1. Записать матрицу $A$.
2. Вычислить $\det(A-\lambda E)=0$, найти $\lambda_1\neq\lambda_2$ (для $n=2$).
3. Для каждого $\lambda_i$ решить $(A-\lambda_i E)\mathbf{h}_i=\mathbf{0}$, выбрать ненулевой $\mathbf{h}_i$.
4. Записать $\mathbf{x}=C_1\mathbf{h}_1 e^{\lambda_1 t}+C_2\mathbf{h}_2 e^{\lambda_2 t}$.
5. При Коши — подставить $t_0$, найти $C_1,C_2$.

## Разобранный пример

$$\begin{cases} x'=x+2y, \\\\ y'=2x+y. \end{cases} \qquad A=\begin{pmatrix} 1 & 2 \\\\ 2 & 1 \end{pmatrix}.$$

$$\det\begin{pmatrix} 1-\lambda & 2 \\\\ 2 & 1-\lambda \end{pmatrix} =(1-\lambda)^{2}-4=\lambda^{2}-2\lambda-3=0.$$

$$\lambda_1=3,\quad\lambda_2=-1.$$

Для $\lambda=3$: 

$$\begin{pmatrix}-2 & 2 \\\\ 2 & -2\end{pmatrix}\begin{pmatrix}h_1 \\\\ h_2\end{pmatrix}=0$$

 ⇒ $h_2=h_1$. Берём 

$$\mathbf{h}_1=\begin{pmatrix}1 \\\\ 1\end{pmatrix}$$

.

Для $\lambda=-1$: 

$$\begin{pmatrix}2 & 2 \\\\ 2 & 2\end{pmatrix}\mathbf{h}=0$$

 ⇒ $h_2=-h_1$. Берём 

$$\mathbf{h}_2=\begin{pmatrix}1 \\\\ -1\end{pmatrix}$$

.

Общее решение:

$$\begin{cases} x=C_1 e^{3t}+C_2 e^{-t}, \\\\ y=C_1 e^{3t}-C_2 e^{-t}. \end{cases}$$

## Практика

1. 

$$A=\begin{pmatrix}0 & 1 \\\\ 1 & 0\end{pmatrix}$$

 — найти общее решение.
2. 

$$A=\begin{pmatrix}2 & 0 \\\\ 0 & -3\end{pmatrix}$$

 — что будет с координатами?
3. Почему при различных $\lambda$ собственные векторы независимы?
4. Решить задачу Коши для примера выше: $x(0)=2$, $y(0)=0$.

**Ответы:** 1) $\lambda=\pm 1$, $x=C_1 e^{t}+C_2 e^{-t}$, $y=C_1 e^{t}-C_2 e^{-t}$ (с точностью до выбора $\mathbf{h}$); 2) $x=C_1 e^{2t}$, $y=C_2 e^{-3t}$; 3) стандартная теорема линейной алгебры; 4) $C_1=C_2=1$.

## Что сказать устно за 1 минуту

Систему $\mathbf{x}'=A\mathbf{x}$ решаем подстановкой $\mathbf{x}=\mathbf{h}e^{\lambda t}$, получаем задачу на собственные значения. При различных $\lambda_i$ берём собственные векторы $\mathbf{h}_i$ и пишем общее решение как сумму $C_i\mathbf{h}_i e^{\lambda_i t}$. Это фундаментальная система решений линейной однородной системы.

## Источник

- [Системы дифференциальных уравнений (mathprofi)](https://mathprofi.ru/sistemy_differencialnyh_uravnenij.html)
- [Как решить систему ДУ (mathprofi)](https://mathprofi.ru/kak_reshit_sistemu_differencialnyh_uravnenii.html)
