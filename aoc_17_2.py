from itertools import product
inp=[v.strip('\n') for v in open('input.txt')]
n=len(inp[0])
active=set()
for i in range(n):
	for j in range(n):
		if inp[i][j]=='#':
			active.add((i, j, 0, 0))
for _ in range(6):
	cnt={}
	for a, b, c, d in active:
		cnt[(a, b, c, d)]=cnt.get((a, b, c, d), 0)
		for x, y, z, w in product([-1, 0, 1], repeat=4):
			if x==y==z==w==0:
				continue
			cnt[(a+x, b+y, c+z, d+w)]=cnt.get((a+x, b+y, c+z, d+w), 0)+1
	tmpa=set()
	tmpia=set()
	for v in cnt:
		if v in active and not 2<=cnt[v]<=3:
			tmpia.add(v)
		if v not in active and cnt[v]==3:
			tmpa.add(v)
	active=active.difference(tmpia)
	active=active.union(tmpa)
print(len(active))
