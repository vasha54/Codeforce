/**
 * Codeforces - 1360B - Honest Coach
 * Temática: Greedy + Ordenamiento + Busqueda
 * 
 * Idea: Dado un grupo de valores se debe crear dos lista (A, B) con estos números tal que
 * la expresión |max(A) - min(B)| de el menor valor mínimo. La idea es bien simple solo 
 * debemos ordenar los valores de manera ascedentemente y luego buscar los valores X y Y donde
 * X <= Y y son valores adyancentes en la lista ordenadas y la diferencia entre ellos es la minima
 * entre todos los posibles pares (x,y). Lo valores de la lista A sería Y con todos los valores menores
 * o a la izquierda de X mientras la lista B sería Y con todos los valores a la derecha o mayores de X 
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
#define pii pair<int,int>
#define tiii tuple<int,int,int>
#define MAX_N 110
#define MAX_TREE MAX_N << 2
#define MOD  1000000007
#define MID (right+left)/2

using namespace std;
using namespace __gnu_pbds;


int mov_r [] ={ 0, 0, 1,-1};
int mov_c [] ={ 1,-1, 0, 0};


signed main()
{
    OPTIMIZAR_IO
    //PRESICION(2)
    READ_FILE
    //WRITE_FILE

    int cases, n, answer;
    cin>>cases;
    while(cases--){
        cin>>n;
        vector<int> values(n);
        for(int i=0;i<n;i++) cin>>values[i];

        sort(values.begin(),values.end());
        answer = LONG_MAX;
        for(int i=1;i<n;i++){
            answer = min(answer,values[i]-values[i-1]);
        }
        cout<<answer<<ENDL;
    }
    return 0;
}