import java.util.ArrayDeque
import kotlin.math.ceil

class Solution {
    fun solution(progresses: IntArray, speeds: IntArray): IntArray {
        val answer = mutableListOf<Int>()
        val queue = ArrayDeque<Int>()
        var preFeat = 0
        var deployFeat = 0
        
        for (i in 0 until progresses.size) {
            val remainProgress = 100 - progresses[i]
            val deployDay = ceil(remainProgress / speeds[i].toDouble()).toInt()
            queue.add(deployDay)
        }
        
        while (queue.isNotEmpty()) {
            val feat = queue.removeFirst()
            
            if (feat > preFeat) {
                if (deployFeat != 0) {
                    answer.add(deployFeat)
                }
                
                preFeat = feat
                deployFeat = 1
            } else {
                deployFeat += 1
            }
        }
        
        answer.add(deployFeat)
        
        return answer.toIntArray()
    }
}