import sys
sys.stdin=open('input.txt')
def recur(pos):
	global mem, val, addr, ind
	if pos==len(ind):
		mem[int(''.join(addr), 2)]=val
	else:
		addr[ind[pos]]='0'
		recur(pos+1)
		addr[ind[pos]]='1'
		recur(pos+1)
mem={}
for line in sys.stdin.readlines():
	ln=line.split()
	if line[1]=='a':
		mask=list(line[7:])
	else:
		tmp=''
		for v in line[4:]:
			if v==']':
				break
			tmp+=v
		tmp=bin(int(tmp))[2:]
		addr=['0']*(36-len(tmp))+list(tmp)
		ind=[]
		for i in range(36):
			if mask[i]!='0':
				addr[i]=mask[i]
			if mask[i]=='X':
				ind.append(i)
		val=int(ln[2])
		recur(0)
print(sum(mem.values()))