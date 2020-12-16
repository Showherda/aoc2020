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
ans=0
for v in m:
	for d in v.split(','):
		if int(d) not in val:
			ans+=int(d)
print(ans)