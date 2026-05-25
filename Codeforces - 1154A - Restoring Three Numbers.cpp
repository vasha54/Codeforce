 /**
 * Codeforces - 1154A - Restoring Three Numbers
 * Temática: Aritmetica - Algebra
 * 
 * Idea: Se pensado tres números enteros positivos a, b y c. Los 
 * mantiene en secreto, pero escribe cuatro números en una pizarra en 
 * orden arbitrario: las tres sumas por parejas (a+b, a+c, b+c) y la 
 * suma de los tres números (a+b+c). Así, en la pizarra hay cuatro 
 * números desordenados. Se pide adivinar los valores de a, b y c a 
 * partir de esos cuatro números. Se puede imprimir cualquier orden 
 * de los tres números. Los números originales pueden ser iguales 
 * (incluyendo el caso a=b=c).
 * 
 * El problema se resuelve observando que entre los cuatro números 
 * dados, el mayor es la suma total a+b+c. Por lo tanto, para obtener 
 * a, b y c, basta con restar de ese máximo cada uno de los otros tres 
 * números.
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
	vector<int> values(4);
	for(int i=0;i<4;i++) cin>>values[i];
	int max_v = *max_element(values.begin(),values.end());
	for(int x: values){
		if(max_v != x) cout<<max_v-x<<" ";
	}
	cout<<ENDL;
}

