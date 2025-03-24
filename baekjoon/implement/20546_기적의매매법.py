import sys
money = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

s_buy, m_buy = [], []
s_money, m_money = money, money
stack = []

for i, v in enumerate(li):
    if s_money >= v:
        s_buy.append((s_money // v, v))
        s_money %= v

    if m_money >= v and i > 2 and li[i-3] > li[i-2] > li[i-1]:
        m_buy.append((m_money // v, v))
        m_money %= v

    if i > 2 and li[i-3] < li[i-2] < li[i-1]:
        for i in m_buy:
            m_money += i[0] * v
        m_buy = []

for i in s_buy:
    s_money += i[0] * li[-1]

for i in m_buy:
    m_money += i[0] * li[-1]

if s_money > m_money:
    print("BNP")
elif s_money < m_money:
    print("TIMING")
else:
    print("SAMESAME")


