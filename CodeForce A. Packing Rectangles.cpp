/**
 * CodeForce A. Packing Rectangles
 * Temáticas: Búsqueda Binaria.
 *
 * Idea:
 **/
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

ULL w, h, n;

bool isSideGood(ULL x){
    return (x / w) * (x / h) >= n;
}

int main() {
	OPTIMIZAR_IO
	cin >> w >> h >> n;

	ULL low = 0, high = 1;

	while (!isSideGood(high))
		high *= 2;

	ULL minSide = 0;
	while (high > low + 1) {
		ULL mid = (low + high) >> 1;

		if (isSideGood(mid)) {
			high = mid;
		} else
			low = mid;
	}

	cout << high << ENDL;
	return 0;
}

