"""
    Codeforces - 520B - Two Buttons
    Temática : Teoria grafos : BFS camino mínimo    
    
    Idea: Dado dos valores n y m y dos posibles operaciones:
        - Multiplicar el valor n por dos
        - Decrementar el valor de n en uno
    Determinar la menor cantidad de operaciones para del valor n obtener el valor
    m. 
    Para solucionar el problema podemos modelar el problema como un grafo dirigido
    donde cada numero es un nodo y el nodo X tendrá una arista hacia los nodos 
    X*2 y X-1 con peso 1. Por lo que tenemos un grafo dirigido y ponderado con
    ponderación constante para todas las aristas y debemos encontrar el camino 
    mas corto del nodo N al nodo M por tanto podemos aplicar un BFS para hallar
    la lóngitud de ese camino. 
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
MAX = 10**5
INF = 10**9

# dp = [[0] * (MAX) for _ in range(MAX)]



def read_nonempty():
    s = sys.stdin.readline()
    while s is not None and s.strip() == "":
        s = sys.stdin.readline()
    return s.strip()

def solve():
    input_line = read_nonempty
    n, m = map(int, input_line().strip().split())
    queue = deque()
    queue.append((n,0))
    find = False
    visit = [False for i in range(MAX)]
    visit[n] = True
    while queue and not find:
        pair = queue.popleft()
        if pair[0] == m:
            print(pair[1])
            find = True
        else:
            red = pair[0] * 2
            blue = pair[0] - 1
            if 1 <= red and red < MAX and not visit[red]:
                queue.append((red,pair[1]+1))
                visit[red] = True
            if 1 <= blue and blue < MAX and not visit[blue]:
                queue.append((blue,pair[1]+1))
                visit[blue] = True

if __name__ == "__main__":
    solve()