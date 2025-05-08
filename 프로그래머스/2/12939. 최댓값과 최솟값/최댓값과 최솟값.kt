class Solution {
    fun solution(s: String): String {
        var answer = ""
        
        val arr = s.split(" ").map {it.toInt()}.toIntArray()
        
        arr.sort()
        
        val min = arr.first().toString()
        val max = arr.last().toString()
        
        answer = min + " " + max
        
        return answer
    }
}