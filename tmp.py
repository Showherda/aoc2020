f=open('input.txt')
alr={}
evr=set()
cnt={}
for v in f:
	i=v.index('(contains ')
	tmp=v[i+10:].split(',')
	for c in v[:i].split():
		evr.add(c)
		cnt[c]=cnt.get(c, 0)+1
	for c in tmp:
		try:
			alr[c.strip(' ,)\n')].append(set(v[:i].split()))
		except:
			alr[c.strip(' ,)\n')]=[set(v[:i].split())]
pss=set()
for u in alr:
	tmp=alr[u][0]
	for v in alr[u][1:]:
		tmp=tmp.intersection(v)
	for c in tmp:
		pss.add(c)
print(sum(cnt[c] for c in evr.difference(pss)))