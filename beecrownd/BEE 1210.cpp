#include <bits/stdc++.h>

using namespace std;

int n, i, m, p;
int manu[2010], venda[2010];

pair<int, vector<int>> dp[2010][2010];
bool dp2[2010][2010];

pair<int, vector<int>> solve(int pos, int idade) {
  if (pos == n)
    return {0, {}};

  if (dp2[pos][idade]) {
    return dp[pos][idade];
  }

  pair<int, vector<int>> vende, nao_vende;

  vende = solve(pos + 1, 0);
  vende.first += p - venda[idade] + manu[idade];
  vende.second.push_back(pos+1);

    cout << vende.second.size() << endl;
  if (idade == m) {
    dp2[pos][idade] = true;
    return dp[pos][idade] = vende;
  }
  nao_vende = solve(pos + 1, idade + 1);
  nao_vende.first += manu[idade];

  if (vende.first <= nao_vende.first) {
    dp2[pos][idade] = true;
    return dp[pos][idade] = vende;
  }
  dp2[pos][idade] = true;
  return dp[pos][idade] = nao_vende;
}

int main() {

  while (cin >> n >> i >> m >> p) {
    memset(dp2, 0, sizeof dp2);
    for (int i = 0; i < m; i++) {
      cin >> manu[i];
    }

    for (int i = 1; i <= m; i++) {
      cin >> venda[i];
    }

    auto sol = solve(0, i);
    cout << sol.first << endl;

    for (int i = 0; i < sol.second.size(); i++) {
      cout << i << " --> " << sol.second[i] << endl;
    }

    cout << endl;
  }
  return 0;
}