/*
Codeforces - 279B - Books

Tematica: Suma de prefijo + Dos punteros
    
*/
#include <iostream>
#include <math.h>
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define ENDL '\n'
#define OPTIMIZAR_IO ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define PRESICION(x) cout.setf(ios::fixed,ios::floatfield); cout.precision(x);
#define READ_FILE freopen("Input.txt","r",stdin);
#define WRITE_FILE freopen("Output.txt","w",stdout);
#define MAX_N 100010
#define MAX_TREE (MAX_N << 2)
#define MID (left+right)/2
#define MOD 1000000007
#define EPS 1e-4
#define INF 0x3f3f3f3f3f3f3f3f
#define int long long
#define uint unsigned long long
#define pii pair<int,int>
#define ALPHABET_SIZE 26 //['a-z']
#define Point pair<int, int>
#define X first
#define Y second
#define PLUS '+'
#define MINUS '-'
#define SPACE ' '
#define CELL_FREE '.'
#define CELL_WALL '#'
#define PRINT_LINE cout<<ENDL;
using namespace std;
using namespace __gnu_pbds;
int mov_r [] = { 0,  0, -1,  1};
int mov_c [] = {-1,  1,  0,  0};




signed main()
{
    OPTIMIZAR_IO
    //PRESICION(0)
    //READ_FILE
    //WRITE_FILE
    int nbooks, freeTimes, best=0;
    cin>>nbooks>>freeTimes;
    vector<int> dp(nbooks+5);
    dp[0]=0;
    for(int i=1;i<=nbooks;i++){
        cin>>dp[i];
        dp[i]+=dp[i-1];
    }
    int pl=0,pr=1;
    while(pr<=nbooks && pl<= pr){
        while(pr<=nbooks && dp[pr]-dp[pl]<=freeTimes ){
            best=max(best,pr-pl);
            pr++;
        }
        if(pr<=nbooks && dp[pr]-dp[pl]<=freeTimes)
            best=max(best,pr-pl);
        pl++;
    }
    cout<<best<<ENDL;
    return 0;
}