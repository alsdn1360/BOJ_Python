import kotlin.math.sqrt

class Solution {
    fun makePermutation(char: List<Char>): Set<Int> {
        val result = mutableSetOf<Int>()
        
        fun permute(prefix: String, remain: String) {
            if (prefix.isNotEmpty()) result.add(prefix.toInt())
            
            for (i in remain.indices) {
                permute(prefix + remain[i], remain.removeRange(i, i + 1))
            }
        }
        
        permute("", char.joinToString(""))
        
        return result
    }
    
    fun isPrime(num: Int): Boolean {
        if (num < 2) return false
        
        for (i in 2..sqrt(num.toDouble()).toInt()) {
            if (num % i == 0) return false
        }
        
        return true
    }
    
    fun solution(numbers: String): Int {
        val answer = makePermutation(numbers.toList())
        
        return answer.count {isPrime(it)}
    }
}