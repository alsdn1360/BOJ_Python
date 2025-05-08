class Solution {
    fun solution(queue1: IntArray, queue2: IntArray): Int {
        var answer = 0
        
        val deque1 = ArrayDeque(queue1.toList())
        val deque2 = ArrayDeque(queue2.toList())
        
        // 매번 sum() 함수를 사용하지 않기 위해 별도의 합을 변수로 초기화
        var sumDeque1 = deque1.sumOf {it.toLong()}
        var sumDeque2 = deque2.sumOf {it.toLong()}
        
        val total = sumDeque1 + sumDeque2
        
        // 총합이 홀수면 소수가 나오기 때문에 불가능
        if (total.toInt() % 2 != 0) return -1
        
        // 큰 큐에서 하나 빼서 작은 큐로 넣기 반복
        while (sumDeque1 != (total / 2)) {
            // 작업 횟수가 큐 크기의 3배가 되면 더 이상 만들 수 없음
            if (answer > queue1.size * 3) return -1
            
            if (sumDeque1 > sumDeque2) {
                val currNum = deque1.removeFirst().toLong()
                
                sumDeque1 -= currNum
                sumDeque2 += currNum
                
                deque2.add(currNum.toInt())
            } else {
                val currNum = deque2.removeFirst().toLong()
                
                sumDeque1 += currNum
                sumDeque2 -= currNum
                
                deque1.add(currNum.toInt())
            }
            
            answer++
        }
        
        return answer
    }
}