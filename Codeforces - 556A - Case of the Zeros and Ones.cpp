/**
 * Codeforces - 556A - Case of the Zeros and Ones
 * Temática: Greedy
 * 
 * Idea: Cada operación elimina exactamente un '0' y un '1' adyacentes (sin importar
 * el orden). Mientras existan ambos caracteres en la cadena, siempre es posible
 * encontrar un par adyacente "01" o "10" y eliminarlo, porque si hay al menos un
 * '0' y un '1', forzosamente habrá un punto donde la cadena cambia de 0 a 1 o
 * viceversa, formando un par removible.
 *
 * Por lo tanto, el proceso se repite hasta que se agota uno de los dos caracteres.
 * El número total de eliminaciones es min(#0, #1), y la longitud final será la
 * diferencia entre las cantidades: max(#0, #1) - min(#0, #1) = abs(#0 - #1).
 *
 * Complejidad: O(n) para contar los caracteres. 
 */
#include <bits/stdc++.h>
#include <bitset>
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
#define MAX_N 1000010
#define MOD  1000000007
#define pii pair<int,int>
#define tiib tuple<int,int,bool>

using namespace std;
using namespace __gnu_pbds;



signed main()
{
    OPTIMIZAR_IO
    //PRESICION(2)
    READ_FILE
    //WRITE_FILE

    int n, zeros=0, ones=0;
    string binary;
    cin>>n;
    cin>>binary;
    for(auto x : binary){
        x == '0' ? zeros++ : ones++;
    }
    cout<<max(zeros,ones)-min(zeros,ones)<<ENDL;
    
    return 0;
}
