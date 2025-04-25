import kotlin.math.abs

class Solution {
    fun solution(n: Int, wires: Array<IntArray>): Int {
        var answer = mutableListOf<Int>()
        
        for (removedEdge in wires.indices) {
            val tree = mutableMapOf<Int, MutableList<Int>>().withDefault {mutableListOf()}
            
            for ((edge, wire) in wires.withIndex()) {
                if (removedEdge == edge) continue
                
                tree.getOrPut(wire[0]) {mutableListOf()}.add(wire[1])
                tree.getOrPut(wire[1]) {mutableListOf()}.add(wire[0])
            }
            
            val queue = ArrayDeque<Int>()
            queue.addLast(1)
            
            val visited = mutableSetOf<Int>()
            visited.add(1)
            
            var towerCnt = 1
            
            while (queue.isNotEmpty()) {
                val currTower = queue.removeFirst()
                
                for (adjTower in tree.getValue(currTower)) {
                    if (adjTower !in visited) {
                        queue.addLast(adjTower)
                        visited.add(adjTower)
                        towerCnt++
                    }
                }
            }
            
            answer.add(abs(n - 2 * towerCnt))
        }
        
        return answer.minOrNull() ?: 0
    }
}