 /**
 * Codeforces - 9A - Die Roll 
 * Temática: Probabilidad 
 * 
 * Idea: Dot gana si en su lanzamiento obtiene un valor mayor o igual al mayor 
 * resultado entre Yakko y Wakko. El dado tiene 6 caras, así que los casos favorables 
 * son 7 - max(Y,W). Luego se simplifica la fracción favorables/6 usando el máximo común 
 * divisor y se imprime en el formato pedido. Si la probabilidad es 0 (cuando max(Y,W)=6?) 
 * realmente 6 da 1 favorable -> 1/6, no cero. Probabilidad cero sólo si favorables=0, es decir, 
 * cuando max(Y,W)>=7, pero como Y, W ≤ 6, favorables ≥ 1. Así que nunca se imprimirá "0/1" a 
 * menos que los valores fueran mayores, pero se puede cubrir el caso por completitud; con 
 * la lógica actual siempre dará al menos 1/6. La simplificación funciona correctamente.  
 *
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
    int Y, W;
	cin>>Y>>W;
	int better = max(Y,W);
	int favor = 7 - better;
	int total = 6;
	int g = __gcd(favor,total);
	favor /= g;
	total /= g;
	cout<<favor<<"/"<<total<<ENDL;
}

