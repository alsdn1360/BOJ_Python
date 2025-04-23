import java.util.ArrayDeque

class Solution {
    fun solution(priorities: IntArray, location: Int): Int {
        var answer = 1
        val queue = ArrayDeque<Pair<Int, Int>>()
        
        for ((i, p) in priorities.withIndex()) {
            queue.add(Pair(i, p))
        }
        
        while (queue.isNotEmpty()) {
            val (l, p) = queue.removeFirst()
            val maxP = queue.maxOfOrNull {it.second} ?: 0
            
            if (p < maxP) {
                queue.add(Pair(l, p))
            } else {
                if (l == location) {
                    return answer
                }
                
                answer++
            }
        }
        
        error("종료")
    }
}