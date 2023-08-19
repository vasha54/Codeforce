/**
 * Codeforces - B - Ropes
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

bool goodCut(double x, vector<long> piece, int k) {
	int p = 0;
	if (x == 0) return true;
	for (int i = 0; i < piece.size(); i++) {
		p += piece[i] / x;
	}
	return (p >= k);
}

int main() {
	OPTIMIZAR_IO
	PRESICION(20)
	int n, k;
	cin >> n >> k;
	vector<long> pieces(n);
	for (int i = 0; i < n; i++)
		cin >> pieces[i];

	sort(pieces.begin(),pieces.end());
	double begin = 0, end = pieces.back(), pivot;

	while (abs(end-begin)>EPS) {
		pivot = begin + (end - begin) / 2;

		if (goodCut(pivot, pieces, k))
			begin = pivot;
		else
			end = pivot;
	}

	cout << begin << ENDL;

	return 0;
}

