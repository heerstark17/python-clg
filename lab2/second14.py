def q1():
    a=float(input("Enter first number"))
    b=float(input("Enter second number"))
    if (a>b):
        print("Largest number is",a)
        print("Smallest number is",b)
    else:
        print("Largest number is",b)
        print("Smallest number is",a)
        
def q2():
    a=float(input("Enter first number"))
    b=float(input("Enter second number"))
    c=float(input("Enter Third number"))
    if (a>b)and(a>c)and(b>c):
        print("Largest number is",a)
        print("Smallest number is",c)
    elif(a>b)and(a>c)and(c>b):
        print("Largest number is",a)
        print("Smallest number is",b)
    elif(b>a)and(b>c)and(c>a):
        print("Largest number is",b)
        print("Smallest number is",a)
    elif(b>a)and(b>c)and(c<a):
        print("Largest number is",b)
        print("Smallest number is",c)
    elif(c>a)and(c>b)and(a>b):
        print("Largest number is",c)
        print("Smallest number is",b)
    else:
        print("Largest number is",c)
        print("Smallest number is",a)

def q3():
    a=float(input("Enter your number"))
    if (a%2)==0:
        print(a,"is Even number is")
    else:
        print(a,"is odd number is")

def q4():
    a=float(input("Enter your number"))
    if (a%10)==0:
        print(a,"is divisible by 10")
    else:
        print(a,"is not divisible by 10")

def q5():
    a=int(input("Enter your Age"))
    if (a<18):
        print("You are Minor")
    else:
        print("You are Major")

def q7():
    a=int(input("Enter year"))
    if (a%4)==0:
        print(a,"is leap year")
    else:
        print(a,"is not leap year")

def q8():
    a=float(input("Enter first angle of triangle"))
    b=float(input("Enter second angle of triangle"))
    c=float(input("Enter third angle of triangle"))
    if (a+b+c)==180:
        print("Your triangle is valid")
    else:
        print("Your triangle isn't valid")
    
def q9():
    a=int(input("Enter your number"))
    print("Absolute value is",a) if (a>0) else print("Absolute value is ",a*-1)  

def q10():
    L=float(input("Enter length of rectangle"))
    B=float(input("Enter width of rectangle"))
    A=L*B
    P=2*(L+B)
    if(A>P):
        print("Area is greater than perimeter ")
    else:
        print("Perimeter is greater than area")
    
def q11():
    x1=float(input("Enter x1 cordinate"))
    y1=float(input("Enter y1 cordinate"))
    x2=float(input("Enter x2 cordinate"))
    y2=float(input("Enter y2 cordinate"))
    x3=float(input("Enter x3 cordinate"))
    y3=float(input("Enter y3 cordinate"))
    m1=(y2-y1)/(x2-x1)
    m2=(y3-y2)/(x3-x2)
    print("All points lies on same line") if (m1==m2) else print("All points doesn't lie on same line")

def q12():
    x=float(input("Enter x cordinate of center of circle"))
    y=float(input("Enter y cordinate of center of circle"))
    r=float(input("Enter radius of circle"))
    x1=float(input("Enter x1 cordinate"))
    y1=float(input("Enter y1 cordinate"))
    m=(x1-x)**2+(y1-y)**2-r**2
    if (m>0):
        print("given point lies outside the circle")
    elif (m<0):
        print("given point lies inside the circle")
    else:
        print("given point lies on the circle")

def q13():
    a=int(input("Enter your digit from '0 to 19' to convert into words"))
    if (a==0):
        print("given digit is Zero")
    elif (a==1):
        print("given digit is One")
    elif (a==2):
        print("given digit is Two")
    elif (a==3):
        print("given digit is Three")
    elif (a==4):
        print("given digit is Four")
    elif (a==5):
        print("given digit is Five")
    elif (a==6):
        print("given digit is Six")
    elif (a==7):
        print("given digit is Seven")
    elif (a==8):
        print("given digit is Eight")
    elif (a==9):
        print("given digit is Nine")
    elif (a==10):
        print("given digit is Ten")
    elif (a==11):
        print("given digit is Eleven")
    elif (a==12):
        print("given digit is Twelve")
    elif (a==13):
        print("given digit is Thirteen")
    elif (a==14):
        print("given digit is Fourteen")
    elif (a==15):
        print("given digit is Fifteen")
    elif (a==16):
        print("given digit is Sixteen")
    elif (a==17):
        print("given digit is Seventeen")
    elif (a==18):
        print("given digit is Eighteen")
    elif (a==19):
        print("given digit is Nineteen")
    else:
        print("given digit is not in range")

def q14():  
    s1=float(input("Enter marks of first subject"))
    s2=float(input("Enter marks of fsecond subject"))
    s3=float(input("Enter marks of third subject"))
    total=s1+s2+s3
    avg=total/3
    print("Your average of three subjects is",avg,"And total marks of three subjects is",total)
    if (s1<=39 or s2<=39 or s3<=39):
        print("You are fail")

    if 80<=s1<=100:
        print("O")
    elif 70<=s1<=79:
        print("A+")
    elif 60<=s1<=69:
        print("A")
    elif  55<=s1<=59:
        print("B+")
    elif 50<=s1<=54:
        print("B")
    elif 45<=s1<=49:
        print("C")
    elif 40<=s1<=44:
        print("P")
    elif 0<=s1<=39:
        print("F")
    else :
        print("NA")
        
    if 80<=s2<=100:
        print("O")
    elif 70<=s2<=79:
        print("A+")
    elif 60<=s2<=69:
        print("A")
    elif  55<=s2<=59:
        print("B+")
    elif 50<=s2<=54:
        print("B")
    elif 45<=s2<=49:
        print("C")
    elif 40<=s2<=44:
        print("P")
    elif 0<=s2<=39:
        print("F")
    else :
        print("NA")

    if 80<=s3<=100:
        print("O")
    elif 70<=s3<=79:
        print("A+")
    elif 60<=s3<=69:
        print("A")
    elif  55<=s3<=59:
        print("B+")
    elif 50<=s3<=54:
        print("B")
    elif 45<=s3<=49:
        print("C")
    elif 40<=s3<=44:
        print("P")
    elif 0<=s3<=39:
        print("F")
    else:
        print("NA")
  


    
