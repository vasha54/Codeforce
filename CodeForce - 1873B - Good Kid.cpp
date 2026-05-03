 /**
 * Codeforces - 1873B - Good Kid 
 * Temática: Greedy 
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
    int cases,nvalues;
    cin>>cases;
    while(cases--){
        cin>>nvalues;
        vector<int> values(nvalues);
        for(int i=0;i<nvalues;i++) cin>>values[i];
        
        sort(values.begin(),values.end());
        values[0]++;
        int answer = 1;
        for(int i=0;i<nvalues;i++) answer*=values[i];

        cout<<answer<<ENDL;
    }
    return 0;
}

