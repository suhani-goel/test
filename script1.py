sl = []
temp = "val1"
new = input().split(",")
print(new)

def fun(inp):
	# temp = "val2"

	print ("<<", temp)
	inp = "inp"+inp
	inp = inp.upper()
	return inp
print (">>", temp)	



if new == "end" : 
	print(sl)
else :
	for i in new:
		t = fun(i)
		sl.append(t)
	# print (sl[0])
	# sl[0].sort()
	# print (type(sl[0]))
	sl.sort()
	print(sl)	