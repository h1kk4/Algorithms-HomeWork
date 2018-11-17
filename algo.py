import sys
from menu import Menu
from parser import *
import pdb

def start(argv):
    file_menu = argv[0]
    file_promo = argv [1]
    money =  int (argv [2])
    menu = menuParser(file_menu)

    # for keys in menu:
    #   menu[keys].getInfo()


    N = len(menu)
    #print (menu)

    tab = [[0] * (money+1) for i in range(N+1)]  
    
    for i in range (money+1):
        tab [0][i]=0
    
    for i in range (1, N+1):
        for c  in range (money+1):
            tab [0][i]=0 #fill first column with 0
    for i in range(1, N+1):    
        for k in range(money+1):                                                      
            if k >= menu[(i)].p():                                              
                tab[i][k] = max( tab[i - 1][k], tab[i][ k-menu[i].p()] + menu[i].c()) 
                #print(i,'\t',k,'\t_1_')
            else:
                tab[i][k] = tab[i - 1][k] 
                #print(i,'\t',k,'\t_2_')
    cur_weight = 0
    for l in tab:

        print (cur_weight,'\t',l)     
        cur_weight+=1



if __name__ == '__main__':

    start(sys.argv[1:])