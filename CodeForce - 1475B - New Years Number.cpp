 /**
 * Coderfoce - 1475B  - New Years Number 
 
  * Temática: Programación Dinamica + Coin Change
 * 
 * Idea: Dado un número N determinar si se puede representar
 * como una suma de x cantidad 2020 y z cantidad de 2021 es decir
 * se debe cumplir que:
 *      n = 2020X + 2021Z 
 * Donde:
 * X y Z son numeros naturales 
 *
 * Si enfocamos el problema como coin change donde las denominaciones 
 * de monedas son 2020 y 2021 podemos ver que el problema se basa saber
 * si el valor n se puede devolver usando billetes de denomicación
 * 2020 y 2021
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
#define MAX_N 1000010
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
    //WRITE_FILE
    int cases, n;
    bool possible[MAX_N];
    fill(possible,possible+MAX_N,false);
    possible[0] = true;
    for(int i=0;i<MAX_N;i++){
        if(!possible[i]) continue;
        if(i+2020 < MAX_N) possible[i+2020] = true;
        if(i+2021 < MAX_N) possible[i+2021] = true;
    }
    cin>>cases;
    while(cases --){
        cin>>n;       
        cout<<( possible[n] ? "YES" : "NO"  )<<ENDL;
    }
    return 0;
}

