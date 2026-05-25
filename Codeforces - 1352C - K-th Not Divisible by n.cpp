/**
 * Codeforces - 1352C - K-th Not Divisible by n
 * Temática: Búsqueda Binaria
 * 
 * Idea: La cantidad de enteros positivos no divisibles por n hasta un
 * número x viene dada por f(x) = x - ⌊x/n⌋. Buscamos el menor x tal que
 * f(x) = k. Si ese x resulta ser múltiplo de n, entonces el k-ésimo no
 * divisible es x-1; en caso contrario, es x. Mediante búsqueda binaria
 * sobre el rango [1, 10^18] (o n*k) se encuentra el x que iguala a k,
 * logrando una solución O(log(max)) por cada caso.
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

    int cases, begin, end, pivot, multiple, KK, n, k;
    cin>>cases;
    while(cases--){
        cin>>n>>k;
        begin=1;
        end = LONG_MAX;
        while(true){
            pivot = (begin + end)/2;
            multiple = pivot / n;
            KK = pivot - multiple;

            if(KK == k){
                cout<<(pivot%n ==0 ? pivot-1 : pivot)<<ENDL;
                break;
            } 
            else if(KK < k) begin = pivot+1;
            else end = pivot - 1 ;
        }
    }
    return 0;
}
