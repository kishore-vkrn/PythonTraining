def varafun(*argt):
	print argt
	msum = 0
	for arg in argt:
		msum += arg
	return msum

print varafun(10,20,30,40,50,50)
