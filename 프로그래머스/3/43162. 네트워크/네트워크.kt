class Solution {
    fun solution(n: Int, computers: Array<IntArray>): Int {
        var answer = 0
        
        val network = mutableMapOf<Int, MutableList<Int>>()
        val visited = mutableSetOf<Int>()
        
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (computers[i][j] != 1) continue
                
                network.getOrPut(i) {mutableListOf()}.add(j)
            }
        }
        
        fun dfs(curr_com: Int): Unit {
            visited.add(curr_com)
            
            for (adj_com in network.getValue(curr_com)) {
                if (adj_com !in visited) {
                    dfs(adj_com)
                }
            }
        }
        
        for (com in 0 until n) {
            if (com !in visited) {
                dfs(com)
                answer++
            }
        }
        
        return answer
    }
}