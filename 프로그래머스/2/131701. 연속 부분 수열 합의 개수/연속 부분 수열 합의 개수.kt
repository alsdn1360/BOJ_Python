class Solution {
    fun solution(elements: IntArray): Int {
        val answer = mutableSetOf<Int>()
        
        val n = elements.size
        val extended = elements + elements
        
        val prefix = IntArray(2 * n + 1)
        
        for (i in 0 until 2 * n) {
            prefix[i + 1] = prefix[i] + extended[i]
        }
        
        for (i in 0 until n) {
            for (len in 1..n) {
                answer.add(prefix[i + len] - prefix[i])
            }
        }
        
        return answer.size
    }
}