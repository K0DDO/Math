# Практика по спецразделам — линейные операторы, квадратичные формы, ДУ и системы

> **Источники практики (разобранные примеры):**
> - [Линейные преобразования](https://mathprofi.ru/linejnye_preobrazovanija.html)
> - [Собственные числа и собственные векторы](https://mathprofi.ru/sobstvennye_znachenija_i_sobstvennye_vektory.html)
> - [Квадратичные формы. Критерий Сильвестра](https://mathprofi.ru/kvadratichnye_formy.html)
> - [Приведение квадратичной формы к каноническому виду. Метод Лагранжа](https://mathprofi.ru/kak_privesti_kf_k_kanonicheskomu_vidu.html)
> - [Ортогональное преобразование квадратичной формы](https://mathprofi.ru/metod_ortogonalnogo_preobrazovaniya_kf.html)
> - [Приведение уравнения линии 2 порядка к каноническому виду](https://mathprofi.ru/kak_privesti_uravnenie_linii_2_poryadka_k_kanonicheskomu_vidu.html)
> - [Свойства матричных операций. Блочные матрицы](https://mathprofi.ru/svoistva_operacij_nad_matricami_matrichnye_vyrazheniya.html)
> - [Ранг матрицы](https://mathprofi.ru/rang_matricy.html)
> - [Однородные системы](https://mathprofi.ru/odnorodnye_sistemy_lineinyh_uravnenij.html)
> - [ДУ с разделяющимися переменными](https://mathprofi.ru/differencialnye_uravnenija_primery_reshenii.html)
> - [Однородные ДУ 1 порядка](https://mathprofi.ru/odnorodnye_diffury_pervogo_poryadka.html)
> - [ДУ, сводящиеся к однородным](https://mathprofi.ru/du_svodjashiesja_k_odnorodnym.html)
> - [Линейные ДУ 1 порядка](https://mathprofi.ru/lineinye_differencialnye_uravnenija.html)
> - [ДУ в полных дифференциалах](https://mathprofi.ru/differencialnye_uravnenija_v_polnyh_differencialah.html)
> - [Уравнение Бернулли](https://mathprofi.ru/differencialnoe_uravnenie_bernulli.html)
> - [ДУ, допускающие понижение порядка](https://mathprofi.ru/differencialnye_uravnenija_dopuskajushie_ponizhenie_poryadka.html)
> - [Линейные однородные ДУ 2-го порядка](https://mathprofi.ru/differencialnye_uravnenija_vtorogo_poryadka.html)
> - [Неоднородные ДУ 2-го порядка](https://mathprofi.ru/kak_reshit_neodnorodnoe_uravnenie_vtorogo_poryadka.html)
> - [Линейные ДУ высших порядков](https://mathprofi.ru/linejnye_diffury_vysshih_porjadkov.html)
> - [Метод вариации произвольных постоянных](https://mathprofi.ru/metod_variacii_proizvolnyh_postoyannyh.html)
> - [Системы ДУ](https://mathprofi.ru/sistemy_differencialnyh_uravnenij.html)

---

## 1. Линейный оператор, матрица, ранг, ядро, дефект, сопряжённый — практика — [лекция](https://mathprofi.ru/linejnye_preobrazovanija.html)

**Пример 1.** Проверить линейность $A(x_1,x_2)=(x_1+2x_2, 3x_1-x_2)$. $A(ax+by)=aAx+bAy$ — выполняется.

**Пример 2.** Матрица оператора $A(x_1,x_2)=(2x_1+x_2, x_1-x_2)$ в базисе $e_1,e_2$: $Ae_1=(2,1)$ → 1-й столбец $(2,1)^T$, $Ae_2=(1,-1)$ → 2-й столбец → 

$$\begin{pmatrix}2 & 1 \\\\ 1 & -1\end{pmatrix}$$

.

**Пример 3.** 

$$A=\begin{pmatrix}1 & 2 \\\\ 2 & 4\end{pmatrix}$$

: $\ker A$ — решение $x+2y=0$ → базис $(-2,1)$, $def=1$, $rang=1$, $rang+def=2$.

**Пример 4.** В $\mathbb R^2$ со скалярным $(x,y)=x_1y_1+x_2y_2$, 

$$A=\begin{pmatrix}1 & 2 \\\\ 0 & 1\end{pmatrix}$$

 → 

$$A^*=A^T=\begin{pmatrix}1 & 0 \\\\ 2 & 1\end{pmatrix}$$

; $A$ не самосопряжён. 

$$B=\begin{pmatrix}2 & -1 \\\\ -1 & 3\end{pmatrix}$$

 — симметрична → самосопряжён.

## 2. Изменение матрицы при переходе — практика — [лекция](https://mathprofi.ru/linejnye_preobrazovanija.html)

**Пример.** 

$$A_e=\begin{pmatrix}0 & -1 \\\\ 1 & 0\end{pmatrix}$$

 (поворот $90°$), новый базис $e'_1=(1,1), e'_2=(1,-1)$ → 

$$C=\begin{pmatrix}1 & 1 \\\\ 1 & -1\end{pmatrix}$$

, 

$$C^{-1}=\frac{1}{2}\begin{pmatrix}1 & 1 \\\\ 1 & -1\end{pmatrix}$$

, 

$$A_{e'}=C^{-1}AC =\begin{pmatrix}0 & 1 \\\\ -1 & 0\end{pmatrix}$$

.

**Пример.** Диагонализация поворота не над $\mathbb R$.

## 3. Собственные числа/векторы, характеристический многочлен — практика — [лекция](https://mathprofi.ru/sobstvennye_znachenija_i_sobstvennye_vektory.html)

**Пример 1.** 

$$A=\begin{pmatrix}2 & 1 \\\\ 1 & 2\end{pmatrix}$$

: 

$$p(λ)=\det\begin{pmatrix}2-λ & 1 \\\\ 1 & 2-λ\end{pmatrix}=(2-λ)^2-1=λ^2-4λ+3=0$$

 → $λ_1=1$, $λ_2=3$. Для $λ_1=1$: $(A-E)X=0$ → $x+y=0$ → $h_1=(1,-1)$; $λ_2=3$: $h_2=(1,1)$. $tr=4=1+3$, $det=3=1·3$.

**Пример 2.** 

$$A=\begin{pmatrix}0 & 1 \\\\ -1 & 0\end{pmatrix}$$

 → $p=λ^2+1=0$ → $λ=±i$ (комплексные).

**Пример 3.** 

$$A=\begin{pmatrix}2 & 1 & 0 \\\\ 0 & 2 & 0 \\\\ 0 & 0 & 3\end{pmatrix}$$

 → $λ=2$ кратн.2, $λ=3$.

## 4. Собственный базис, диагональная матрица — практика — [лекция](https://mathprofi.ru/sobstvennye_znachenija_i_sobstvennye_vektory.html)

**Пример.** Для предыдущего 

$$A=\begin{pmatrix}2 & 1 \\\\ 1 & 2\end{pmatrix}$$

, 

$$C=(h_1|h_2)=\begin{pmatrix}1 & 1 \\\\ -1 & 1\end{pmatrix}$$

, $C^{-1}AC=\mathrm{diag}(1,3)$. В базисе $f_1,f_2$ оператор действует как $Af_1=1·f_1$, $Af_2=3·f_2$.

**Пример.** 

$$A=\begin{pmatrix}1 & 1 \\\\ 0 & 1\end{pmatrix}$$

 — только один собственный вектор $(1,0)$ → собственного базиса нет (дефект).

## 5. Билинейные/квадратичные, матрица, диагонализация собственными — практика — [лекция](https://mathprofi.ru/kvadratichnye_formy.html)

**Пример 1.** $Q=2x_1^2+4x_1x_2+5x_2^2$: 

$$A=\begin{pmatrix}2 & 2 \\\\ 2 & 5\end{pmatrix}$$

, $Q=X^TAX$.

**Пример 2.** Восстановить по матрице 

$$A=\begin{pmatrix}1 & -1 \\\\ -1 & 2\end{pmatrix}$$

: $Q=x_1^2-2x_1x_2+2x_2^2$.

**Пример 3 (ортогональная диагонализация).** 

$$A=\begin{pmatrix}2 & 1 \\\\ 1 & 2\end{pmatrix}$$

, $λ_1=1$, $λ_2=3$, нормированные $u_1=\frac1{\sqrt2}(1,-1)$, $u_2=\frac1{\sqrt2}(1,1)$ → 

$$U=\frac1{\sqrt2}\begin{pmatrix}1 & 1 \\\\ -1 & 1\end{pmatrix}$$

, $U^T A U=\mathrm{diag}(1,3)$, замена $X=UY$ → $Q=y_1^2+3y_2^2$.

## 6. Лагранж и Якоби — практика — [лекция](https://mathprofi.ru/kak_privesti_kf_k_kanonicheskomu_vidu.html)

**Лагранж Пример 1.** $Q=x_1^2+2x_1x_2+2x_2^2$ → $(x_1+x_2)^2+x_2^2$ → замена $y_1=x_1+x_2$, $y_2=x_2$ → $Q=y_1^2+y_2^2$.

**Лагранж Пример 2.** $Q=x_1x_2$ (нет квадратов): $x_1=y_1+y_2$, $x_2=y_1-y_2$ → $Q=y_1^2-y_2^2$.

**Якоби Пример.** 

$$A=\begin{pmatrix}2 & 1 & 0 \\\\ 1 & 2 & 1 \\\\ 0 & 1 & 2\end{pmatrix}$$

, $\Delta_1=2$, $\Delta_2=3$, $\Delta_3=4$ → $Q=2y_1^2+\frac{3}{2} y_2^2+\frac{4}{3} y_3^2$. Если все $\Delta_k≠0$ — быстро.

## 7. Сильвестр — практика — [лекция](https://mathprofi.ru/kvadratichnye_formy.html)

**Пример 1.** 

$$A=\begin{pmatrix}2 & -1 \\\\ -1 & 2\end{pmatrix}$$

: $\Delta_1=2>0$, $\Delta_2=3>0$ → положительно определена, $Q>0$.

**Пример 2.** 

$$A=\begin{pmatrix}-1 & 1 \\\\ 1 & -2\end{pmatrix}$$

: $\Delta_1=-1<0$, $\Delta_2=1>0$ → отрицательно определена.

**Пример 3.** 

$$A=\begin{pmatrix}1 & 2 \\\\ 2 & 1\end{pmatrix}$$

: $\Delta_1=1>0$, $\Delta_2=-3<0$ → неопределённая (седло).

**Пример 4.** 

$$A=\begin{pmatrix}1 & 1 \\\\ 1 & 1\end{pmatrix}$$

: $\Delta_1=1>0$, $\Delta_2=0$ → полуопределённая, Сильвестр не решает окончательно → приводим к канону $Q=(x_1+x_2)^2≥0$.

## 8. Приведение кривых/поверхностей 2 порядка — практика — [лекция](https://mathprofi.ru/kak_privesti_uravnenie_linii_2_poryadka_k_kanonicheskomu_vidu.html)

**Пример кривой.** $2x^2+4xy+5y^2-4x-4y-1=0$: 

$$A=\begin{pmatrix}2 & 2 \\\\ 2 & 5\end{pmatrix}$$

, $λ=1,6$, $U$ как выше → после поворота $y_1^2+6y_2^2+ b'_1y_1+...=0$ → выделяем квадраты → эллипс центр $(...)$ полуоси $a=\sqrt{...}$.

**Пример.** $x^2+ y^2 +2xy =1$ → $A$ имеет $λ_1=0$, $λ_2=2$ → парабола/пара прямых — вырожденный.

**Поверхность.** $x^2+y^2+z^2+4xy=1$ → 

$$A=\begin{pmatrix}1 & 2 & 0 \\\\ 2 & 1 & 0 \\\\ 0 & 0 & 1\end{pmatrix}$$

, $λ=-1,3,1$ → гиперболоид.

## 9. Блочные матрицы — практика — [лекция](https://mathprofi.ru/svoistva_operacij_nad_matricami_matrichnye_vyrazheniya.html)

**Пример сложения.** 

$$\begin{pmatrix}A & B \\\\ 0 & D\end{pmatrix}+\begin{pmatrix}A' & B' \\\\ 0 & D'\end{pmatrix}=\begin{pmatrix}A+A' & B+B' \\\\ 0 & D+D'\end{pmatrix}$$

.

**Умножение.** 

$$M=\begin{pmatrix}I & A \\\\ 0 & I\end{pmatrix}$$

, 

$$N=\begin{pmatrix}I & B \\\\ 0 & I\end{pmatrix}$$

 → 

$$MN=\begin{pmatrix}I & A+B \\\\ 0 & I\end{pmatrix}$$

.

**Определитель Шура.** 

$$M=\begin{pmatrix}2 & 1 & | & 0 \\\\ 1 & 2 & | & 1 \\\\ \hline0 & 1 & | & 3\end{pmatrix}$$

 → $\det M =\det A·\det(D-CA^{-1}B)$.

**Обратная блочная.** 

$$\begin{pmatrix}I & X \\\\ 0 & I\end{pmatrix}^{-1}=\begin{pmatrix}I & -X \\\\ 0 & I\end{pmatrix}$$

.

## 10. Построение собственного базиса — практика — [лекция](https://mathprofi.ru/sobstvennye_znachenija_i_sobstvennye_vektory.html)

**Пример.** 

$$A=\begin{pmatrix}1 & 2 & 0 \\\\ 0 & 3 & 0 \\\\ 0 & 0 & 2\end{pmatrix}$$

: $p=(1-λ)(3-λ)(2-λ)=0$ → $λ=1,2,3$ три различных → три вектора $(1,0,0)$, $(0,0,1)$, $(2,1,0)$? решаем $(A-3E)X=0$ → $h_3=(1,1,0)$ — базис.

**Пример с кратностью.** 

$$A=\begin{pmatrix}3 & 0 & 0 \\\\ 0 & 2 & 1 \\\\ 0 & 0 & 2\end{pmatrix}$$

: $λ=2$ кратн.2, ранг $(A-2E)=1$ → дефект 2 → два вектора $(0,1,0),(0,0,1)$? фактически $h_1=(1,0,0)$ для $3$, $h_2=(0,1,0)$, $h_3=(0,0,1)$ — базис есть; если Жорданова клетка 

$$\begin{pmatrix}2 & 1 \\\\ 0 & 2\end{pmatrix}$$

 — только один вектор → базиса нет.

---

## 11. ДУ: порядок, общее/частное/особое — практика — [лекция](https://mathprofi.ru/differencialnye_uravnenija_primery_reshenii.html)

**Пример 1.** $y'=x^2$ → общее $y=x^3/3+C$, частное через $(0,1)$: $C=1$ → $y=x^3/3+1$.

**Пример 2.** $y'=y^2$ → общее $ -1/y = x+C$ → $y=-1/(x+C)$, особое $y=0$ (теряется при делении на $y^2$).

**Пример 3.** Уравнение Клеро $y=xy'+y'^2$ → общее $y=Cx+C^2$ (прямые), особое $y=-x^2/4$ (огибающая, касание).

## 12. Интегральные кривые, изоклины — практика — [лекция](https://mathprofi.ru/differencialnye_uravnenija_primery_reshenii.html)

**Пример.** $y'=x$: изоклины $x=k$ — вертикальные прямые; поле — горизонтально при $k=0$; интегральные $y=x^2/2+C$ — параболы.

**Пример.** $y'=y$: изоклины $y=k$ — горизонтальные; кривые $y=Ce^x$.

**Построение:** для $y'=x+y$ изоклина $x+y=k$ → $y=k-x$ — семейство параллельных прямых.

## 13. 1 порядок, Коши, разделяющиеся, однородные — практика — [лекция](https://mathprofi.ru/differencialnye_uravnenija_primery_reshenii.html)

**Разделяющиеся.** $(1+x^2)dy -2x y dx=0$ → $dy/y=2xdx/(1+x^2)$ → $\ln|y|=\ln(1+x^2)+C$ → $y=C(1+x^2)$.

**Задача Коши.** $y'=y/x$, $y(1)=2$ → $y=Cx$, $C=2$ → $y=2x$.

**Однородное.** $(x^2+y^2)dx-2xy dy=0$ → $u=y/x$ → $du/(...)$ → $\ln|x|=...$ → $y^2 = x^2(Cx-1)$? Решение: $x^2+y^2=Cx$? проверим: однородное → ответ $y^2 = Cx^2 - x^2$? На сайте пример даёт $y= Cx+...$.

**Неединственность.** $y'=2\sqrt{y}$, $y(0)=0$ → решения $y=0$ и $y=x^2$ — $f_y=1/\sqrt{y}$ разрывна.

## 14. Линейные 1 порядка — практика — [лекция](https://mathprofi.ru/lineinye_differencialnye_uravnenija.html)

**Пример Бернулли-методом.** $y'+y = e^x$: $y=uv$, $v'+v=0$ → $v=e^{-x}$, $u'v=e^x$ → $u'=e^{2x}$ → $u=e^{2x}/2+C$ → $y= e^x/2+Ce^{-x}$.

**Пример вариация.** $y'+2xy = x e^{-x^2}$: однородное $y=Ce^{-x^2}$, $C'(x)e^{-x^2}=x e^{-x^2}$ → $C=x^2/2+C$ → $y=(x^2/2+C)e^{-x^2}$.

**Задача Коши.** $y'+y/x = x$, $y(1)=0$ → $y= x^2/3 -1/(3x)$.

## 15. Полные дифференциалы и Бернулли — практика — [лекция](https://mathprofi.ru/differencialnye_uravnenija_v_polnyh_differencialah.html)

**Полный.** $(2xy+x^2)dx+(x^2+y)dy=0$: $P_y=2x=Q_x$ → $U=\int Pdx = x^2 y + x^3/3+ φ(y)$, $U_y=x^2+φ'=Q=x^2+y$ → $φ=y^2/2$ → общий интеграл $x^2 y + x^3/3 + y^2/2=C$.

**Неполный множитель.** $(y)dx+...$ — ищут $μ(x)$.

**Бернулли.** $y'+y = x y^2$ ($n=2$): делим $y^{-2}$, $z= y^{-1}$, $z' -z = -x$ → линейное → $z=Ce^{x}+x+1$ → $y=1/(Ce^{x}+x+1)$.

**Бернулли 2.** $y'+2y = y^2 e^x$ → $z=1/y$ → $z'-2z=-e^x$.

## 16. Особое решение, огибающая — практика — [лекция](https://mathprofi.ru/differencialnye_uravnenija_v_polnyh_differencialah.html)

**Пример.** Семейство $y=Cx+C^2$ → $Φ=y-Cx-C^2=0$, $Φ_C=-x-2C=0$ → $C=-x/2$ → огибающая $y=-x^2/4$ — особое решение ДУ $y=xy'+y'^2$.

**Пример.** $y= C(x-C)^2$ (?) огибающая — дискриминанта.

**Проверка:** подставить огибающую в ДУ — тождество, но не получается из общего при $C$.

## 17. Высшие порядки, Коши, понижение — практика — [лекция](https://mathprofi.ru/differencialnye_uravnenija_dopuskajushie_ponizhenie_poryadka.html)

**Тип 1:** $y''=x$ → $y'=x^2/2+C_1$, $y=x^3/6+C_1x+C_2$.

**Тип 2 (нет y):** $y''=y'$? $F(x,y',y'')=0$ → $z=y'$ → $z'=z$ → $z=C_1 e^x$ → $y=C_1 e^x +C_2$.

**Тип 3 (нет x):** $y''= y'·y$? $y''=2yy'$? Пусть $y''=y$? $F(y,y',y'')=0$ → $p=y'$, $y''=p dp/dy$ → $p dp/dy = ...$ → интегрируют.

**Задача Коши 2 порядка (механика):** $y''=-y$, $y(0)=0$, $y'(0)=1$ → $y=\sin x$ — гармонические колебания.

## 18. Линейный оператор, свойства частных решений — практика — [лекция](https://mathprofi.ru/differencialnye_uravnenija_vtorogo_poryadka.html)

**Пример.** $L[y]=y''+y$: $L[\sin x]=0$, $L[\cos x]=0$ → $L[2\sin+3\cos]=0$.

**Пример неоднородного:** $y''+y=x$, $y_1=x$ частное, то $y_1+ C_1\cos+C_2\sin$ — общее.

## 19. Вронский, независимость — практика — [лекция](https://mathprofi.ru/differencialnye_uravnenija_vtorogo_poryadka.html)

**Пример 1.** $y_1=e^x$, $y_2=e^{2x}$: 

$$W=\begin{vmatrix}e^x&e^{2x} \\\\ e^x&2e^{2x}\end{vmatrix}=e^{3x}≠0$$

 → независимы.

**Пример 2.** $y_1=x$, $y_2= x^2$ для $y''-2y'/x+...$? $W= x^2≠0$ → независимы.

**Пример зависимых.** $y_1=\sin x$, $y_2=2\sin x$ → $W=0$.

**Формула Лиувилля:** для $y''+ y=0$, $W=C$.

## 20. ФСР и структура общего ЛОДУ — практика — [лекция](https://mathprofi.ru/differencialnye_uravnenija_vtorogo_poryadka.html)

**Пример 2 порядка.** $y''-3y'+2y=0$: ФСР $e^x$, $e^{2x}$ → $y=C_1e^x+C_2e^{2x}$.

**Пример 3 порядка.** $y'''-y''=0$: $k^3-k^2=0$ → $k=0$ (кратн.2), $1$ → ФСР $1,x,e^x$ → $y=C_1+C_2x+C_3 e^x$.

## 21. Переменные коэффициенты — практика — [лекция](https://mathprofi.ru/linejnye_diffury_vysshih_porjadkov.html)

**Эйлер.** $x^2 y''+ x y' - y=0$ → $x=e^t$, $D=y'_t$: $D(D-1)y+ Dy -y=0$ → $D^2 y -y=0$ → $y=C_1 e^t +C_2 e^{-t}=C_1 x +C_2/x$.

**Известно $y_1$.** $y''+ y =0$ уже постоянные; для $x^2 y''-2y=0$, $y_1=x^2$ → $y_2= y_1\int e^{-\int P} /y_1^2 dx = ...=1/x$.

## 22. Неоднородные высшие, вариация — практика — [лекция](https://mathprofi.ru/kak_reshit_neodnorodnoe_uravnenie_vtorogo_poryadka.html)

**Структура.** $y''+y = x$ → $y_{о.о.}=C_1\cos+C_2\sin$, $y_{ч}=x$ → общее $C_1\cos+C_2\sin +x$.

**Вариация 2 порядка.** $y''+y=1/\cos x$: ФСР $\cos,\sin$, $W=1$, $C_1'=-\sin/\cos$, $C_2'=1$ → $C_1=\ln|\cos x|$, $C_2=x$ → $y_{ч}=\cos x·\ln|\cos|+ x\sin x$.

**Вариация 3 порядка** аналогично система 3×3.

## 23. Постоянные коэффициенты однородные — практика — [лекция](https://mathprofi.ru/differencialnye_uravnenija_vtorogo_poryadka.html)

**Пример 1.** $y''-5y'+6y=0$: $k^2-5k+6=0$ → $k=2,3$ → $y=C_1e^{2x}+C_2e^{3x}$.

**Пример 2.** $y''+2y'+y=0$: $(k+1)^2=0$ → $y=(C_1+C_2x)e^{-x}$.

**Пример 3.** $y''+4y=0$: $k=±2i$ → $y=C_1\cos2x+C_2\sin2x$.

**Пример 4.** $y^{(4)}+2y''+y=0$: $(k^2+1)^2=0$ → $k=±i$ кратн.2 → $y=(C_1+C_2x)\cos x+(C_3+C_4x)\sin x$.

## 24. Неоднородные + спец. правая часть — практика — [лекция](https://mathprofi.ru/kak_reshit_neodnorodnoe_uravnenie_vtorogo_poryadka.html)

**Пример 1.** $y''-2y'+y = e^x$ ($p=1$ кратн.2): $y_{ч}=A x^2 e^x$ → подставляем $A=1/2$ → $y_{ч}= x^2 e^x/2$.

**Пример 2.** $y''+y = \cos x$ ($γ=i$ простой): $y_{ч}= x(A\cos x +B\sin x)$? $γ=i$ — корень → $s=1$ → $y_{ч}=x(A\cos x +B\sin x)$ → $A=0, B=1/2$ → $y_{ч}= x\sin x/2$.

**Пример 3.** $y''- y = 2x$ → $y_{ч}=Ax+B$ → $A=-2, B=0$ → $y_{ч}=-2x$.

**Пример сумма:** $y''+y = e^x+\cos x$ → сумма двух подборов.

## 25. Системы в нормальной форме — практика — [лекция](https://mathprofi.ru/sistemy_differencialnyh_uravnenij.html)

**Пример.** 

$$\begin{cases}x'=y \\\\ y'=-x\end{cases}$$

 → $x''=y'=-x$ → $x''+x=0$ → $x=C_1\cos t+C_2\sin t$, $y=x'= -C_1\sin t+C_2\cos t$.

**Обратно.** $y'''=y''+x$ → $x_1=y$, $x_2=y'$, $x_3=y''$ → система.

**Задача Коши.** $x(0)=1$, $y(0)=0$ → $C_1=1, C_2=0$ → $x=\cos t$, $y=-\sin t$.

## 26. Линейные однородные системы, простые корни — практика — [лекция](https://mathprofi.ru/sistemy_differencialnyh_uravnenij.html)

**Пример.** 

$$\begin{pmatrix}x' \\\\ y'\end{pmatrix}=\begin{pmatrix}1 & 2 \\\\ 2 & 1\end{pmatrix}\begin{pmatrix}x \\\\ y\end{pmatrix}$$

: $p(λ)=(1-λ)^2-4=0$ → $λ_1=3$, $h_1=(1,1)$ → $\mathbf{x}_1=(1,1)e^{3t}$, $λ_2=-1$, $h_2=(1,-1)$ → $\mathbf{x}_2=(1,-1)e^{-t}$ → общее $C_1(1,1)e^{3t}+C_2(1,-1)e^{-t}$.

## 27. Кратные действительные — практика — [лекция](https://mathprofi.ru/sistemy_differencialnyh_uravnenij.html)

**Пример 1 (диагонализируемая).** $A=3I$ → любой вектор собственный → $\mathbf{x}=e^{3t}C$.

**Пример 2 (дефектная).** 

$$A=\begin{pmatrix}2 & -1 \\\\ 1 & 0\end{pmatrix}$$

: $λ=1$ кратн.2, $h=(1,1)$, $(A-I)g=h$ → $g=(1,0)$ → $\mathbf{x}_1= h e^{t}$, $\mathbf{x}_2=(ht+g)e^{t}$ → $x=(C_1+C_2 t +C_2)e^{t}$, $y=(C_1+C_2 t)e^{t}$.

## 28. Комплексные — практика — [лекция](https://mathprofi.ru/sistemy_differencialnyh_uravnenij.html)

**Пример.** 

$$A=\begin{pmatrix}0 & -1 \\\\ 1 & 0\end{pmatrix}$$

: $λ=±i$, $h=(1,-i)= (1,0)+i(0,-1)$ → $u=(1,0)$, $v=(0,-1)$ → $\mathbf{x}_1=e^{0}(u\cos t -v\sin t)=(\cos t, -\sin t?)$ → решение $x=C_1\cos t+C_2\sin t$, $y=C_1\sin t -C_2\cos t$ — окружность.

**Пример.** 

$$A=\begin{pmatrix}1 & -2 \\\\ 2 & 1\end{pmatrix}$$

: $λ=1±2i$ → $x=e^{t}(C_1\cos2t+C_2\sin2t)$.

## 29. Неоднородные системы, вариация — практика — [лекция](https://mathprofi.ru/sistemy_differencialnyh_uravnenij.html)

**Пример.** 

$$\mathbf{x}'=\begin{pmatrix}1 & 0 \\\\ 0 & 2\end{pmatrix}\mathbf{x}+\begin{pmatrix}e^t \\\\ t\end{pmatrix}$$

: $Φ=\mathrm{diag}(e^{t},e^{2t})$, $Φ^{-1}g=(1, t e^{-2t})$ → $C_1=t$, $C_2=\int t e^{-2t}dt$ → частное $ΦC(t)$.

**Пример 2×2.** $x'=x+y+ t$, $y'=x+y+1$ — $Φ$ из однородной → $C'=Φ^{-1}g$.

## 30. Неоднородные, спец. правая часть — практика — [лекция](https://mathprofi.ru/sistemy_differencialnyh_uravnenij.html)

**Пример.** 

$$\mathbf{x}'=\begin{pmatrix}0 & 1 \\\\ -1 & 0\end{pmatrix}\mathbf{x}+\begin{pmatrix}0 \\\\ \cos t\end{pmatrix}$$

: $γ=i$ собственный → $s=1$ → ищем $\mathbf{x}_p = t(a\cos t+b\sin t)$.

**Пример.** $\mathbf{x}'=A\mathbf{x}+ \mathbf{p} e^{2t}$, $2$ не собственное → $\mathbf{x}_p = \mathbf{q} e^{2t}$, $(2I-A)q=p$ → решают.

**Суперпозиция:** если $g=g_1+g_2$ → сумма частных.