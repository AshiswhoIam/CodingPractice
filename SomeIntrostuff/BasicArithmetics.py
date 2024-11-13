import math
cookie=5
#cookie+=1
#cookie-=2
#cookie*=3
#cookie/=3
#cookie**=5
remainder= cookie%3
print(remainder)

x=2.1
y=-3
z=4
#round fnc
r = round(x)
print(r)

#abs fnc
r=abs(y)
print(r)

#exp
r=pow(3,4)
print(r)

r=max(x,y,z)
print(r)
r=min(x,y,z)
print(r)

#some more math fncs
a=25
b=9.1
c=7.9
print(math.pi)
print(math.e)
re=math.sqrt(a)
re1=math.ceil(b)
re2=math.floor(c)
print(re)
print(re1)
print(re2)


#some exercise1

radius=float(input("Enter R of circle"))
cir=2*math.pi *radius
print(f"The cir is: {cir}")
print(f"The cir is: {round(cir,2)}")

#some exercise2
radius=float(input("Enter R of circle"))
area= math.pi *pow(radius,2)
print(f"The area is: {area}")

#hyp of triangle

sidea=float(input("Enter a of rect"))
sideb=float(input("Enter b of rect"))
sidec= math.sqrt(pow(sidea,2)+pow(sideb,2))
print(f"Side c is {sidec}")