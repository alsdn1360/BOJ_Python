import kotlin.math.abs

class Solution {
    private val MOVES = listOf(-1 to 0, 1 to 0, 0 to -1, 0 to 1)
    
    data class Point(val x: Int, val y: Int)
    
    fun inBound(nx: Int, ny: Int): Boolean {
        return (0 <= nx && nx < 5) && (0 <= ny && ny < 5)
    }
    
    fun checkManhattan(x1: Int, y1: Int, x2: Int, y2: Int): Boolean {
        if (abs(x1 - x2) + abs(y1 - y2) <= 2) {
            return true
        } else {
            return false
        }
    }
    
    fun bfs(i: Int, j: Int, place: Array<String>): Boolean {
        val queue = ArrayDeque<Point>()
        queue.add(Point(i, j))
        
        val visited = Array(5) {BooleanArray(5)}
        visited[i][j] = true
        
        while (queue.isNotEmpty()) {
            val (x, y) = queue.removeFirst()
            
            for ((dx, dy) in MOVES) {
                val nx = x + dx
                val ny = y + dy
                
                if (inBound(nx, ny) && !visited[nx][ny] && checkManhattan(i, j, nx, ny)) {
                    if (place[nx][ny] == 'P') {
                        return false
                    } else if (place[nx][ny] == 'X') {
                        continue
                    } else {
                        queue.add(Point(nx, ny))
                        visited[nx][ny] = true
                    }
                }
            }
        }
        
        return true
    }
    
    fun solution(places: Array<Array<String>>): IntArray {
        var answer = mutableListOf<Int>()
        
        for (place in places) {
            var isOk = true
            
            outer@ for (i in 0 until 5) {
                for (j in 0 until 5) {
                    if (place[i][j] == 'P') {
                        if (!bfs(i, j, place)) {
                            isOk = false
                            break@outer
                        }
                    }
                }
            }
            
            answer.add(if (isOk) 1 else 0)
        }
        
        return answer.toIntArray()
    }
}