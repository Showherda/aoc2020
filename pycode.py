# import sys
# LI=lambda:list(map(int, sys.stdin.readline().split()))
# MI=lambda:map(int, sys.stdin.readline().split())
# SI=lambda:sys.stdin.readline().strip('\n')
# II=lambda:int(sys.stdin.readline())

import sys
from itertools import product
sys.stdin=open('input.txt')
inp=[list(v.strip('\n')) for v in sys.stdin.readlines()]
n=len(inp)
m=len(inp[0])
def cnt(i, j):
	global inp, n, m
	val=0
	for p in product([-1, 0, 1], repeat=2):
		a, b=p
		if 0<=i+a<n and 0<=j+b<m and inp[i+a][j+b]=='#':
			val+=1
	return val
flag=1
ok=1
while ok:
	ok=0
	cng=[]
	if flag:
		for i in range(n):
			for j in range(m):
				if inp[i][j]=='L' and cnt(i, j)==0:
					ok=1
					cng.append((i, j))
		for i, j in cng:
			inp[i][j]='#'
	else:
		for i in range(n):
			for j in range(m):
				if inp[i][j]=='#' and cnt(i, j)>4:
					ok=1
					cng.append((i, j))
		for i, j in cng:
			inp[i][j]='L'
	flag=not flag
ans=0
for i in range(n):
	for j in range(m):
		if inp[i][j]=='#':
			ans+=1
print(ans)