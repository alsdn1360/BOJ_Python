class Solution {
    fun find(tree: IntArray, x: Int): Int {
        if (tree[x] == x) return x
        
        tree[x] = find(tree, tree[x])
        
        return tree[x]
    }
    
    fun union(tree: IntArray, rank: IntArray, x: Int, y: Int): Unit {
        val xroot = find(tree, x)
        val yroot = find(tree, y)
        
        if (rank[xroot] < rank[yroot]) {
            tree[xroot] = yroot
        } else if (rank[xroot] > rank[yroot]) {
            tree[yroot] = xroot
        } else {
            tree[yroot] = xroot
            rank[xroot]++
        }
    }
    
    fun solution(n: Int, costs: Array<IntArray>): Int {
        costs.sortBy({it[2]})
        
        val tree = IntArray(n) {it}
        val rank = IntArray(n) {0}
        
        var minCost = 0
        var edges = 0
        
        for (edge in costs) {
            if (edges == n - 1) break
            
            val x = find(tree, edge[0])
            val y = find(tree, edge[1])
            
            if (x != y) {
                union(tree, rank, x, y)
                minCost += edge[2]
                edges++
            }
        }
        
        return minCost
    }
}