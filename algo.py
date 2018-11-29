import sys
from menu import Menu
from parser import *
import collections
import pdb


def start(argv):
    file_menu = argv[0]
    file_promo = argv[1]
    money = int(argv[2])

    menu = menuParser(file_menu)
    promo = promoParser(file_promo)
    make_additional_menu(menu, promo)

    for keys in menu:
        menu[keys].getInfo()

    N = len(menu)

    tab = [[0] * (money + 1) for i in range(N + 1)]

    for i in range(money + 1):
        tab[0][i] = 0

    for i in range(1, N + 1):
        for c in range(money + 1):
            tab[0][i] = 0  # fill first column with 0
    for i in range(1, N + 1):
        for k in range(money + 1):
            if k >= menu[(i)].price:
                tab[i][k] = max(tab[i - 1][k], tab[i][k - menu[i].price] + menu[i].calories)
            else:
                tab[i][k] = tab[i - 1][k]

    cur_weight = 0
    for l in tab:
        print(cur_weight, '\t', l)
        cur_weight += 1

    find_ans(N, money, tab, menu)


def find_ans(i, k, tab, menu):
    if tab[i][k] == 0:
        return
    if tab[i][k] == tab[i - 1][k]:
        find_ans(i - 1, k, tab, menu)
    else:
        find_ans(i, k - menu[i].price, tab, menu)
        answer.append(menu[i].name)
    # answer


def find_ans_1(i, k, tab, menu, needed_calories):
    # for i in range(1, N+1):
    #     for k in range(money+1):
    #         if (needed_calories<=tab[i][k]):
    #             print(i,k,tab[i][k])
    if tab[i][k] == 0:
        return

    if tab[i][k - 1] >= needed_calories:
        find_ans_1(i, k - 1, tab, menu, needed_calories)

    elif tab[i][k] == tab[i - 1][k]:
        find_ans_1(i - 1, k, tab, menu, needed_calories)
    else:
        find_ans_1(i, k - menu[i].price, tab, menu, needed_calories)
        answer.append(menu[i].name)


def MONEY_CALORIES(menu, grocery_list):
    money = 0
    calories = 0
    for i in grocery_list:
        money += menu[i].price
        calories += menu[i].calories
    return money, calories


def first_algo(argv):
    file_menu = argv[0]
    file_promo = argv[1]

    grocery_list_ = list(map(int, (argv[2]).split(',')))
    grocery_list = collections.Counter(grocery_list_)
    menu = menuParser(file_menu, grocery_list)

    ans = MONEY_CALORIES(menu, grocery_list_)
    money = ans[0]
    needed_calories = ans[1]
    print(money, needed_calories)
    promo = promoParser(file_promo)
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
            for l in reversed(range(1, min(menu[i].count, k // menu[i].price) + 1)):
                tab[i][k] = max(tab[i][k], tab[i - 1][k - l * menu[i].price] + menu[i].calories * l)

    cur_weight = 0
    for l in tab:
        print(cur_weight, '\t', l)
        cur_weight += 1

    find_ans_1(N, money, tab, menu, needed_calories)


if __name__ == '__main__':
    answer = []
    first_algo(sys.argv[1:])
    # start(sys.argv[1:])
    print(answer)
