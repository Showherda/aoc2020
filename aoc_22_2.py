p1, p2=[], []
f=open('input.txt').readlines()
flag=1
for v in f:
	v=v.strip('\n')
	if 'Player 2' in v:
		flag=0
	if v.isnumeric():
		if flag:
			p1.append(int(v))
		else:
			p2.append(int(v))

def recurse(p1, p2, config):
	while len(p1) and len(p2):
		if p1 in config[1] or p2 in config[2]:
			return 1, p1
		config[1].append(p1.copy())
		config[2].append(p2.copy())
		a, b=p1.pop(0), p2.pop(0)
		if len(p1)>=a and len(p2)>=b:
			ret, tmp=recurse(p1[:a], p2[:b], {1:[], 2:[]})
			if ret==1:
				p1.append(a)
				p1.append(b)
			else:
				p2.append(b)
				p2.append(a)
		else:
			if a>b:
				p1.append(a)
				p1.append(b)
			else:
				p2.append(b)
				p2.append(a)
		if len(p1)==0 or len(p2)==0:
			if len(p1)==0:
				return 2, p2
			else:
				return 1, p1

flag, tmp=recurse(p1, p2, {1:[], 2:[]})
ans=0
for i, q in enumerate(tmp[::-1], 1):
	ans+=q*i
print(ans)
