"""
    Codeforces - 1619A - Square String?
    Temática : String
    
    Idea:  Dada una cadena determinar si se puede definir como la concatenacion
    de otra cadena dos veces. 
 
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
    cases = int(input_line())
    for i in range(0,cases):
        word = str(input_line().strip())
        n = len(word)
        if n % 2 == 0:
           first_half = word[:n//2]
           second_half = word [n//2:]
           print(("YES" if second_half == first_half else "NO"))
        else:
           print("NO")     
 
if __name__ == "__main__":
    solve()