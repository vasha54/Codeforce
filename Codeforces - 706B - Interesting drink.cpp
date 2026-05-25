 /**
 * Codeforces - 706B - Interesting drink
 * Temática: Busqueda Binaria
 * 
 * Idea: 
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
	int n,querys,x,answer;
	cin>>n;
	vector<int> prices(n);
	for(int i=0;i<n;i++) cin>>prices[i];
	sort(prices.begin(), prices.end());
	cin>>querys;
	for(int i=0;i<querys;i++){
		cin>>x;
		answer = lower_bound(prices.begin(), prices.end(),(x+1)) - prices.begin();
		cout<<answer<<ENDL; 
	}
}

