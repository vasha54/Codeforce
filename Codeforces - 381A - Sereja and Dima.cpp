 /**
 * Codeforces - 381A - Sereja and Dima  
 * Temática: Simulación
 * 
 * Idea: 
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
#define MAX_N 100010
#define MOD  1000000007
 
using namespace std;
using namespace __gnu_pbds;

signed main()
{
    OPTIMIZAR_IO
    //PRESICION(2)
    READ_FILE
    //WRITE_FILE
    int n,turn=0;
	cin>>n;
	deque<int> values(n),answer(2,0);
	for(int i=0;i<n;i++) cin>>values[i];
	while(!values.empty()){
		n = max(values.back(),values.front());
		answer[turn%2]+=n;
		turn++;
		if (n == values.back()) values.pop_back();
		else values.pop_front();
    }
	cout<<answer[0]<<" "<<answer[1]<<ENDL;
    return 0;
}

