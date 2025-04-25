class Solution {
    data class Point(val word: String, val step: Int)
    
    fun isDiffOne(word1: String, word2: String): Boolean {
        var cnt = 0
        
        for ((a, b) in word1.zip(word2)) {
            if (a == b) continue
            
            cnt++
            
            if (cnt > 1) return false
        }
        
        return true
    }
    
    fun solution(begin: String, target: String, words: Array<String>): Int {
        if (target !in words) return 0

        val queue = ArrayDeque<Point>()
        val visited = mutableSetOf<String>()
        
        queue.addLast(Point(begin, 0))
        visited.add(begin)
        
        while (queue.isNotEmpty()) {
            val (word, step) = queue.removeFirst()
            
            if (word == target) return step
            
            for (diffWord in words) {
                if (diffWord !in visited && isDiffOne(word, diffWord)) {
                    queue.addLast(Point(diffWord, step + 1))
                    visited.add(diffWord)
                }
            }
        }
        
        error("종료")
    }
}