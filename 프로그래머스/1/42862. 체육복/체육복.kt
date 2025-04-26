class Solution {
    fun solution(n: Int, lost: IntArray, reserve: IntArray): Int {
        val student = IntArray(n + 1) {1}
        student[0] = 0
        
        for (l in lost) student[l]--
        for (r in reserve) student[r]++

        for (i in 1..n) {
            if (student[i] <= 1) continue
            
            if (i > 1 && student[i - 1] == 0) {
                student[i]--
                student[i - 1]++
            }
            else if (i < n && student[i + 1] == 0) {
                student[i]--
                student[i + 1]++
            }
        }
        
        return student.count {it > 0}
    }
}