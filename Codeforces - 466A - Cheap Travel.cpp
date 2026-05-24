/**
 * Codeforces - 466A - Cheap Travel
 * Temática: Aritmetica - Algebra
 * 
 * Idea: Para minimizar el gasto se consideran tres estrategias: 
 *  - comprar únicamente billetes de un viaje, 
 *  - comprar únicamente billetes de m viajes (aunque sobren viajes), 
 *  - comprar una combinación donde se cubre la mayor parte con billetes especiales y el resto con sencillos. 
 * Se elige la de menor coste.
 */
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

#define ENDL '\n'
#define OPTIMIZAR_IO ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define PRESICION(x) cout.setf(ios::fixed,ios::floatfield); cout.precision(x);
 
#ifdef LOCAL
    #define READ_FILE freopen("Input.txt","r",stdin);
    #define WRITE_FILE freopen("Output.txt","w",stdout);
#else
    #define READ_FILE 
    #define WRITE_FILE 
#endif
#define REP(x) for(int i=1;i<=x;i++)
#define int long long
#define uint unsigned long long
#define PRINT_LINE cout<<ENDL;
#define MAX_N 200010
#define MAX_TREE MAX_N << 2
#define MOD  1000000007
#define MID (right+left)/2
 
using namespace std;
using namespace __gnu_pbds;

signed main()
{
    OPTIMIZAR_IO
    //PRESICION(2)
    READ_FILE
    //WRITE_FILE
    int n, m, a, b;
    cin >> n >> m >> a >> b;

    // Opción 1: solo billetes sencillos
    int costo_solo_sencillos = n * a;

    // Opción 2: solo billetes especiales (se pueden comprar de más)
    int boletos_especiales = (n + m - 1) / m; // división con redondeo hacia arriba
    int costo_solo_especiales = boletos_especiales * b;

    // Opción 3: combinación óptima de especiales + sencillos para el resto
    int especiales = n / m;
    int resto = n % m;
    int costo_combinado = especiales * b + resto * a;

    // El mínimo de las tres opciones
    int respuesta = min({costo_solo_sencillos, costo_solo_especiales, costo_combinado});

    cout << respuesta <<ENDL;
    return 0;
}