import sys
sys.stdin=open('input.txt')
num=[int(v) for v in sys.stdin.readlines()]
val=542529149
n=len(num)
inp=num.copy()
for i in range(1, n):
	inp[i]+=inp[i-1]
for i in range(n):
	for j in range(n):
		if i-j>1 and inp[i]-inp[j]==val:
			print(min(num[j+1:i+1])+max(num[j+1:i+1]))
