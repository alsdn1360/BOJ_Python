class Solution {
    fun solution(clothes: Array<Array<String>>): Int {
        var answer = 1
        val closet = mutableMapOf<String, Int>()
        
        for ((cloth, category) in clothes) {
            closet[category] = closet.getOrDefault(category, 0) + 1
        }
        
        for (cnt in closet.values) {
            answer *= cnt + 1
        }
        
        return answer - 1
    }
}