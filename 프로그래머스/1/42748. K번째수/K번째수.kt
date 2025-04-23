class Solution {
    fun solution(array: IntArray, commands: Array<IntArray>): IntArray {
        var answer = mutableListOf<Int>()
        
        for ((i, j, k) in commands) {
            val tempArr = array.slice(i - 1..j - 1).sorted()
            answer.add(tempArr[k - 1])
        }
        
        return answer.toIntArray()
    }
}