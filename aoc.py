import sys
# LI=lambda:list(map(int, sys.stdin.readline().split()))
# MI=lambda:map(int, sys.stdin.readline().split())
# SI=lambda:sys.stdin.readline().strip('\n')
# II=lambda:int(sys.stdin.readline())
sys.stdin=open('input.txt')
# sys.stdout=open('output.txt', 'w')
inp=sorted([int(v) for v in sys.stdin.readlines()])
# n=len(inp)
one, three=1, 1
for i in range(1, len(inp)):
	if inp[i]-inp[i-1]==1:
		one+=1
	if inp[i]-inp[i-1]==3:
		three+=1
print(one*three)