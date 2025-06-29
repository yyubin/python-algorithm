import sys
from collections import Counter, defaultdict

T = int(sys.stdin.readline())

for _ in range(T):
    cards = sys.stdin.readline().split()
    counter = Counter(cards)

    if any(v >= 3 for v in counter.values()):
        print(":)")
        continue

    if sum(1 for v in counter.values() if v >= 2) >= 2:
        print(":)")
        continue

    suit_map = defaultdict(list)
    for card in cards:
        num, suit = int(card[0]), card[1]
        suit_map[suit].append(num)

    found = False
    for suit in suit_map:
        num_counter = Counter(suit_map[suit])
        nums = sorted(num_counter.keys())
        for i in range(len(nums) - 2):
            if (nums[i+1] == nums[i] + 1 and
                nums[i+2] == nums[i] + 2):
                found = True
                break
        if found:
            break

    print(":)" if found else ":(")