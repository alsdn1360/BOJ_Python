class Solution {
    fun solution(genres: Array<String>, plays: IntArray): IntArray {
        val answer = mutableListOf<Int>()
        val album = mutableMapOf<String, MutableList<Pair<Int, Int>>>()
        val totalPlays = mutableMapOf<String, Int>()
        
        for ((i, genre) in genres.withIndex()) {
            album.getOrPut(genre) {mutableListOf()}.add(i to plays[i])
            totalPlays[genre] = totalPlays.getOrDefault(genre, 0) + plays[i]
        }
        
        val sortedGenres = totalPlays.entries.sortedByDescending {it.value}.map {it.key}
        
        for (genre in sortedGenres) {
            val sortedAlbum = album[genre]!!.sortedWith(compareByDescending<Pair<Int, Int>> {it.second}.thenBy {it.first})
            answer += sortedAlbum.take(2).map {it.first}
        }
        
        return answer.toIntArray()
    }
}