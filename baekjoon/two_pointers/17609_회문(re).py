import sys
for i in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().rstrip()
    if s == s[::-1]:
        print(0)
    else:
        s_left = list(s)
        s_right = list(s)

        for j in range(len(s)//2):
            if s[j] != s[-(j+1)]:
                s_left.pop(j)
                s_right.pop(-(j+1))
                if s_left == s_left[::-1]:
                    print(1)
                elif s_right == s_right[::-1]:
                    print(1)
                else:
                    print(2)
                break