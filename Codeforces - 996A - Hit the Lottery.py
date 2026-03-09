"""
    Codeforces - 996A - Hit the Lottery
    Temática : Greddy
    
    Idea: Dado una cantidad de dinero N se quiere saber la mínima cantidad de
    billetes con las denomicaciones [1, 5, 10, 20, 100]
        
"""
 
from functools import cmp_to_key, reduce
from collections import deque, Counter
 
# Comparadores en Estructuras de Datos
import heapq
import sys
 
mov_r = [2, 2, -2, -2, 1, -1, 1, -1]
mov_c = [1, -1, 1, -1, 2, 2, -2, -2]
 
MOD = 10**9 + 7

def read_nonempty():
    s = sys.stdin.readline()
    while s is not None and s.strip() == "":
        s = sys.stdin.readline()
    return s.strip()

def solve():
    input_line = read_nonempty
    n = int(input_line())
    bills = 0
    bill = [100, 20, 10, 5]
    for b in bill:
        bills = bills + (n // b)
        n = n % b
    bills = bills + n 
    print(bills)


if __name__ == "__main__":
    solve()