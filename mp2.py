import math as math
import numpy as np
x1=int(input('Enter x1: '))
y1=int(input('Enter y1: '))
x2=int(input('Enter x2: '))
y2=int(input('Enter y2: '))
x3=int(input('Enter x3: '))
y3=int(input('Enter y3: '))
a=(x1-x2)**2+(y1-y2)**2
b=(x2-x3)**2+(y2-y3)**2
c=(x3-x1)**2+(y3-y1)**2
d=2*((b*c)+(c*a)+(a*b))-(a**2+b**2+c**2)
h1=(b*(c+a-b)*x1+c*(a+b-c)*x2+a*(b+c-a)*x3)/d
k1=(b*(c+a-b)*y1+c*(a+b-c)*y2+a*(b+c-a)*y3)/d
r1=math.sqrt((h1-x1)**2+(k1-y1)**2)
d=np.array([(x1**(2)+y1**(2),y1,1),(x2**(2)+y2**(2),y2,1),(x3**(2)+y3**(2),y3,1)])
e=np.array([(x1**(2)+y1**(2),x1,1),(x2**(2)+y2**(2),x2,1),(x3**(2)+y3**(2),x3,1)])
f=np.array([(x1**(2)+y1**(2),x1,y1),(x2**(2)+y2**(2),x2,y2),(x3**(2)+y3**(2),x3,y3)])
g=np.array([(x1,y1,1),(x2,y2,1),(x3,y3,1)])
G=np.linalg.det(g)
dd=np.linalg.det(d)/G
D1=-1*dd;
E1=np.linalg.det(e)/G
ff=np.linalg.det(f)/G
F1=-1*ff
h=round(h1,2)
k=round(k1,2)
r=round(r1,2)
D=round(D1,2)
E=round(E1,2)
F=round(F1,2)
print('The central coordinates of the circle (h,k) are: h=',h,'k=',k)
print('The radius of the circle is: r=',r)
print('The vector [D,E,F], where D,E,F are the coefficients in the general equation of a circle are: D=',D,'E=',E,'F=',F)
