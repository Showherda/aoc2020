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
		x, y=i, j
		a, b=p
		while 0<=x+a<n and 0<=y+b<m:
			x+=a
			y+=b
			if inp[x][y]=='L':
				break
			if inp[x][y]=='#':
				val+=1
				break
	return val
flag=1
ok=1
while ok:
	cng=[]
	if flag:
		for i in range(n):
			for j in range(m):
				if inp[i][j]=='L' and cnt(i, j)==0:
					cng.append((i, j))
		ok=len(cng)
		for i, j in cng:
			inp[i][j]='#'
	else:
		for i in range(n):
			for j in range(m):
				if inp[i][j]=='#' and cnt(i, j)>5:
					cng.append((i, j))
		ok=len(cng)
		for i, j in cng:
			inp[i][j]='L'
	flag=not flag
ans=0
for i in range(n):
	for j in range(m):
		if inp[i][j]=='#':
			ans+=1
print(ans)
