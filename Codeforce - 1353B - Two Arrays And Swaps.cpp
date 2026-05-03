 /**
 * Coderfoce - 1353B  - Two Arrays And Swaps 
 * Temática: Ordenamiento
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
#define MAX_N 200010
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
    //WRITE_FILE
    int cases, n, k, x;
    cin>>cases;
    while(cases --){
        cin>>n>>k;
        vector<pii> values(2*n);
        for(int i=0;i<n;i++){
            cin>>x;
            values[i]={x,1};
        }
        for(int i=n;i<2*n;i++){
            cin>>x;
            values[i] = {x,0};
        }
        sort(values.rbegin(),values.rend());
        int sums = 0, nn = 0, kk = 0;
        for(auto it:values){
            if(nn < n){
                if(it.second == 1){
                    sums+=it.first;
                    nn++;
                }
                if(it.second == 0 && kk < k ){
                    sums+=it.first;
                    kk++;
                    nn++;
                }
            }
        }
        cout<<sums<<ENDL;       

    }
    return 0;
}

