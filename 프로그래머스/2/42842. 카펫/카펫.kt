import kotlin.math.sqrt

class Solution {
    fun solution(brown: Int, yellow: Int): IntArray {
        val area = brown + yellow
        val maxH = sqrt(area.toDouble()).toInt()
        
        for (h in 3..maxH) {
            if (area % h != 0) continue
            
            val w = area / h
            
            if (2 * (w + h) - 4 == brown && (w - 2) * (h - 2) == yellow) {
                return intArrayOf(w, h)
            }
        }
        
        error("종료")
    }
}