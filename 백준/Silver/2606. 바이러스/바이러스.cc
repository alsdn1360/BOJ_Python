#include <iostream>
#include <queue>

using namespace std;

queue<int> check;
int visit[101] = {0,};
int computer[101][101];

int BFS(int N) {
    int ans = 0, i;

    check.push(1);
    visit[1] = 1;

    while (!check.empty()) {
        int temp = check.front();
        check.pop();
        ans++;

        for (i = 1; i <= N; i++) {
            if (computer[temp][i] == 1 && visit[i] == 0) {
                visit[i] = 1;
                check.push(i);
            }
        }
    }

    return ans;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, network, i, x, y;

    cin >> N >> network;

    for (i = 0; i < network; i++) {
        cin >> x >> y;
        computer[x][y] = computer[y][x] = 1;
    }

    cout << BFS(N) - 1;

    return 0;
}