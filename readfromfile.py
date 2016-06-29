# Inputs as a list in dictonary: mapping with keys
db={}
for line in open('places.txt'):
	l = line.split()
	actor = l[0]
	movie = l[1]

	if actor in db:
		db[actor].append(movie)
	else:
		db[actor] = [movie]

print db

'''
# mapping with Values
newdb = {}
for k,v in db.items():
	for e in v:
		 if e in newdb:
		 	newdb[e].append(k)
		 else:
		 	newdb[e] = [k]

print newdb
'''

#max of Values
l = db.items()

def mycmp(x,y):
	return len(x[1]) - len(y[1])

f = sorted (l,cmp = mycmp, reverse = True)
print f