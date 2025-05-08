class Solution {
    fun solution(n: Int): Long {
        if (n == 1) return 1
        else if (n == 2) return 2
        else {
            val dp = LongArray(n + 1)
            
            dp[1] = 1
            dp[2] = 2
            
            for (i in 3..n) {
                dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567
            }
            
            return dp[n]
        }
        
        return 0
    }
}