class Solution {
    fun solution(arr: IntArray): IntArray {
        var answer = mutableListOf<Int>()
        val min_num = arr.minOrNull()
        
        for (num in arr) {
            if (num != min_num) {
                answer.add(num)
            }
        }
        
        return if (answer.isEmpty()) intArrayOf(-1) else answer.toIntArray()
    }
}