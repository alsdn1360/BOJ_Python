class Solution {
    fun solution(tickets: Array<Array<String>>): Array<String> {
        var answer = mutableListOf<String>()
        val sortedTickets = tickets.sortedWith(compareBy({it[0]}, {it[1]}))
        val n = sortedTickets.size
        val usedTickets = BooleanArray(n)
        
        fun dfs(route: MutableList<String>): Boolean {
            if (route.size == n + 1) {
                answer.addAll(route)
                return true
            }
            
            for (i in 0 until n) {
                if (route.last() == sortedTickets[i][0] && !usedTickets[i]) {
                    usedTickets[i] = true
                    route.add(sortedTickets[i][1])
                    
                    if (dfs(route)) return true
                    
                    route.removeAt(route.size - 1)
                    usedTickets[i] = false
                }
            }
            
            return false
        }
        
        dfs(mutableListOf("ICN"))
        
        return answer.toTypedArray()
    }
}