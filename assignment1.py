#print("Hello World " )


# List
a = []
b = [0,1,'house','c',2.67 ]


a.append(1)
a.append(2)
a.append(b)
a.append(56)


for indexPtr,iter in enumerate(b) :
	if (iter == 'house' ) :
		continue
	if indexPtr % 2 == 0 :
		print(" Values: " + str(iter) )
	else :
		print(" Index: " + str(indexPtr))

#	if ( iter == 1 ) :
#		break


#print(a)

#print an index of the list :

#print(a[2])

# output [ 1, 2, [0,1,'house','c',2.67], 56 ]


# Map

c = {0:'element1',1:'element2',3:'element3' }   # Empty map

c[0] = 'test'

#print(c)
#print(c[1])





 
