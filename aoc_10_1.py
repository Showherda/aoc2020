import sys
sys.stdin=open('input.txt')
inp=sorted([int(v) for v in sys.stdin.readlines()])
one, three=1, 1
for i in range(1, len(inp)):
	if inp[i]-inp[i-1]==1:
		one+=1
	if inp[i]-inp[i-1]==3:
		three+=1
print(one*three)
