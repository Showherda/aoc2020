from queue import Queue
p1, p2=Queue(), Queue()
f=open('input.txt').readlines()
flag=1
for v in f:
	v=v.strip('\n')
	if 'Player 2' in v:
		flag=0
	if v.isnumeric():
		if flag:
			p1.put(int(v))
		else:
			p2.put(int(v))
while not p1.empty() and not p2.empty():
	a, b=p1.get(), p2.get()
	if a>b:
		p1.put(a)
		p1.put(b)
	else:
		p2.put(b)
		p2.put(a)
flag=p1.empty()
tp1, tp2=[], []
while not p1.empty():
	tp1.append(p1.get())
while not p2.empty():
	tp2.append(p2.get())
ans=0
for i, q in enumerate([tp1[::-1], tp2[::-1]][flag], 1):
	ans+=q*i
print(ans)
