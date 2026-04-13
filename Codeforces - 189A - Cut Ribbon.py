"""
    Codeforces - 189A - Cut Ribbon
 
    Temática : Programación Dinámica
    
    Idea: Tenemos una cinta de longitud n y debemos cortarla en trozos de
    longitudes permitidas a, b o c (pueden repetirse). Queremos maximizar la
    cantidad de trozos obtenidos. Se garantiza que siempre existe al menos una
    forma de cortar la cinta usando solo esas longitudes.

    La solución dada implementa un DP iterativo que recuerda, para cada
    longitud i de la cinta, la máxima cantidad de trozos que se pueden obtener.

    Sea dp[i] = máximo número de trozos en que se puede cortar una cinta de 
    longitud i usando únicamente trozos de tamaño a, b o c.
    Si no es posible cortar la longitud i, dp[i] permanecerá en 0 (aunque más 
    adelante veremos que la inicialización se hace con cuidado).

    - Para cada corte en {a, b, c}, si corte <= n, entonces se puede formar un 
    trozo de esa longitud con exactamente 1 pieza, así que dp[corte] = 1.

    - El resto de dp[i] se inicializa implícitamente en 0.

    Recorremos i desde 1 hasta n. Si dp[i] > 0 (es decir, existe alguna forma 
    de cortar la longitud i), entonces para cada corte en {a, b, c} podemos 
    agregar un trozo más, obteniendo una nueva longitud i + corte. 

    dp[i + corte] = max(dp[i + corte], dp[i] + 1)

    Esto es equivalente a: si ya sabemos cómo cortar i en dp[i] trozos, al 
    añadir un trozo de tamaño corte obtenemos una forma de cortar i+corte con 
    un trozo más. Tomamos el máximo sobre todas las formas de llegar a esa 
    longitud.

    dp[n] contiene la máxima cantidad de trozos para la cinta original.
 
"""
 
from functools import cmp_to_key, reduce
from collections import deque, Counter
 
# Comparadores en Estructuras de Datos
import heapq
import sys
import itertools
import math
 
mov_r = [2, 2, -2, -2, 1, -1, 1, -1]
mov_c = [1, -1, 1, -1, 2, 2, -2, -2]
 
MOD = 10**9 + 7
MODM1 = MOD - 1          # para exponentes
MOD2M1 = 2 * MODM1       # para reducir d(N) antes de dividir por 2

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
    n,a,b,c = map(int,input_line().split())
    ribbon_pieces = [0] * (n+2)
    cuts = [a,b,c]
    for c in cuts:
        if c <= n:
            ribbon_pieces[c] = 1
    for i in range(1,n+1):
        if ribbon_pieces[i] != 0:
            for c in cuts:
                if i+c <=n:
                    ribbon_pieces[i+c] = max(ribbon_pieces[i+c],ribbon_pieces[i]+1)
    print(ribbon_pieces[n])

        
if __name__ == "__main__":
    solve()
