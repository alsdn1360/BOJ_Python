class Solution {
    fun solution(number: String, k: Int): String {
        val stack = ArrayDeque<Char>()
        var cnt = k
        
        for (num in number) {
            while (stack.isNotEmpty() && cnt > 0 && stack.last() < num) {
                stack.removeLast()
                cnt--
            }
            
            stack.addLast(num)
        }
        
        while (cnt > 0) {
            stack.removeLast()
            cnt--
        }
        
        return stack.joinToString("")
    }
}