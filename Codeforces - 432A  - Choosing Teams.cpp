 /**
 * Codeforces - 432A  - Choosing Teams
 * Temática: Búsqueda 
 * 
 * Idea: Dado un grupo de estudiantes de los cuales se conoce la cantidad
 * previa de participaciones en ICPC previos se quiere saber la cantidad
 * de equipos que se pueden formar con la condición de los equipos formados
 * participen al menos k veces en ICPC integramente sin cambios en los
 * integrantes y conociendo que un estudiante solo puede participar 5 veces
 * en el ICPC.
 * Para solucionar el problema basta con contar la cantidad de estudiantes 
 * que la cantidad de oportunidades que le queda por participar en ICPC sea
 * igual o mayor que k. Con dicha cantidad basta con dividirla entre 3 (
 * solo nos interesa la parte entera) y tendremos la cantidad de equipos
 * que se puede conformar.
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
#define MAX_N 100010
#define MOD  1000000007
 
using namespace std;
using namespace __gnu_pbds;

signed main()
{
    OPTIMIZAR_IO
    //PRESICION(2)
    READ_FILE
    //WRITE_FILE
    int nstudents, k, selects=0, participated ;
    cin>>nstudents>>k;
    for(int i=1;i<=nstudents;i++){
        cin>>participated;
        if(5-participated >=k)
            selects++;
    }
    cout<<selects/3<<ENDL;

    return 0;
}

