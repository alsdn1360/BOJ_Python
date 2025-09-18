import sys

input = sys.stdin.readline


# main
n = int(input())
words = [input().rstrip() for _ in range(n)]

cycle_words = []

for word in words:
    is_new = True

    if cycle_words:
        for cycle_word in cycle_words:
            if word in (cycle_word * 2) and len(word) == len(cycle_word):
                is_new = False
                break

    if is_new:
        cycle_words.append(word)

print(len(cycle_words))
