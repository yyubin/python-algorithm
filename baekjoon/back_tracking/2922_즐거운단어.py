import sys
import string
vowel = {'A', 'I', 'O', 'U', 'E'}
consonant = set(string.ascii_uppercase) - vowel
st = sys.stdin.readline().rstrip()
ans = 0

def chk(s):
    if 'L' not in s:
        return False
    for i in range(len(st)-2):
        if (s[i] in vowel) and (s[i+1] in vowel) and (s[i+2] in vowel):
            return False
        if (s[i] in consonant) and (s[i+1] in consonant) and (s[i+2] in consonant):
            return False
    return True

def bt(now, idx, ch):
    global ans
    if '_' not in now:
        if chk(now):
            tmp = 1
            for y in ch:
                if y == 'A':
                    tmp *= 5
                elif y == 'B':
                    tmp *= 20
            ans += tmp
        return
    for i in range(idx, len(now)):
        if now[i] == '_':
            now = now[:i] + 'A' + now[i+1:]
            bt(now, idx+1, ch+'A')
            now = now[:i] + 'B' + now[i+1:]
            bt(now, idx+1, ch+'B')
            now = now[:i] + 'L' + now[i+1:]
            bt(now, idx+1, ch+'L')
            return

for i in range(len(st)):
    if st[i] == '_':
        bt(st, i, '')
        break
else:
    print(1)
print(ans)

# 생각이 안남
# https://baby-ohgu.tistory.com/9