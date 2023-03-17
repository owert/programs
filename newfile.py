def com(a,b):
	z= complex(a,b)
	import math
	print("modulus =", math.sqrt(a**2+ b**2))
	print ("arguement=",math.atan(b/a))
	p=math.atan(b/a)
	print("argument in degrees=", p*(180)/(math.pi))
	return
com(int(input("enter number 1-")) ,int(input("enter number 2-")))
