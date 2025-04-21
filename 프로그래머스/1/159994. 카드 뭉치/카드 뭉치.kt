import java.util.ArrayDeque

class Solution {
    fun solution(cards1: Array<String>, cards2: Array<String>, goal: Array<String>): String {
        val queue1 = ArrayDeque(cards1.toList())
        val queue2 = ArrayDeque(cards2.toList())
        val goal_queue = ArrayDeque(goal.toList())
        
        while (goal.isNotEmpty()) {
            val word = goal_queue.peekFirst()
            
            if (queue1.isNotEmpty() && queue1.peekFirst() == word) {
                queue1.removeFirst()
                goal_queue.removeFirst()
            }
            else if (queue2.isNotEmpty() && queue2.peekFirst() == word) {
                queue2.removeFirst()
                goal_queue.removeFirst()
            }
            else {
                break
            }
        }
        
        return if (goal_queue.isEmpty()) "Yes" else "No"
    }
}