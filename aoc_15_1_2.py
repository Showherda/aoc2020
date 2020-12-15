inp=[1, 0, 15, 2, 10, 13]
mem={}
val=2020	# put in 30000000 for part 2
for i, v in enumerate(inp, 1):
	mem[v]=[i]
while len(inp)<val:
	num=inp[-1]
	if len(mem[num])==1:
		inp.append(0)
		try:
			mem[0].append(len(inp))
		except:
			mem[0]=[len(inp)]
	else:
		inp.append(mem[num][-1]-mem[num][-2])
		try:
			mem[inp[-1]].append(len(inp))
		except:
			mem[inp[-1]]=[len(inp)]
print(inp[val-1])
