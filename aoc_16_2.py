import re
s=open('input.txt').read()
pattern='\d*-\d*'
val=set()
m=re.findall(pattern, s)
for v in m:
	l, r=v.split('-')
	for d in range(int(l), int(r)+1):
		val.add(d)
re.purge()
pattern='.*\d*,.*'
m=re.findall(pattern, s)
col={}
for v in m:
	ok=1
	for d in v.split(','):
		if int(d) not in val:
			ok=0
			break
	if ok:
		for i, d in enumerate(v.split(',')):
			try:
				col[i].append(int(d))
			except:
				col[i]=[int(d)]
match={}
for v in s.split('\n'):
	pattern='\d*-\d*'
	val=set()
	re.purge()
	m=re.findall(pattern, v)
	for a in m:
		l, r=a.split('-')
		for d in range(int(l), int(r)+1):
			val.add(d)
	for i in range(len(col)):
		ok=1
		for j in col[i]:
			if j not in val:
				ok=0
				break
		if ok:
			try:
				match[v[:v.index(':')]].add(col[i][0])
			except:
				match[v[:v.index(':')]]=set([col[i][0]])
ok=1
while ok:
	ok=0
	for v in match:
		if len(match[v])==1:
			val=match[v].pop()
			match[v].add(val)
			for u in match:
				if u!=v and val in match[u]:
					match[u].remove(val)
					ok=1
ans=1
for v in match:
	if v[:2]=='de':
		ans*=match[v].pop()
print(ans)
# if anyone is reading this, I feel you ;-;
