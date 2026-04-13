def nand(a,b):
	return int(not(a and b))
	
inputs = [(0,0),(0,1),(1,0),(1,1)]
print ("INPUT A \t|\tINPUT B |\t OUTPUT ")
print ("-" * 47)
for a,b in inputs:
	output=nand(a,b)
	print(f"\t{a}\t|\t{b}\t|\t{output}")
	
