/**
 * Codeforces - D. Children Holiday
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

struct Assistant {
	LL timePerBallon, ballonConsecutive, timeTired;
};

LL blown(Assistant x, int time) {
	LL result = 0;

	result += x.ballonConsecutive * (time / (x.timePerBallon * x.ballonConsecutive + x.timeTired));
	LL rem = time % (x.timePerBallon * x.ballonConsecutive + x.timeTired);
	if (rem >= (x.timePerBallon * x.ballonConsecutive))
		result += x.ballonConsecutive;
	else
		result += rem / x.timePerBallon;

	return result;
}

bool good(int m, vector<Assistant> &h, int time) {
	LL result = 0;

	for (const auto &x : h) {
		result += blown(x, time);
	}

	return result >= m;
}

int main() {
	OPTIMIZAR_IO
	//PRESICION(20)
	LL m, n;
	cin >> m >> n;

	vector<Assistant> assistants(n);
	for (auto &x : assistants) {
		cin >> x.timePerBallon >> x.ballonConsecutive >> x.timeTired;
	}

	LL begin = -1;
	LL end = 2e9 + 1;

	while (end > begin + 1) {
		LL pivot = (begin + end) / 2;
		if (good(m, assistants, pivot)) {
			end = pivot;
		} else {
			begin = pivot;
		}
	}

	cout << end << ENDL;
	for (int i = 0; i < n; i++) {
		if(i)cout << " ";

		LL x = blown(assistants[i], end);
		cout << min(m, x);
		m -= min(m, x);
	}
	cout << ENDL;

	return 0;
}

