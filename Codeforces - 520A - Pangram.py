"""
    Codeforces - 520A - Pangram
    Temática : String
    
    Idea: Dada una cadena queremos saber si en la cadena esta o no al menos
    todas las letras del alfabeto al menos una vez sin importar la capitalización
 
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
    word = str(input_line())
    word = word.lower()
    frec = Counter(word)
    print(('YES' if len(frec) == 26 else 'NO'))
         
 
if __name__ == "__main__":
    solve()