def print_factors(x):
	flag=0
	for i in range(2,x):
		if x % i == 0:
			flag=1
	if flag==0:
		print x,"is a Prime Number"
	else:
		for i in range(1, x + 1):
			if x % i == 0:
				print(i)