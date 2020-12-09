import sys
# LI=lambda:list(map(int, sys.stdin.readline().split()))
# MI=lambda:map(int, sys.stdin.readline().split())
# SI=lambda:sys.stdin.readline().strip('\n')
# II=lambda:int(sys.stdin.readline())
sys.stdin=open('input.txt')
# sys.stdout=open('output.txt', 'w')
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