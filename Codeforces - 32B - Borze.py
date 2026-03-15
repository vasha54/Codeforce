"""
    Codeforces - 32B - Borze

    Temática : Implementación
    
    Idea: Dado el código en morse de un número en base ternaria expresar su 
    valor en decimal. Basta con procesar la cadena en el orden que se da 

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
    line = str(input_line())
    n = len(line)
    decode_ternary = ""
    i = 0
    while i < n:
        if line[i] == '.':
            decode_ternary = decode_ternary + "0"
            i += 1
        elif line[i] == '-':
            if line[i+1] == '-':
                decode_ternary = decode_ternary + "2"
            elif line[i+1] == '.':
                decode_ternary = decode_ternary + "1"
            i += 2
    print(decode_ternary)

if __name__ == "__main__":
    solve()
