class Solution {
    fun solution(numbers: IntArray): Int {
        var answer = 0
        
        for (i in 0..9) {
            if (i !in numbers) {
                answer += i
            }
        }
        
        return answer
    }
}