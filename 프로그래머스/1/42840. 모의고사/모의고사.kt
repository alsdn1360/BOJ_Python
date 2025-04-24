class Solution {
    fun solution(answers: IntArray): IntArray {
        val answer = mutableListOf<Int>()
        
        val soopojaScore = mutableListOf(0, 0, 0)
        val soopojaPattern = arrayOf(
            intArrayOf(1, 2, 3, 4, 5),
            intArrayOf(2, 1, 2, 3, 2, 4, 2, 5),
            intArrayOf(3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
        )
        
        for ((i, a) in answers.withIndex()) {
            for ((j, p) in soopojaPattern.withIndex()) {
                if (a == p[i % p.size]) {
                    soopojaScore[j] += 1
                }
            }
        }
        
        val max_score = soopojaScore.maxOrNull()
        
        for ((i, score) in soopojaScore.withIndex()) {
            if (score == max_score) {
                answer.add(i + 1)
            }
        }
        
        return answer.sorted().toIntArray()
    }
}