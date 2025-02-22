def solution(board, moves):
    stack = []
    result = 0
    
    new_board = [list(row) for row in zip(*board)]
    
    for move in moves:
        picked_doll = 0
        
        for i in range(len(new_board[move - 1])):
            if new_board[move -1][i] != 0:
                picked_doll = new_board[move - 1].pop(i)
                break
                
        if stack and stack[-1] == picked_doll:
            stack.pop()
            result += 2
        elif picked_doll != 0:
            stack.append(picked_doll)
        
    return result