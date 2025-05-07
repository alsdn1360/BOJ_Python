class Solution {
    fun solution(elements: IntArray): Int {
        val answer = mutableSetOf<Int>()
        val n = elements.size
        
        for (len in 1..n) {
            for (i in 0 until n) {
                var sum = 0
                
                for (j in i until (i + len)) {
                    sum += elements[j % n]
                }
                
                answer.add(sum)
            }   
        }
        
        return answer.size
    }
}