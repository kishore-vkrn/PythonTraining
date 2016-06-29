class Complex(object):
	def __init__(self,i,j):
		self.i = i
		self.j = j

	def __repr__(self): #throws only string values. to convert the address to reqd values this is used.
		return "Complex Num: " + str(self.i) + "+" + str(self.j) + "i"


num1 = Complex(2,4)
num2 = Complex(3,8)

print num1
print num2