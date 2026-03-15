"""
    Codeforces - 80A - Panoramix's Prediction

    Temática : Teoría de Numeros + Criba de primos
    
    Idea: Dado dos números n y m donde n siempre es primos determinar si m es el
    proximo número primo despues de n.
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
MAX = 10**4
INF = 10**9

def read_nonempty():
    s = sys.stdin.readline()
    while s is not None and s.strip() == "":
        s = sys.stdin.readline()
    return s.strip()


def solve():
    input_line = read_nonempty
    numbers = [ True for i in range(0,55)]
    primes = []

    for i in range(2,55):
        if numbers[i]:
            primes.append(i)
            for j in range(i*i,55,i):
                numbers[j] = False

    n, m = map(int,input_line().split())
    index_n = primes.index(n)
    print(("YES" if primes[index_n+1] == m else "NO"))

if __name__ == "__main__":
    solve()
