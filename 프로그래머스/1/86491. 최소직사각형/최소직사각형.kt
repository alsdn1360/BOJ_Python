class Solution {
    fun solution(sizes: Array<IntArray>): Int {
        val rSizes = MutableList(2) { mutableListOf<Int>() }
        
        for (i in 0 until sizes.size) {
            if (sizes[i][0] > sizes[i][1]) {
                rSizes[0].add(sizes[i][1])
                rSizes[1].add(sizes[i][0])
            }
            else {
                rSizes[0].add(sizes[i][0])
                rSizes[1].add(sizes[i][1])
            }
        }
        
        return rSizes[0].maxOrNull()!! * rSizes[1].maxOrNull()!!
    }
}