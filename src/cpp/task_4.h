#include <iostream>
#include <vector>

using namespace std;

int dfs(int node, int parent, int target, vector<vector<int>>& graph) {
    if (node == target) {
        return 0;
    }
    
    for (int neighbor : graph[node]) {
        if (neighbor != parent) {
            int distance = dfs(neighbor, node, target, graph);
            if (distance >= 0) {
                return distance + 1;
            }
        }
    }
    
    return -1;
}

int main() {
    int n, x;
    cin >> n >> x;
    
    vector<vector<int>> graph(n+1);
    
    for (int i = 0; i < n-1; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    
    int distance = dfs(1, 0, x, graph);
    
    cout << distance * 2 << endl;
    
    return 0;
}
