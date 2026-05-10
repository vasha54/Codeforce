 /**
 * Codeforces - 158B - Taxi  
 * Temática: Greedy
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
    int taxis=0, ngroups, g1=0, g2=0, g3=0, g4=0, xi;
	cin>>ngroups;
	for(int i=0;i<ngroups;i++){
		cin>>xi;
		if(xi==4)g4++;
		else if(xi==3)g3++;
		else if(xi==2)g2++;
		else if(xi==1)g1++;
	}
	taxis+=g4;
    
	while(g3>0){
		taxis++;
		g3--;
		if(g1>0) g1--;
	}
	
	while(g2>=2){
		taxis++;
		g2-=2;
	}

	if(g2>=1){
		taxis++;
		g2--;
		g1-=2;
	}
	
	while(g1>0){
		taxis++;
		g1-=4;
	}
	
	cout<<taxis<<ENDL;

    return 0;
}

