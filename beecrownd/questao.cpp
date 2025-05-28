#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    while(cin >> n){
        if(n < 0){
            cout << "NO\n";
            continue;
        }
        int menor = 0;
        int maior = sqrt(n);
        
        bool menor_acao = true;
        bool encontrado = false;

        while(maior >= 0 || maior >= menor){
            if(maior * maior + menor * menor == n){
                cout << "YES\n";
                encontrado = true;
                break;
            }

            if(menor_acao && maior * maior + menor * menor < n)
                menor++;

            if(maior * maior + menor * menor > n)
                maior--;
        }

        if(!encontrado)
            cout << "NO\n";
    }
    return 0;
}