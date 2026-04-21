/*
Codeforces - 1915C - Can I Square?

    
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


bool is_square(int x) {
    int l = 1, r = 1e9;
    while (l <= r) {
        int mid = l + (r - l) / 2;
        if (mid * mid == x) return true;
        if (mid * mid > x) r = mid - 1;
        else l = mid + 1;
    }
    return false;
}
 
void solve() {
    int n;
    cin >> n;
    int s = 0;
    for (int i = 0, x; i < n; ++i) {
        cin >> x;
        s += x;
    }
    if (is_square(s)) cout << "YES\n";
    else cout << "NO\n";
}

signed main()
{
    //OPTIMIZAR_IO
    //PRESICION(0)
    //READ_FILE
    //WRITE_FILE
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}