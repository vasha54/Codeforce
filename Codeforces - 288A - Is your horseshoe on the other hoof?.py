"""
    Codeforces - 228A - Is your horseshoe on the other hoof?

    Temática : Estructura de Datos + Set
    
    Idea: Dado cuatro números determinar cuantos numeros debemos adicionar para
    que exista 4 números diferentes

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
    
    colors_horseshoes = set(map(int,input_line().split())) 
    print(4-len(colors_horseshoes))

if __name__ == "__main__":
    solve()

