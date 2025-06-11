from collections import defaultdict

# main
n, k = map(int, input().split())
seq = list(map(int, input().split()))

num_dict = defaultdict(int)
max_seq_len = 0

left = 0
right = 0

while right < n:
    prev_num = seq[left]
    curr_num = seq[right]

    if num_dict[curr_num] + 1 <= k:
        num_dict[curr_num] += 1
        right += 1
    else:
        num_dict[prev_num] -= 1
        left += 1

    max_seq_len = max(max_seq_len, right - left)

print(max_seq_len)
