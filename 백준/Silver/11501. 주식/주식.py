# main
t = int(input())

for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))

    total = 0
    curr_price = prices[n - 1]

    for price in reversed(prices):
        if price > curr_price:
            curr_price = price
        else:
            total += curr_price - price

    print(total)
