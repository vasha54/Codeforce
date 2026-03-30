"""
    Codeforces - 230A - Dragons

    Temática : Ordenamiento + Greedy
    
    Idea: Dado un grupo de dragones los cuales tienen cada uno valor de fuerza
    y un valor de bonificación si se mata dicho dragón. Se parte con una fuerza inicial
    con la cual sola podrá matar al dragón si dicho valor es mayor estricto a la fuerza
    del dragon que se enfrente , en caso de matar al dragon su fuerza se incrementa 
    en el valor de la bonificación del dragón muerto. Se necesita saber si se puede 
    pasar de nivel lo cual se logra matando a todos los dragones. Para determinar
    esto solo basta ordenar los dragones de acuerdo a su fuerza de forma ascedentemente
    y simular el proceso de ir matando los dragones uno si algún la fuerza no es superior
    a lde dragon i entonces no se podrá pasar de nivel 

"""
 
from functools import cmp_to_key, reduce
from collections import deque, Counter
 
# Comparadores en Estructuras de Datos
import heapq
import sys
import itertools
 
mov_r = [2, 2, -2, -2, 1, -1, 1, -1]
mov_c = [1, -1, 1, -1, 2, 2, -2, -2]
 
MOD = 10**9 + 7
INV2 = (MOD + 1) // 2   # inverso modular de 2
MAX = 10**6+10
INF = 10**9
# dp = [[0]*(MAX+5) for _ in range((MAX+5))]

def read_nonempty():
    s = sys.stdin.readline()
    while s is not None and s.strip() == "":
        s = sys.stdin.readline()
    return s.strip()


def solve():
    input_line = read_nonempty
    strength, ndragons = map(int,input_line().split())
    dragons = [] 
    for _ in range(ndragons):
        live, bonus = map(int,input_line().split())
        dragons.append((live,bonus))

    dragons = sorted(dragons, key=lambda x: (x[0], -x[1]))

    next_level = True
    i = 0 

    while next_level and i < ndragons:
        if dragons[i][0] < strength :
            strength += dragons[i][1]
        else:
            next_level = False
        i += 1
    print(("YES" if next_level else "NO"))



if __name__ == "__main__":
    solve()
