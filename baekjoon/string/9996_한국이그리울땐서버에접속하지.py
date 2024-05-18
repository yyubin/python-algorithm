import sys
n = int(sys.stdin.readline())
pattern = list(sys.stdin.readline().rstrip().split('*'))
st, ed = pattern[0], pattern[-1]

for _ in range(n):
    string = sys.stdin.readline().rstrip()
    if len(string) < len(st) + len(ed):
        print("NE")
        continue

    if string[:len(st)] == st and string[-len(ed):] == ed:
        print("DA")
    else:
        print("NE")


