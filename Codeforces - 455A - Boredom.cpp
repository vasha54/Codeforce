/*
Codeforces - 455A - Boredom

Tematica: Programación Dinamica

Idea: El problema se puede reinterpretar como: tenemos un conjunto de números 
donde podemos elegir un valor x y ganar x puntos, pero al hacerlo eliminamos
todos los números con valor x, x-1 y x+1. Queremos maximizar la suma total de puntos.

Observaciones clave:
    Los números se pueden agrupar por su valor, contando cuántas veces aparece cada uno. 
    Llamemos freq[v] a la frecuencia del valor v.

    Si decidimos tomar el valor v, ganamos v × freq[v] puntos, pero no podremos tomar los valores 
    v-1 ni v+1.

Definimos dp[i] como la máxima puntuación que se puede obtener considerando únicamente números del 1 hasta *i*.
La relación de recurrencia es:

Si no tomamos el número i, entonces dp[i] = dp[i-1].

Si tomamos el número i, ganamos i × freq[i] puntos, pero no podemos tomar i-1, por lo que debemos sumar dp[i-2].
Por tanto:
    dp[i] = max(dp[i-1], dp[i-2] + i * freq[i])
El límite superior para los valores es 10⁵, por lo que podemos construir un arreglo de frecuencias hasta ese 
máximo y calcular la DP iterativamente.
*/
#include <iostream>
#include <math.h>
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define ENDL '\n'
#define OPTIMIZAR_IO ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define PRESICION(x) cout.setf(ios::fixed,ios::floatfield); cout.precision(x);
#define READ_FILE freopen("Input.txt","r",stdin);
#define WRITE_FILE freopen("Output.txt","w",stdout);
#define MAX_N 100000
#define MAX_TREE (MAX_N << 2)
#define MID (left+right)/2
#define MOD 1000000007
#define EPS 1e-4
#define INF 0x3f3f3f3f3f3f3f3f
#define int long long
#define uint unsigned long long
#define pii pair<int,int>
#define ALPHABET_SIZE 26 //['a-z']
#define Point pair<int, int>
#define X first
#define Y second
#define PLUS '+'
#define MINUS '-'
#define SPACE ' '
#define CELL_FREE '.'
#define CELL_WALL '#'
#define PRINT_LINE cout<<ENDL;
using namespace std;
using namespace __gnu_pbds;
int mov_r [] = { 0,  0, -1,  1};
int mov_c [] = {-1,  1,  0,  0};




signed main()
{
    OPTIMIZAR_IO
    //PRESICION(0)
    //READ_FILE
    //WRITE_FILE
    int n;
    cin >> n;
    vector<long long> freq(MAX_N + 1, 0);

    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        freq[x]++;
    }

    vector<long long> dp(MAX_N + 1, 0);
    dp[0] = 0;
    dp[1] = freq[1] * 1;

    for (int i = 2; i <= MAX_N; ++i) {
        dp[i] = max(dp[i-1], dp[i-2] + i * freq[i]);
    }

    cout << dp[MAX_N] << ENDL;
    return 0;
}