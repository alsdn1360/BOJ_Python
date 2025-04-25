class Solution {
    fun dfs(numbers: IntArray, target: Int, idx: Int, total: Int): Int {
        if (idx == numbers.size) {
            if (total == target) return 1 else return 0
        }
        
        return dfs(numbers, target, idx + 1, total + numbers[idx]) + dfs(numbers, target, idx + 1, total - numbers[idx])
    }
    
    
    fun solution(numbers: IntArray, target: Int): Int {
        return dfs(numbers, target, 0, 0)
    }
}