import sys
sys.stdin=open('input.txt')
inp=[int(v) for v in sys.stdin.readlines()]
n=len(inp)
val=542529149
num=inp.copy()
for i in range(1, n):
	num[i]+=num[i-1]
p1=0
while p1<n:
	p2=p1
	while num[p2]-num[p1]<val:
		p2+=1
	if p2-p1>1 and num[p2]-num[p1]==val:
		print(min(inp[p1+1:p2+1])+max(inp[p1+1:p2+1]))
	while p2>=p1 and num[p2]-num[p1]>val:
		p1+=1
	p1+=1
