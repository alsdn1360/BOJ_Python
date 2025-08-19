import sys

input = sys.stdin.readline

# main
n, m = map(int, input().split())

dna = []

for _ in range(n):
    dna.append(input())

s = ""
h_d = 0

for i in range(m):
    nucleotide = {"A": 0, "C": 0, "G": 0, "T": 0}

    for j in range(n):
        nucleotide[dna[j][i]] += 1

    sorted_nucleotide = sorted(nucleotide.items(), key=lambda x: (-x[1], x[0]))

    s += sorted_nucleotide[0][0]

    for nuc, c in sorted_nucleotide[1:]:
        if c != 0:
            h_d += c

print(s)
print(h_d)
