def solution(sequence):
    n = len(sequence)
    
    pulse_seq1 = []
    pulse_seq2 = []
    
    pulse = 1
    
    for num in sequence:
        pulse_seq1.append(num * pulse)
        pulse *= -1
        pulse_seq2.append(num * pulse)

    prefix_sum1 = [0] * (n + 1)
    prefix_sum2 = [0] * (n + 1)
    
    for i in range(1, n + 1):
        prefix_sum1[i] = prefix_sum1[i - 1] + pulse_seq1[i - 1]
        prefix_sum2[i] = prefix_sum2[i - 1] + pulse_seq2[i - 1]
        
    pulse_sum1 = max(prefix_sum1) - min(prefix_sum1)
    pulse_sum2 = max(prefix_sum2) - min(prefix_sum2)
    
    return max(pulse_sum1, pulse_sum2)