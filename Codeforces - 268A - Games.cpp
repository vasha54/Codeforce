 /**
 * Codeforces - 268A - Games 
 * Temática: Estructura de Datos + Mapas + Busqueda 
 * 
 * Idea: 
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
    int nteams, games, l, v, answer=0;
	map<int,int> local,visits;
	cin>>nteams;

	for(int i=0;i<nteams;i++){
		cin>>l>>v;
		local[l]++;
		visits[v]++;
	}
    
	for(auto it: visits){
		answer+=(local[it.first] * it.second);
	}

	cout<<answer<<ENDL;

}

