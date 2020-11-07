def scramble(seq):
	for i in range(len(seq)):
		seq = seq[1:] + seq[:1]
		yield seq
		
"""def scramble(seq):
	for i in range(len(seq)):
		yield seq[i:] + seq[:1]"""
		
F = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))

seq = input("enter sequence: ")
print(list(scramble(seq)))