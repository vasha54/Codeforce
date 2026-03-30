"""
    Codeforces - 136A - Even Odds

    Temática : Aritmetica - Algebra
    
    Idea: Dados todos los numeros naturales de 1 a N se quiere saber el numero
    que ocupa la posición luego que los números son ordenados de la siguiente manera
    - Se coloca todos los numeros impares ordenados de forma ascendente
    - Se coloca todos los numeros pares ordenados de forma ascendente

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
    n,k = map(int,input_line().split())
    if n % 2 == 0:
        if k <= int(n / 2):
            print(k*2-1)
        else:
            print((k-int(n/2))*2)
    else:
        if k <= int(n / 2) + 1:
            print(k*2-1)
        else:
            print((k-(int(n/2)+1))*2)


if __name__ == "__main__":
    solve()
