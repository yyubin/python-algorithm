import sys
word = sys.stdin.readline().rstrip()
encrypted = sys.stdin.readline().rstrip()
key = []
for i in range(len(word)):
    key.append((ord(encrypted[i]) - ord(word[i])) + 64)

for i in range(len(key)):
    if key[i] < 65:
        key[i] += 26

s = ''
for i in range(1, len(key)+1):
    if len(key) % i != 0:
        continue
    if key[:i] * (len(key) // i) == key:
        s = key[:i]
        break

for i in s:
    print(chr(i), end="")
