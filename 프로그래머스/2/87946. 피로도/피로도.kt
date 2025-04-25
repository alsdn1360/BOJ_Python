class Solution {
    fun dfs(k: Int, dungeons: Array<IntArray>, visited: BooleanArray, cnt: Int): Int {
        var maxCnt = cnt
        
        for ((i, dungeon) in dungeons.withIndex()) {
            val minFati = dungeon[0]
            val useFati = dungeon[1]
            
            if (!visited[i] && k >= minFati) {
                visited[i] = true
                
                maxCnt = maxOf(maxCnt, dfs(k - useFati, dungeons, visited, cnt + 1))
                
                visited[i] = false
            }
        }
        
        return maxCnt
    }
    
    fun solution(k: Int, dungeons: Array<IntArray>): Int {
        val visited = BooleanArray(dungeons.size)
        
        return dfs(k, dungeons, visited, 0)
    }
}