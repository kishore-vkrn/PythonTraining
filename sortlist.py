l = [ ['awi',30], ['hgs',34], ['jkl',54] ]

'''
def mcmp(x,y):
	print x,y
	return x[1] - y[1]

def mname(x,y):
	print x,y
	if x[0] < y [0]:
 		return -1
	elif x[0] > y [o]:
		return 1
	else:
		return 0
'''
def newkey(x):
	print x
	print x[0]
	return x[0]

'''
f = sorted (l,mcmp)
print f

f = sorted (l,mname,reverse=True)
print f
'''
f = sorted (l,key=newkey)
print f
