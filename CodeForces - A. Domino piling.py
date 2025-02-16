"""
 CodeForces - A. Domino piling
 
 Temática: Aritmética-Álgebra 
 
 Idea: Dado un tablero de NxM determinar la máxima cantidad de piezas de domino
 con dimensiones 2x1 se puede colocar en el tablero tal que no exista fichas 
 superpuesta una arriba de otras y no puede existir una ficha parcialmente fuera 
 del tablero.Para determinar la cantidad piezas que vamos a colocar vamos a establecer 
 que M tendra la dimensión mayor del tablero mientras N será el menor de los dos. 
 Esta idea nos va facilitar el analisis y posterior solución. Para esto vamos a 
 ver posibles situaciones:
     1- N es igual a 1 entonces la cantidad de fichas sera floor(M/2). La unica opción
     nos queda es colocar las fichas una detrás de la otra a lo largo de M. 
     2- N mayor que 1 entonces la cantidad d fichas va ser igual M*(N/2) mas si N
     es impar quedaria una fila de M columnas donde puedo colocar M/2 piezas 
     adicionales. La idea es ocupando un area de 2xM dentro de un area de NxM mientra
     sea posible si N es impar quedaría un area de 1xM que se podría poner M/2 fichas.
"""
def main():
   m, n = map(int, input().split())
   [m,n] = [max(m,n),min(m,n)]
   if n==1:
       print(m//2)
   else:
       print(m*(n//2)+(n%2)*(m//2))

if __name__ == '__main__':
    main()