import sys
sys.stdin=open('input.txt')
t=int(input())
inp=[]
for v in sys.stdin.readline().split(','):
	if v!='x':
		inp.append(int(v))
# inp=set(v.strip('\n') for v in sys.stdin.readline().split(','))
# inp.remove('x')
# inp=[int(v) for v in inp]
# print(inp)
from math import ceil
d=10000000000
for v in inp:
	ct=ceil(t/v)*v
	cd=ct-t
	if cd<d:
		d=cd
		ans=cd*v
print(ans)