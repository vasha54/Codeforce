"""
    Codeforces - 131A - cAPS lOCK
    Temática : String + Ad -Hoc
    
    Idea: El problema plantea una regla para corregir palabras que han sido 
    escritas accidentalmente con la tecla Bloq Mayús activada. Se considera que 
    una palabra fue escrita con esa tecla activada si cumple alguna de estas 
    condiciones:

        Todas las letras son mayúsculas (ejemplo: "HTTP").

        Todas las letras excepto la primera son mayúsculas (ejemplo: "hELLO").

    En esos casos, debemos cambiar el caso de todas las letras (las mayúsculas 
    pasan a minúsculas y viceversa). Si la palabra no cumple ninguna de las dos 
    condiciones, se deja igual.
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
    word = input_line()
    if len(word) == 1 or word[1:].isupper():
        print(word.swapcase())
    else:
        print(word)

if __name__ == "__main__":
    solve()