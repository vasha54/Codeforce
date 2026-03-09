"""
    Codeforces - 271A - Beautiful Year
    Temática : Busqueda Exhaustiva  o Completa
    
    Idea: Dado un valor menor que 10000 y mayor igual 1000 es buscar el menor 
    valor mayor que el valor dado que cumpla con la condición que no tenga digitos 
    repetidos. Como el rango es pequeño podemos implementar una busqueda completa
    hasta encontrar el valor solicitado 
 
"""
from functools import cmp_to_key, reduce
from collections import deque, Counter
 
# Comparadores en Estructuras de Datos
import heapq
import sys
 
mov_r = [2, 2, -2, -2, 1, -1, 1, -1]
mov_c = [1, -1, 1, -1, 2, 2, -2, -2]
 
MOD = 10**9 + 7

def check(_year):
    x = str(_year)
    frec = Counter(x)
    if len(x) == len(frec):
       return True 
    return False
 
def read_nonempty():
    s = sys.stdin.readline()
    while s is not None and s.strip() == "":
        s = sys.stdin.readline()
    return s.strip()

def solve():
    input_line = read_nonempty
    year = int(input_line())
    year = year + 1
    while not check(year):
        year = year + 1   
    print(year) 
 
if __name__ == "__main__":
    solve()