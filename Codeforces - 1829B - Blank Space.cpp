 /**
 * Coderfoce - 1829B - Blank Space 
 * Temática: Programación Dinámica
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
    int cases, n, tmp_zeros, max_zeros;
	cin>>cases;
	while(cases --){
		cin>>n;
		vector<int> sequences(n);
		for(int i=0;i<n;i++) cin>>sequences[i];
		tmp_zeros = 0;
		max_zeros = 0;
		for(int i=0;i<n;i++){
			if(sequences[i] == 0) tmp_zeros++;
			else tmp_zeros = 0;
			max_zeros = max(max_zeros,tmp_zeros);
		}
		cout<<max_zeros<<ENDL;
	}
    return 0;
}

