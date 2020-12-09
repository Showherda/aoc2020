import sys
sys.stdin=open('input.txt')
inp=sys.stdin.readlines()
l, r=-1, 23
for i in range(25, len(inp)):
	l+=1
	r+=1
	ok=0
	for j in range(l, r+1):
		for k in range(l, r+1):
			if j!=k and int(inp[j])+int(inp[k])==int(inp[i]):
				ok=1
				break
	if not ok:
		print(inp[i])
