import sys
sys.stdin=open('input.txt')
inp=[int(v) for v in sys.stdin.readlines()]
m=max(inp)
tab=set(inp)
memo={}
done=set()
def fun(u):
	global tab, m
	if u in done:
		return memo[u]
	if u>=m:
		return 1
	memo[u]=0
	if u+1 in tab:
		memo[u]+=fun(u+1)
	if u+2 in tab:
		memo[u]+=fun(u+2)
	if u+3 in tab:
		memo[u]+=fun(u+3)
	done.add(u)
	return memo[u]
print(fun(0))
