import sys
from menu import Menu
from parser import *
# import pdb

def start(argv):
    file_menu = argv[0]
    file_promo = argv [1]
    money =  int (argv [2])
    
    menu = menuParser(file_menu)
    promo = promoParser(file_promo)
    make_additional_menu(menu, promo)



    for keys in menu:
      menu[keys].getInfo()


    N = len(menu)

    tab = [[0] * (money+1) for i in range(N+1)]  
    
    for i in range (money+1):
        tab [0][i]=0
    
    for i in range (1, N+1):
        for c  in range (money+1):
            tab [0][i]=0 #fill first column with 0
    for i in range(1, N+1):    
        for k in range(money+1):                                                      
            if k >= menu[(i)].price:                                              
                tab[i][k] = max( tab[i - 1][k], tab[i][ k-menu[i].price] + menu[i].calories) 
            else:
                tab[i][k] = tab[i - 1][k] 

    cur_weight = 0
    for l in tab:

        print (cur_weight,'\t',l)     
        cur_weight+=1

    find_ans(N, money, tab, menu)

def find_ans(i, k, tab, menu):
    if tab[i][k] == 0:
        return
    if tab[i][k] == tab [i-1][k]:
        find_ans(i-1, k, tab, menu)
    else:
        find_ans(i, k - menu[i].price ,tab, menu)
        answer.append(menu[i].name)
    #answer      
 


def first_algo(argv):
    file_menu = argv[0]
    file_promo = argv [1]
    menu =  int (argv [2])
    
    menu = menuParser(file_menu)
    promo = promoParser(file_promo)



if __name__ == '__main__':
    answer=[]
    start(sys.argv[1:])
    print(answer)