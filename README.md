# Введение

Задача о ранце (или задача о рюкзаке) — NP-полная задача комбинаторной оптимизации. Своё название получила от конечной цели: уложить как можно большее число ценных вещей в рюкзак при условии, что вместимость рюкзака ограничена. С различными вариациями задачи о ранце можно столкнуться в экономике, прикладной математике, криптографии и логистике.
В общем виде задачу можно сформулировать так: из заданного множества предметов со свойствами «стоимость» и «вес» требуется отобрать подмножество с максимальной полной стоимостью, соблюдая при этом ограничение на суммарный вес.

# Теоретическая часть
### Ограниченный рюкзак (англ. Bounded Knapsack Problem) — обобщение классической задачи, когда любой предмет может быть взят некоторое количество раз.
## Формулировка задачи
Каждый предмет может быть выбран ограниченное *b<sub>i</sub>>* число раз. Задача выбрать число *x<sub>i</sub>>* предметов каждого типа так, чтобы
 - максимизировать общую стоимость: <img src="https://latex.codecogs.com/svg.latex?\sum_{i=1}^{N}p_{i}x_{i};" title="\sum_{i=1}^{N}p_{i}x_{i};" />
 - выполнялось условие совместности: <img src="https://latex.codecogs.com/svg.latex?\sum_{i=1}^{N}w_{i}x_{i}\leqW;" title="\sum_{i=1}^{N}w_{i}x_{i}\leqW;" />

## Варианты решения	
- Метод ветвей и границ.
- Метод динамического программирования.

## Выбор метода решения
Пусть *d(i,c)* максимальная стоимость любого количества вещей типов от 1 до *i* , суммарным весом до *c* включительно.
Заполним *d(0,c)* нулями.
Тогда меняя i от 1 до *N* , рассчитаем на каждом шаге *d(i,c)* , для *c* от 1 до *W* , по рекуррентной формуле:

<img src="https://latex.codecogs.com/svg.latex?d(i,&space;c)=max(d(i-1,c-lw_{i})&plus;lp_{i})" title="d(i, c)=max(d(i-1,c-lw_{i})+lp_{i})" />  по всем целым *l* из промежутка <img src="https://latex.codecogs.com/svg.latex?0\leq&space;l\leq&space;min(b_{i},\left&space;\lfloor&space;c/w_{i}&space;\right&space;\rfloor)" title="0\leq l\leq min(b_{i},\left \lfloor c/w_{i} \right \rfloor)" />

После выполнения в *d(N,W)* будет лежать максимальная стоимость предметов, помещающихся в рюкзак.

Сложность алгоритма *O(NW^2^)*.

n^2^

### Неограниченный рюкзак (англ.Unbounded Knapsack Problem) — обобщение ограниченного рюкзака, в котором любой предмет может быть выбран любое количество раз.
## Формулировка задачи
Каждый предмет может быть выбран любое число раз. Задача выбрать количество *x<sub>i</sub>>* предметов каждого типа так, чтобы
- максимизировать общую стоимость: <img src="https://latex.codecogs.com/svg.latex?\sum_{i=1}^{N}x_{i}p_{i};" title="\sum_{i=1}^{N}x_{i}p_{i};" />
- выполнялось условие совместности: <img src="https://latex.codecogs.com/svg.latex?\sum_{i=1}^{N}w_{i}x_{i}\leq&space;W;" title="\sum_{i=1}^{N}w_{i}x_{i}\leq W;" />
где *x<sub>i</sub>>* <img src="https://latex.codecogs.com/svg.latex?\geq&space;0" title="\geq 0" /> целое, для всех *i=1,2,…,N* . 
<!-- Дано *N* предметов, *W* — вместимость рюкзака, *w={*w<sub>1</sub>*,w<sub>2</sub>,…,w<sub>N</sub>}*  — соответствующий ему набор положительных целых весов,*p={p<sub>1</sub>,p<sub>2</sub>,…,p<sub>N</sub>}* — соответствующий ему набор положительных целых стоимостей. Нужно найти набор бинарных величин  *B={b1,b2,…,bN}*, где  *b<sub>i</sub>=1*, если предмет *n<sub>i</sub>* включен в набор, *b<sub>i</sub>=0*, если предмет *n<sub>i</sub>* не  включен, и такой что:
 - *b<sub>1</sub>w<sub>1</sub>+…+b<sub>N</sub>w<sub>N</sub> <= W*
 - *b<sub>1</sub>p<sub>1</sub>+…+b<sub>N</sub>p<sub>N</sub>* максимальна. -->
  

## Варианты решения	
Самые распространенные методы точного решения это:
- Метод ветвей и границ.
- Метод динамического программирования.

## Выбор метода решения 
Для данной задачи наиболее оптимальным по памяти является метод динамического программирования.
Пусть *d(i,c)* максимальная стоимость любого количества вещей типов от 1 до *i* , суммарным весом до *c* включительно.
Заполним *d(0,c)* нулями.
Тогда меняя i от 1 до *N* , рассчитаем на каждом шаге *d(i,c)* , для *c* от 0 до *W* , по рекуррентной формуле:

<img src="https://latex.codecogs.com/svg.latex?d(i,c)\left\{\begin{matrix}&space;d(i-1,c)&space;\;&space;for&space;\;&space;c=0,...,w_{i}-1&space;\\&space;max(d(i-1,c),d(i,&space;c-w_{i})&plus;p_{i})&space;\;&space;for\;&space;c=w_{i},...,W;&space;\end{matrix}\right." title="d(i,c)\left\{\begin{matrix} d(i-1,c) \; for \; c=0,...,w_{i}-1 \\ max(d(i-1,c),d(i, c-w_{i})+p_{i}) \; for\; c=w_{i},...,W; \end{matrix}\right." />

После выполнения в *d(N,W)* будет лежать максимальная стоимость предметов, помещающихся в рюкзак.

Сложность алгоритма *O(NW)*.


# Форматы входных и выходных данных

#### Программа принимает входные данные в виде двух текстовых файлов. 
 - Первый из файлов содержит в себе меню вида:
 ```
 #number (price calories)
 ```
 - Второй файл служит для хранения списка доступных акций 
  **type** - тип акции 
  **positions** - список продуктов, чтобы акцию получить (строка, где перечислены номера товаров через запятую)
  **discount** - бесплатный продукт или фиксированная цена (зависит от типа акции)

 ```
type products discount
 ```


#### На выходе программа выдает список товаров, которые нужно купить

# План решения
- Написать алгоритм для решения задачи о дп.
- Разобраться с тем как все это дело лучше хранить
- Прикрутить к алгоритму акции
- Подумать над тем как решить первую задачу через вторую
- Покрыть все тестами

