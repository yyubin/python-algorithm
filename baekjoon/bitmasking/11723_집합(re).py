import sys
now = 0
for _ in range(int(sys.stdin.readline())):
    com = list(sys.stdin.readline().rstrip().split())
    if com[0] == "add":
        x = int(com[1])
        now |= (1 << (x-1))
    elif com[0] == "remove":
        x = int(com[1])
        now &= (~(1 << (x-1)))
    elif com[0] == "check":
        x = int(com[1])
        print(now >> (x-1) & 1)
    elif com[0] == "toggle":
        x = int(com[1])
        now ^= (1 << (x-1))
    elif com[0] == "all":
        now = (1 << 20) - 1
    else:
        now = 0

