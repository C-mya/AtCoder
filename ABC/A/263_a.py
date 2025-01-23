card = list(map(int, input().split(" ")))
card.sort()
ans = "No"

if len(set(card)) == 2:
    if card.count(card[0]) == 2 or card.count(card[0]) == 3:
        ans = "Yes"

print(ans)
