import sys
# LI=lambda:list(map(int, sys.stdin.readline().split()))
# MI=lambda:map(int, sys.stdin.readline().split())
# SI=lambda:sys.stdin.readline().strip('\n')
# II=lambda:int(sys.stdin.readline())
sys.stdin=open('input.txt')
sys.stdout=open('output.txt', 'w')
inp=sys.stdin.readlines()
n=len(inp)
for j in range(n):
	ok=0
	if inp[j][:3]=='jmp':
		ok=1
		tmp=list(inp[j])
		tmp[0]='n'
		tmp[1]='o'
		inp[j]=''.join(tmp)
	acc=i=0
	done=set()
	while True:
		if i<0:
			i=0
		elif i>=n:
			i=n-1
		if i in done:
			break
		done.add(i)
		if inp[i][:3]=='nop':
			i+=1
		elif inp[i][:3]=='jmp':
			i+=int(inp[i][4:])
		else:
			acc+=int(inp[i][4:])
			i+=1
	if n-1 in done:
		print(acc)
	if ok:
		tmp[0]='j'
		tmp[1]='m'
		inp[j]=''.join(tmp)