a=int(input("enter no.1-"))
b=int(input("enter no.2-"))
c=int(input("enter no.3-"))
if a>b:
	if a>c:
		print("1st maximum number=",a)
		if b>c:
			print("2 nd maximum number=",b)
			print("3 rd maximum number=",c)
		else:
			print("2 nd maximum number=",c)
			print("3rd maximum number",b)
	else:
		print("1st maximum number=",c)
		print("2nd maximum number=",a)
		print("3rd maximum number=",b)

else:
	if b>c:
		print("1st maximum number=",b)
		if a>c:
			print("2 nd maximum number=",a)
			print("3 rd maximum number=",c)
		else:
			print("2 nd maximum number=",c)
			print("3 rd maximum number=",a)
	else:
		print("1st maximum number=",c)
		print("2 nd maximum number=",b)
		print("3rd maximum number=",a)		
	