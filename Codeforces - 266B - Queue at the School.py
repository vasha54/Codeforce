"""
    Codeforces - 266B - Queue at the School

    Temática : Implementación + Simulación
    
    Idea: Dada una cola de nños y niñas donde se sabe que en cada segundo el si
    en la posición i existe un niño y en la posición i+1 una níña estos 
    intercambian sus posiciones. Se quiere dado el orden incial de la cola y 
    unas x cantidad de segundos saber el orden de la cola una vez pasado los x 
    segundos . Con simular el proceso es suficiente

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
    nchilds, seconds = map(int,input_line().split())
    queue_childs = list(input_line())

    for _ in range(seconds):
        i = 0
        while i < nchilds-1:
            if queue_childs[i] == 'B' and queue_childs[i+1] == 'G':
               queue_childs[i] = 'G'
               queue_childs[i+1] = 'B'
               i+=2
            else:
                i+=1

    print("".join(queue_childs))  

if __name__ == "__main__":
    solve()
