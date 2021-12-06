def blackjack():
    _, bj = map(int, input().split())
    card = list(map(int, input().split()))
    idx = len(card)
    sums = 0

    for i in range(idx-2):
        for j in range(i+1, idx-1):
            for k in range(j+1, idx):
                if (card[i] + card[j] + card[k]) > bj:
                    continue
                else: sums = max(sums, card[i] + card[j] + card[k])
    return sums

if __name__ == "__main__":
    print(blackjack())