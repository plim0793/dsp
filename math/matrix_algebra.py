# Matrix Algebra
import numpy as np

def main():
	A = np.array([[1,2,3],[2,7,4]])
	B = np.array([[1,-1],[0,1]])
	C = np.array([[5,-1],[9,1],[6,0]])
	D = np.array([[3,-2,-1],[1,2,3]])

	u = np.array([[6,2,-3,5]])
	v = np.array([[3,5,-1,4]])
	w = np.array([[1],[8],[0],[5]])

	alpha = 6

	# Matrix Dimensions:

	print('Matrix Dimensions:')
	print('1.1) ', A.shape)
	print('1.2) ', B.shape)
	print('1.3) ', C.shape)
	print('1.4) ', D.shape)
	print('1.5) ', u.shape)
	print('1.6) ', w.shape)

	# Vector Operations:

	print('\nVector Operations:')
	print('2.1) ', u + v)
	print('2.2) ', u - v)
	print('2.3) ', alpha*u)
	try:
		print('2.4) ', np.dot(u, v))
	except:
		print('2.4) ', 'Not Defined')
	print('2.5) ', np.linalg.norm(u))

	# Matrix Operations:

	print('\nMatrix Operations:')
	try:
		print('3.1) ', A + C)
	except: print('3.1) ', 'Not Defined')
	print('3.2)\n', A - np.transpose(C))
	print('3.3)\n', np.transpose(C) + 3*D)
	print('3.4)\n', np.dot(B,A))
	try:
		print('3.5) ', B*np.transpose(A))
	except:
		print('3.5) ', 'Not Defined')













if __name__ == '__main__':
	main()
