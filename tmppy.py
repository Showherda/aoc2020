import sys
sys.stdin=open('input.txt')
mem={}
for line in sys.stdin.readlines():
	ln=line.split()
	if line[1]=='a':
		mask=ln[2]
	else:
		tmp=bin(int(ln[2]))[2:]
		tmp=list('0'*(36-len(tmp))+tmp)
		for i in range(36):
			if mask[i]=='1':
				tmp[i]='1'
			if mask[i]=='0':
				tmp[i]='0'
		val=''.join(tmp)
		ln[2]=str(int(val, 2))
		exec(' '.join(ln))
print(sum(mem.values()))