"""
    Codeforces - 110A - Nearly Lucky Number
    Temática : Add-Hoc   
    
    Idea: Dado un numero contar la cantidad de digitos de 4 y 7 que tiene
    si dicha cantidad es un numero que se conforma solo por digitos de 4 y 7
    imprimir YES en caso contrario NO.
 
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

def is_correct(_x):
    strx = str(_x)
    for i in strx:
        if i != '4' and i != '7':
            return False
    return True 
 
def solve():
    input_line = read_nonempty
    number = input_line()
    sums = 0 
    for x in number:
        if x in ['4','7']:
            sums = sums + 1

    
    if is_correct(sums):
        print("YES")
    else:
        print("NO")
 
 
if __name__ == "__main__":
    solve()