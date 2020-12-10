import sys
sys.stdin=open('input.txt')
inp=[int(v) for v in sys.stdin.readlines()]
l, r=-1, 23
for i in range(25, len(inp)):
	l+=1
	r+=1
	ok=0
	for j in range(l, r+1):
		for k in range(l, r+1):
			if j!=k and inp[j]+inp[k]==inp[i]:
				ok=1
				break
	if not ok:
		print(inp[i])
