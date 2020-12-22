f=open('input.txt')
alr={}
evr=set()
cnt={}
for v in f:
	i=v.index('(contains ')
	tmp=v[i+9:].split(',')
	for c in v[:i].split():
		evr.add(c)
		cnt[c]=cnt.get(c, 0)+1
	for c in tmp:
		try:
			alr[c.strip(' ,)\n')].append(set(v[:i].split()))
		except:
			alr[c.strip(' ,)\n')]=[set(v[:i].split())]
for u in alr:
	tmp=alr[u][0]
	for v in alr[u][1:]:
		tmp=tmp.intersection(v)
	alr[u]=tmp.copy()
ans={}
ok=1
while ok:
	ok=0
	for u in alr:
		if len(alr[u])==1:
			ingr=alr[u].pop()
			ans[u]=ingr
			alr[u].add(ingr)
			for v in alr:
				if v!=u and ingr in alr[v]:
					alr[v].remove(ingr)
					ok=1
out=''
for v in sorted(ans.keys()):
	out+=ans[v]+','
print(out.strip(','))
