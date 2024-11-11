import sys
s = sys.stdin.readline().rstrip()
for i in range((len(s)//10)+1):
    if i == (len(s)//10):
        print(s[i*10:])
    else:
        print(s[i*10:i*10+10])
