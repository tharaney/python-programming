a=int(raw_input())
b=0
for i in range(1,10000):
	if (a%i==0):
	    b=b+1
if(b==2):
	print ('yes')

else:
	print ('no')
