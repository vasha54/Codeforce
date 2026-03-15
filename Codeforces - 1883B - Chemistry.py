"""
    Codeforces - 1883B - Chemistry
    Temática : String
    
    Idea:Dada una cadena de caracteres de longitud n se quiere saber si 
    removiendo exactamente k caracteres y pudiendo hhacer algún reordenamiento
    se puede formar con las letras un palindrome.
 
    Para solucionar el problema podemos calcular para cada letra de la cadena
    su frecuencia de aparición de esta forma una letra siempre podrá aportar
    de dos en dos siempre que exista necesidad de letras mayor o igual a dos.
 
    Esta forma la cantidad de letras pendiente a selecionar puede caer en los 
    siguientes casos
 
    - Si es 0 significa que se puede forma el palindrome con las cantidades de 
    cada letra selecionada
    - Si es 1 significa que el palindrome a forma es impar por lo que debe 
    existir al menos un letra que su cantidad de ocurrencias seleccionada sea 
    impar por lo que debemos revisar si de las letras con aún ocurrencias sin
    selecionar queda alguna con al menos una si es asi es posible construir el palindrome sino no existará manera de construir el palindrome
    - Si es mayor a 1 es imposible construir el palindrome por in suficientes ocurrencias de letras letras.
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
MAX = 10**5
INF = 10**9

def read_nonempty():
    s = sys.stdin.readline()
    while s is not None and s.strip() == "":
        s = sys.stdin.readline()
    return s.strip()

def solve():
    input_line = read_nonempty
    cases = int(input_line())
    while cases > 0 :
        cases = cases -1
        n,k = map(int, input_line().split())
        word =str(input_line())
        freq = [0] * 26
        for ch in word:
            freq[ord(ch) - ord('a')] += 1

        odd = sum(1 for cnt in freq if cnt % 2 == 1)

        if odd <= k + 1:
            print("YES")
        else:
            print("NO")
        

if __name__ == "__main__":
    solve()