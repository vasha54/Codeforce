//CodeForce -A. Petya and Strings
// Tematica :String
// Idea Básica: Comparar dos string
#include <iostream>
#include <algorithm>
#include <bits/stdc++.h>

#define ENDL '\n'

using namespace std;

int main(){

    string A,B;

    while(cin>>A>>B){
        for(int i=0;i<A.size();i++) if('A'<=A[i] && A[i]<='Z') A[i]+=32;
        for(int i=0;i<B.size();i++) if('A'<=B[i] && B[i]<='Z') B[i]+=32;
        int cmp=strcmp(A.c_str(),B.c_str());

        if(cmp == 0) cout<<0<<ENDL;
        else if(cmp <0)cout<<-1<<ENDL;
        else cout<<1<<ENDL;
    }
    return 0;
}
