class Solution {
    fun solution(a: Int, b: Int, n: Int): Int {
        var answer = 0
        var n = n
        
        while (n >= a) {
            val exchange = (n / a) * b
            
            answer += exchange
            n = (n % a) + exchange
        }
        
        return answer
    }
}