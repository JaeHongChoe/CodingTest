import sys

num1, num2 = map(int, input().split())
n,m=[],[]
for _ in range(num1):
    n_1, n_2 = map(int, input().split())
    n.extend(n_2 for _ in range(n_1))
for _ in range(num2):
    m_1, m_2 = map(int, input().split())
    m.extend(m_2 for _ in range(m_1))

ans=[]
for i in range(100):
    ans.append(m[i]-n[i])

if max(ans) <0:
    print(0)
else:
    print(max(ans))
