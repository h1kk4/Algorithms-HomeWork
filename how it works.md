Примеры запуска программы с параметрами

```bash
python3 algo.py menu.txt promo.txt b 20 
python3 algo.py menu.txt promo.txt a 1,2,4
```

В зависимости от выбранного алгоритма (a, b) нужно указать параметры (список продуктов, сумму) соответственно. 

## Функции 

```python
menuParser(path, grocery_list={})
```
Если grocery_list не пуст то в menu, будет записывано кол-во продуктов, которые есть это нужно для решение задачи об ограниченном рюкзаке(первый алгоритм).

```python
make_additional_menu(menu, promo)
``` 
В зависимости от вида акции составляет новый элемент, который будет добавлен в menu. 
## Алгоритм A/Первый алгоритм:

Задача об ограниченном рюкзаке

```python
first_algo(menu, promo, grocery_list)
```

В функцию передаются меню, акции и список продуктов которые нужно купить.

```python
for i in grocery_list:
        money += menu[i].price * menu[i].count
        needed_calories += menu[i].calories * menu[i].count
```
С помощью цикла:
- Узнаем сколько максимально может стоить список продуктов без акций(худший вариант).
- Узнаем сколько калорий он дает. (Потребуется для поиска ответа).


Далее, используя функцию ```make_additional_menu(menu, promo)```  акции "добавляются в меню", то есть акции становятся продуктом со своей стоимостью и калорийностью. 

```python
for i in range(1, N + 1):
        for k in range(money + 1):
            tab[i][k] = tab[i - 1][k]
            for l in reversed(range(1, min(menu[i].count, k // menu[i].price) + 1)): #Ищем l для которого выполняется максимум
                tab[i][k] = max(tab[i][k], tab[i - 1][k - l * menu[i].price] + menu[i].calories * l) #Выбираем класть его или нет
```

После выполнения в tab(N, money) будет лежать максимальная стоимость предметов, помещающихся в рюкзак.

```python
def find_ans_1(i, k, tab, menu, needed_calories):
    if tab[i][k] == 0:
        return

    if tab[i][k - 1] >= needed_calories: #проверка, так как нам нужна минимальная стоимость мы сравниваем можно ли получить нужные продукты дешевле
        find_ans_1(i, k - 1, tab, menu, needed_calories)

    elif tab[i][k] == tab[i - 1][k]:
        find_ans_1(i - 1, k, tab, menu, needed_calories)
    else:
        find_ans_1(i, k - menu[i].price, tab, menu, needed_calories)
        answer.append(menu[i].name)
```
Найдем наборм предметов, входящих в рюкзак. 

## Алгоритм Б/Второй алгоритм:

Задача о неограниченном рюкзаке.

```python
second_algo(menu, promo, money)
```
В функцию передаются меню, акции и сумма на которую нужно купить продуктов.

Далее, используя функцию ```make_additional_menu(menu, promo)```  акции "добавляются в меню", то есть акции становятся продуктом со своей стоимостью и калорийностью.

```python
for i in range(1, N + 1):
        for k in range(1, money + 1):
            if k >= menu[i].price: #Если текущий предмет вмещается в рюкзак
                tab[i][k] = max(tab[i - 1][k], tab[i][k - menu[i].price] + menu[i].calories) #Выбираем класть его или нет
            else:
                tab[i][k] = tab[i - 1][k]
```

Находим набор предметов, входящих в рюкзак.


