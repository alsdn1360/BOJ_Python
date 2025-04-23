class Solution {
    fun solution(citations: IntArray): Int {
        var hIndex = 0
        
        for (h in 0..citations.size) {
            val cnt = citations.count {it >= h} 
            if (cnt >= h) hIndex = maxOf(hIndex, h)
        }
        
        return hIndex
    }
}