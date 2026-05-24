/**
 * Codeforces - 1374B - Multiply by 2, divide by 6
 * Temática: Aritmética - Factorización
 * 
 * Idea: El número n se puede descomponer en factores primos 2^a * 3^b * c.
 * Solo se puede multiplicar por 2 (aumenta a) o dividir por 6 (reduce a y b en 1).
 * Para llegar a 1 se requiere que c=1 y que tras k multiplicaciones por 2 y m divisiones por 6
 * se tenga a + k - m = 0  y  b - m = 0  →  m = b, k = b - a. Luego k ≥ 0 ⇒ b ≥ a.
 * El número mínimo de movimientos es k + m = 2b - a.
 * Si c != 1 o b < a, es imposible (-1).
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

signed main()
{
    OPTIMIZAR_IO
    //PRESICION(2)
    READ_FILE
    //WRITE_FILE

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        if (n == 1) {
            cout << 0 << ENDL;
            continue;
        }
        int cnt2 = 0, cnt3 = 0;
        int temp = n;
        while (temp % 2 == 0) {
            temp /= 2;
            cnt2++;
        }
        while (temp % 3 == 0) {
            temp /= 3;
            cnt3++;
        }
        if (temp != 1 || cnt3 < cnt2) {
            cout << -1 << ENDL;
        } else {
            cout << 2 * cnt3 - cnt2 << ENDL;
        }
    }

    return 0;
}