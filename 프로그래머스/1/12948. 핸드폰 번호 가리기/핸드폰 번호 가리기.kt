class Solution {
    fun solution(phone_number: String): String {
        val n = phone_number.length
        var answer = ""
        
        for (i in 1..n - 4) {
            answer += "*"
        }
        
        return answer + phone_number.substring(n - 4)
    }
}