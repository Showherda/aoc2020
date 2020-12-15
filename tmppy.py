import sys
sys.stdin=open('input.txt')
s=input()
inp=[]
N=1
for i, v in enumerate(sys.stdin.readline().split(',')):
	if v!='x':
		inp.append((int(v), int(v)-i))
		N*=int(v)
def gcd(a, b):
	if b==0:
		return [1, 0, a]
	x1, y1, d=gcd(b, a%b)
	return [y1, x1-y1*(a//b), d]
def inverse(pos):
	global inp, N
	nk=inp[pos][0]
	Nk=N//nk
	x0, y, d=gcd(Nk, nk)
	x=x0
	t=0
	while x<0:
		t+=1
		x=x0+(nk//d)*t
	return x
ans=0
for i in range(len(inp)):
	a, n, x=inp[i][1], N//inp[i][0], inverse(i)
	ans+=a*n*x
print(ans%N)