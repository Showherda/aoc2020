import sys
sys.stdin=open('input.txt')
inp=sys.stdin.readlines()
n=len(inp)
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
print(acc)
