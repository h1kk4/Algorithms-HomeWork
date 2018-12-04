import sys
from menu import Menu
from parser import *
import collections
import pdb


def start(argv):
    file_menu = argv[0]
    file_promo = argv[1]
    flag_ = argv[2]
    param = argv[3]
    if (flag_ == 'a' or flag_=='A'):

        grocery_list = collections.Counter(list(map(int, param.split(','))))
        menu = menuParser(file_menu, grocery_list)
        promo = promoParser(file_promo)

        first_algo(menu, promo, grocery_list)

    elif (flag_ == 'b' or flag_=='B'):

        menu = menuParser(file_menu)
        promo = promoParser(file_promo)

        second_algo(menu, promo, int(param))
    else:
        print("Chose one of existing algorithm a or b")


def first_algo(menu, promo, grocery_list):
    money = 0
    needed_calories = 0

    for i in grocery_list:
        money += menu[i].price * menu[i].count
        needed_calories += menu[i].calories * menu[i].count

    print(money, needed_calories)
    make_additional_menu(menu, promo)

    for keys in menu:
        menu[keys].getInfo()

    N = len(menu)

    tab = [[0] * (money + 1) for i in range(N + 1)]

    for i in range(money + 1):
        tab[0][i] = 0

    for i in range(1, N + 1):
        tab[i][0] = 0  # fill first column with 0

    for i in range(1, N + 1):
        for k in range(money + 1):
            tab[i][k] = tab[i - 1][k]
            for l in reversed(range(1, min(menu[i].count, k // menu[i].price) + 1)): #TODO zero price case
                tab[i][k] = max(tab[i][k], tab[i - 1][k - l * menu[i].price] + menu[i].calories * l)

    cur_weight = 0
    for l in tab:
        print(cur_weight, '\t', l)
        cur_weight += 1

    find_ans_1(N, money, tab, menu, needed_calories)


def second_algo(menu, promo, money):
    make_additional_menu(menu, promo)

    for keys in menu:
        menu[keys].getInfo()

    N = len(menu)

    tab = [[0] * (money + 1) for i in range(N + 1)]

    for i in range(money + 1):
        tab[0][i] = 0

    for i in range(N + 1):
        tab[i][0] = 0  # fill first column with 0

    for i in range(1, N + 1):
        for k in range(1, money + 1):
            if k >= menu[i].price:
                tab[i][k] = max(tab[i - 1][k], tab[i][k - menu[i].price] + menu[i].calories)
            else:
                tab[i][k] = tab[i - 1][k]

    cur_weight = 0
    for l in tab:
        print(cur_weight, '\t', l)
        cur_weight += 1

    find_ans_2(N, money, tab, menu)


def find_ans_2(i, k, tab, menu):
    if tab[i][k] == 0:
        return
    if tab[i][k] == tab[i - 1][k]:
        find_ans_2(i - 1, k, tab, menu)
    else:
        find_ans_2(i, k - menu[i].price, tab, menu)
        answer.append(menu[i].name)
    # answer


def find_ans_1(i, k, tab, menu, needed_calories):
    if tab[i][k] == 0:
        return

    if tab[i][k - 1] >= needed_calories:
        find_ans_1(i, k - 1, tab, menu, needed_calories)

    elif tab[i][k] == tab[i - 1][k]:
        find_ans_1(i - 1, k, tab, menu, needed_calories)
    else:
        find_ans_1(i, k - menu[i].price, tab, menu, needed_calories)
        answer.append(menu[i].name)


if __name__ == '__main__':
    answer = []
    start(sys.argv[1:])
    print(answer)
