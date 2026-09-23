# Вопрос 28. Линейные однородные системы: комплексные собственные значения

## Что спрашивают на экзамене

- Что делать, если $\lambda=\alpha\pm i\beta$ — комплексно сопряжённая пара.
- Как из комплексного решения получить два действительных.
- Формулы с $\mathbf{u},\mathbf{v}$ (действительная и мнимая части собственного вектора).
- Пример с числами (часто «вращение» / колебания).

## Все понятия с нуля

При действительной матрице $A$ комплексные собственные значения идут **парами** $\alpha\pm i\beta$, $\beta\neq 0$.

**Комплексный собственный вектор** $\mathbf{h}=\mathbf{u}+i\mathbf{v}$, где $\mathbf{u},\mathbf{v}$ — действительные векторы:

$$A\mathbf{h}=\lambda\mathbf{h},\qquad\lambda=\alpha+i\beta.$$

([урок](https://mathprofi.ru/sobstvennye_znachenija_i_sobstvennye_vektory.html))

Комплексная экспонента:

$$e^{(\alpha+i\beta)t}=e^{\alpha t}(\cos\beta t+i\sin\beta t).$$

**Действительная ФСР** получается разделением комплексного решения на действительную и мнимую части (линейность системы с действительными коэффициентами это позволяет). ([урок](https://mathprofi.ru/kak_reshit_sistemu_differencialnyh_uravnenii.html))

## Теория подробно

1. Находим $\lambda=\alpha+i\beta$ и комплексный $\mathbf{h}=\mathbf{u}+i\mathbf{v}$ из $(A-\lambda E)\mathbf{h}=\mathbf{0}$.
2. Комплексное решение: $\mathbf{z}(t)=\mathbf{h}\,e^{\lambda t}=e^{\alpha t}(\cos\beta t+i\sin\beta t)(\mathbf{u}+i\mathbf{v}).$
3. Раскрываем: $\begin{aligned} \mathbf{z}&=e^{\alpha t}\bigl[ (\mathbf{u}\cos\beta t-\mathbf{v}\sin\beta t) +i(\mathbf{u}\sin\beta t+\mathbf{v}\cos\beta t) \bigr]. \end{aligned}$
4. Два действительных независимых решения: $\begin{aligned} \mathbf{x}_1(t)&=e^{\alpha t}(\mathbf{u}\cos\beta t-\mathbf{v}\sin\beta t), \\\\ \mathbf{x}_2(t)&=e^{\alpha t}(\mathbf{u}\sin\beta t+\mathbf{v}\cos\beta t). \end{aligned}$
5. Общее действительное решение: $\mathbf{x}=C_1\mathbf{x}_1+C_2\mathbf{x}_2.$ ([урок](https://mathprofi.ru/kak_reshit_sistemu_differencialnyh_uravnenii.html))

Сопряжённый корень $\alpha-i\beta$ отдельно не обрабатывают — он даёт те же $\mathbf{x}_1,\mathbf{x}_2$.

При кратном комплексном корне появляются множители $t^{j}$ (аналогично скалярному случаю).

## Как решать / алгоритм

1. $\det(A-\lambda E)=0$ → $\lambda=\alpha\pm i\beta$.
2. Решить $(A-(\alpha+i\beta)E)\mathbf{h}=0$; выделить $\mathbf{u}=\mathrm{Re}\,\mathbf{h}$, $\mathbf{v}=\mathrm{Im}\,\mathbf{h}$.
3. Записать $\mathbf{x}_1$, $\mathbf{x}_2$ по формулам выше.
4. Собрать общее решение; при Коши найти $C_1,C_2$.

Практический совет: систему для $\mathbf{h}$ можно решать в комплексных числах аккуратно построчно.

## Разобранный пример

$$A=\begin{pmatrix} 0 & -1 \\\\ 1 & 0 \end{pmatrix} \quad\bigl(x'=-y,\ y'=x\bigr).$$

$$\det\begin{pmatrix} -\lambda & -1 \\\\ 1 & -\lambda \end{pmatrix}=\lambda^{2}+1=0\Rightarrow\lambda=\pm i.$$

$\alpha=0$, $\beta=1$.

Для $\lambda=i$:

$$\begin{pmatrix} -i & -1 \\\\ 1 & -i \end{pmatrix}\begin{pmatrix} h_1 \\\\ h_2 \end{pmatrix}=0 \Rightarrow h_2=-i h_1.$$

Берём $h_1=1$, $h_2=-i$. Тогда 

$$\mathbf{h}=\begin{pmatrix}1 \\\\ 0\end{pmatrix}+i\begin{pmatrix}0 \\\\ -1\end{pmatrix}$$

, то есть

$$\mathbf{u}=\begin{pmatrix} 1 \\\\ 0 \end{pmatrix},\qquad\mathbf{v}=\begin{pmatrix} 0 \\\\ -1 \end{pmatrix}.$$

$$\begin{aligned} \mathbf{x}_1&=\mathbf{u}\cos t-\mathbf{v}\sin t=\begin{pmatrix} \cos t \\\\ \sin t \end{pmatrix}, \\\\ \mathbf{x}_2&=\mathbf{u}\sin t+\mathbf{v}\cos t=\begin{pmatrix} \sin t \\\\ -\cos t \end{pmatrix}. \end{aligned}$$

Общее решение:

$$\begin{cases} x=C_1\cos t+C_2\sin t, \\\\ y=C_1\sin t-C_2\cos t. \end{cases}$$

Траектории — окружности (центр в нуле).

**Ещё пример:** 

$$A=\begin{pmatrix}1 & -2 \\\\ 1 & -1\end{pmatrix}$$

.
Характеристическое: $\lambda^{2}+1=0$? Проверьте: 

$$\det\begin{pmatrix}1-\lambda&-2 \\\\ 1&-1-\lambda\end{pmatrix}=(1-\lambda)(-1-\lambda)+2=\lambda^{2}+1$$

. Да, $\lambda=\pm i$, $\alpha=0$, $\beta=1$. Далее — тот же алгоритм.

## Практика

1. Для 

$$A=\begin{pmatrix}0 & 1 \\\\ -1 & 0\end{pmatrix}$$

 найти общее решение.
2. Что меняется, если $\lambda=2\pm 3i$?
3. Почему достаточно одного комплексного вектора из пары $\alpha\pm i\beta$?
4. Свести систему $x'=-y$, $y'=x$ исключением к уравнению на $x$.

**Ответы:** 1) аналогично окружностям/эллипсам, $\lambda=\pm i$; 2) множитель $e^{2t}$ и частота $3$; 3) сопряжение даёт те же действительные/мнимые части; 4) $x''+x=0$.

## Что сказать устно за 1 минуту

При паре $\alpha\pm i\beta$ находим комплексный собственный вектор $\mathbf{u}+i\mathbf{v}$, берём комплексное решение $\mathbf{h}e^{(\alpha+i\beta)t}$ и выделяем действительную и мнимую части — получаем два действительных решения с множителем $e^{\alpha t}$ и комбинациями $\mathbf{u},\mathbf{v}$ с $\cos\beta t$ и $\sin\beta t$. Общее решение — их линейная комбинация.

## Источник

- [Системы дифференциальных уравнений (mathprofi)](https://mathprofi.ru/sistemy_differencialnyh_uravnenij.html)
- [Как решить систему ДУ (mathprofi)](https://mathprofi.ru/kak_reshit_sistemu_differencialnyh_uravnenii.html)
