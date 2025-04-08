import sys
def is_palindrome(s):
    return s == s[::-1]

def shortest(s):
    n = len(s)
    for i in range(n):
        if is_palindrome(s[i:]):
            return n+i
    return 2 * n

s = sys.stdin.readline().rstrip()
print(shortest(s))