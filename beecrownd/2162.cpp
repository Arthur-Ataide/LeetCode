#include <bits/stdc++.h>

using namespace std;

int n, atual, anterior;
bool isPico, picoAnt;



bool valida(){ //ant = 1; at = 1;
    if (anterior > atual) 
        isPico = 0;
    
    else if (anterior == atual){
        cout << 0 << endl;
        return 1;
    }
    else
        isPico = 1;

    anterior = atual;
    return 0;
}

int main(){
    cin >> n >> anterior >> atual; // n = 3; ant = 1; at = 1;
    if (valida()){ 
        return 0; 
    }
    n--;
    
    while (--n){
        picoAnt = isPico;
        cin >> atual;
        if (valida()){
            return 0;
        }
        
        if (isPico == picoAnt){
            cout << 0 << endl;
            return 0;
        }
    }

    cout << 1 << endl;
    return 0;
}