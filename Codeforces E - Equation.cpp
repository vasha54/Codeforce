/**
 * Codeforces E - Equation
 * Temáticas: Busqueda Binaria
 *
 * Idea:
 */
#include <bits/stdc++.h>
#include <math.h>
#define ENDL '\n'
#define OPTIMIZAR_IO ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define PRESICION(x) cout.setf(ios::fixed,ios::floatfield); cout.precision(x);
#define MAX_N 1005
#define MOD 1000000007
#define EPS 1e-9
#define INF 1000000000
#define LL long long
#define ULL unsigned long long
#define pii pair<int,int>
#define ALPHABET_SIZE 26 //['a-z']
using namespace std;



int main() {
	OPTIMIZAR_IO
	PRESICION(20)

	double c,begin=0,end,x;

	cin>>c;

	end=c;

	for(int i=1;i<=150;i++){
		x=(begin+end)/2.00000;
		if(x*x+sqrt(x)>=c)
			end=x;
		else
			begin=x;
	}
	cout<<end<<ENDL;
	return 0;
}

