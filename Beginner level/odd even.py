a=int(raw_input())
print a
if (a>=1 and a<=100000):
	if(a%2==1):
		print('Odd')
	else:
		print('Even')
else:
	print('invalid input')
