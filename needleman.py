alphabet = ['A', 'T', 'G', 'C']
score = [[4, -1, -1, -1, -2],\
		 [-1, 4, -1, -1, -2],\
		 [-1, -1, 4, -1, -2],\
		 [-1, -1, -1, 4, -2],\
		 [-2, -2, -2, -2, -2]
		 ]
#score[-1][-1] will not be visited

#TODO:output the mismatch, output the other route 
def trace(D, char1, char2, i, j):
	'''
	if D[i-2][j-1] == D[i-1][j-2] and D[i-2][j-1]>D[i-2][j-2]:
		print(char1 + '--' + '_')
		return (i-1, j) 
	'''
	if D[i-1][j-1] == D[i-1][j-2] + score[-1][alphabet.index(char2)]:
		print('_' + '--'+ char2)
		return(i, j-1)
	if D[i-1][j-1] == D[i-2][j-1] + score[alphabet.index(char1)][-1]:
		print(char1 + '--' + '_')
		return (i-1, j)
	if D[i-1][j-1] == D[i-2][j-2] + score[alphabet.index(char1)][alphabet.index(char2)]:
		print(char1 + '--' + char2)
		return (i-1, j-1)


def globalAlignment(x, y):
	D = []
	for i in range(len(x) + 1):
		D.append([0] * (len(y) + 1))

	for i in range(1, len(x) + 1):
		D[i][0] = D[i-1][0] + score[alphabet.index(x[i-1])][-1]
	for i in range(1, len(y) + 1):
		D[0][i] = D[0][i-1] + score[-1][alphabet.index(y[i-1])]

	#全局遍历
	for i in range(1, len(x) + 1):
		for j in range(1, len(y) + 1):
			distHor = D[i][j-1] + score[-1][alphabet.index(y[j-1])]
			distVer = D[i-1][j] + score[alphabet.index(x[i-1])][-1]
			if x[i-1] == y[j-1]:
				distDiag = D[i-1][j-1] + score[alphabet.index(x[i-1])][alphabet.index(y[j-1])]
			else:
				distDiag = D[i-1][j-1] + score[alphabet.index(x[i-1])][alphabet.index(y[j-1])]

			D[i][j] = max(distDiag, distVer, distHor)

	print(x[i-1] + '--' + y[j-1])
	while(i>1 and j>1):
		(i, j) = trace(D, x[i-2], y[j-2], i, j)
		#print(i,j)

	return D[-1][-1]

if __name__ == '__main__':
	seq1 = 'AACGTACTCA'
	seq2 = 'TCGTACTCA'
	penalty = globalAlignment(seq1, seq2)
	print(penalty, seq2, seq1)
