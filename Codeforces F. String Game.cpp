/**
 * Codeforces F. String Game
 * Temáticas: Busqueda Binaria
 *
 * Idea:
 */
#include <bits/stdc++.h>
#include <math.h>
#define ENDL '\n'
#define OPTIMIZAR_IO ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define PRESICION(x) cout.setf(ios::fixed,ios::floatfield); cout.precision(x);
#define MAX_N 1005
#define MOD 1000000007
#define EPS 1e-9
#define INF 1000000000
#define LL long long
#define ULL unsigned long long
#define pii pair<int,int>
#define ALPHABET_SIZE 26 //['a-z']
using namespace std;

bool check(string a,string b,vector<int> dO,int d){
	int idx =0;
	for(int i=0;i<a.size() && idx< b.size();i++){
		if(dO[i]<=d) continue;
		if(a[i]==b[idx]) idx++;
	}
	return idx == b.size();
}

int main() {
	OPTIMIZAR_IO
	//PRESICION(20)
    string p,t;
	int x,begin,end;

	cin>>p>>t;

	vector<int> orderDelete(p.size());



	for(int i=1;i<=p.size();i++){
		cin>>x;
		orderDelete[x-1]=i;
	}

	begin =0;
	end = p.size();

	while(begin+1<end){
		x=(begin+end)/2;
		if(check(p,t,orderDelete,x)){
			begin=x;
		}else{
			end=x;
		}
	}

	cout<<begin<<ENDL;

	return 0;
}

