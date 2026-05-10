 /**
 * Codeforces - 151A - Soft Drinking 
 * Temática: Aritmetica Algebrá
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
#define MAX_N 200010
#define MAX_TREE MAX_N << 2
#define MOD  1000000007
#define MID (right+left)/2
 
using namespace std;
using namespace __gnu_pbds;

// int values[MAX_N];
// int rt[MAX_TREE];
// int rtP[MAX_TREE];
// int n, nquerys, rooms;

// void build(int indx, int left, int right){
// 	if(left == right){
// 		rt[indx] = values[left];
// 		rtP[indx] = left;
// 	}
// 	build(indx*2, left, MID);
// 	build(indx*2+1, MID+1, right);
// 	rt[indx] = max(rt[indx*2],rt[indx*2+1]);
// 	if(rt[indx] == rt[indx*2]) rtP[indx] = rtP[indx*2];
// 	else rtP[indx] = rtP[indx*2+1];
// }

// void update(int indx, int pos, int _v, int left, int right){
// 	if(left == right){
// 		rt[indx] = _v;
// 		rtP[indx] = pos;
	
// 	}
// 	else{
// 		if(pos<= MID) update(indx*2,pos,_v,left,MID);
// 		else update(indx*2+1, pos, _v, MID+1, right);
// 		rt[indx] = max(rt[indx*2],rt[indx*2+1]);
// 		rtP[indx] = 
// 	}	
// }

// int query(int indx, int _v, int left, int right){

// }

signed main()
{
    OPTIMIZAR_IO
    //PRESICION(2)
    READ_FILE
    //WRITE_FILE
    int friends, bottles, milliliters, limes, slices, grams, nl, np;
    cin >> friends >> bottles >> milliliters >> limes >> slices >> grams >> nl >> np;

    int toastsDrink= (bottles * milliliters) / (friends * nl);
    int toastsLime = (limes * slices) / friends;
    int toastsSalt = grams / (friends * np);

    int answer = min({toastsDrink, toastsLime, toastsSalt});

    cout << answer << endl;
    
    return 0;
}

