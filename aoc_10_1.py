import sys
sys.stdin=open('input.txt')
inp=[0]+sorted([int(v) for v in sys.stdin.readlines()])
inp.append(inp[-1]+3)
one, three=0, 0
for i in range(1, len(inp)):
	if inp[i]-inp[i-1]==1:
		one+=1
	if inp[i]-inp[i-1]==3:
		three+=1
print(one*three)
