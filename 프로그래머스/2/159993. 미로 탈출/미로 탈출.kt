import java.util.ArrayDeque

class Solution {
    private val MOVES = listOf(0 to -1, 0 to 1, -1 to 0, 1 to 0)
    
    data class Node(val x: Int, val y: Int, val step: Int)
    
    fun inBound(n: Int, m: Int, nx: Int, ny: Int): Boolean {
        return nx in 0 until n && ny in 0 until m
    }
    
    fun bfs(maps: Array<String>, start: Pair<Int, Int>, target: Char): Int {
        val n = maps.size
        val m = maps[0].length
        
        val queue = ArrayDeque<Node>()
        queue.add(Node(start.first, start.second, 0))
        
        val visited = Array(n) {BooleanArray(m)}
        visited[start.first][start.second] = true
        
        while (queue.isNotEmpty()) {
            val (x, y, step) = queue.removeFirst()
            
            if (maps[x][y] == target) return step
            
            for ((dx, dy) in MOVES) {
                val nx = x + dx
                val ny = y + dy
                
                if (inBound(n, m, nx, ny) && maps[nx][ny] != 'X' && !visited[nx][ny]) {
                    queue.add(Node(nx, ny, step + 1))
                    visited[nx][ny] = true
                }
            }
        }
        
        return -1
    }
    
    fun solution(maps: Array<String>): Int {
        var start: Pair<Int, Int>? = null
        var lever: Pair<Int, Int>? = null
        
        for (i in maps.indices) {
            for (j in maps[i].indices) {
                when (maps[i][j]) {
                    'S' -> start = i to j
                    'L' -> lever = i to j
                }
            }
        }
        
        val stepToLever = bfs(maps, start!!, 'L')
        if (stepToLever == -1) return -1
        
        val stepToExit = bfs(maps, lever!!, 'E')
        if (stepToExit == -1) return -1
        
        return stepToLever + stepToExit
    }
}