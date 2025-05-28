#include <bits/stdc++.h>

using namespace std;

int vetor[10];
vector<int> vet(3,1);

deque<int> deq;

int main(){
    
    vet.push_back(5);
    
    for (int i = 0; i < 4; i++)
        cout << vet[i] << endl;

    
    /*
        DEQUE
        .push_front(valor) : Adiciona um valor no início do deque
        .front() : Retorna o primeiro valor do deque
        .popfront() : Remove o primeiro valor do deque


        VECTOR 
        .push_back(valor) : Adiciona um valor ao final do vetor
        .pop_back() : Remove o último valor do vetor
        .back() : Retorna o último valor do vetor
        .size() : Retorna o tamanho do vetor
        .clear() : Limpa o vetor
        .empty() : Verifica se o vetor está vazio

        .sort() : Ordena o vetor
        .reverse() : Inverte a ordem dos valores do vetor
        .find(valor) : Retorna o iterador para o valor desejado
        .search() : Busca um valor no vetor
        .search_n() : Busca um valor n vezes no vetor
        .count(valor) : Retorna a quantidade de vezes que o valor aparece no vetor
        .max_element() : Retorna o maior valor do vetor
        .min_element() : Retorna o menor valor do vetor
        .accumulate() : Retorna a soma dos valores do vetor
        .unique() : Remove os valores duplicados do vetor

        .copy() : Copia os valores do vetor
        .insert(posição, valor) : Insere um valor na posição desejada
        .erase(posição) : Remove o valor da posição desejada
        .assign(tamanho, valor) : Atribui um valor a todas as posições do vetor
        .resize(tamanho) : Redimensiona o vetor para o tamanho desejado
        .fill() : Preenche o vetor com um valor
    */
}