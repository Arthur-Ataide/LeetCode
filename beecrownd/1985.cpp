#include <bits/stdc++.h>

using namespace std;

int main(){
    int q, num, x;
    double cont = 0;
    cin >> q;
    
    for (int i = 0; i < q; i++){
        cin >> num >> x;
        
        cont += (num-1000+0.5)*x;
    }

    cout <<fixed<< setprecision(2);
    cout << cont << endl;
    return 0;
}