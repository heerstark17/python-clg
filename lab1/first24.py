def q1():
    a=int(input("Enter first num"))
    b=int(input("Enter second num"))
    print("sum of given numbers is",a+b)

def q2():
    a=int(input("Enter first num"))
    b=int(input("Enter second num"))
    print("substraction of given numbers is",a-b)

def q3():
    a=int(input("Enter first num"))
    b=int(input("Enter second num"))
    print("multiplication of given numbers is",a*b)

def q4():
    a=float(input("Enter first num"))
    b=float(input("Enter second num"))
    print("division of given numbers is",a/b)

def q5():
    a=float(input("Enter first num"))
    b=float(input("Enter second num"))
    print("sum of given numbers is",a+b)
    print("substraction of given numbers is",a-b)
    print("multiplication of given numbers is",a*b)
    print("division of given numbers is",a/b)

def q6():
    a=float(input("Enter hours to convert into minutes"))
    print(a,"hours is equals to",a*60,"minutes")

def q7():
    a=float(input("Enter minutes to convert into hours"))
    print(a,"minutes is equals to",a/60,"hours")

def q8():
    a=float(input("Enter amount of dollars to convert into rupees"))
    print(a,"Dollars is equals to",a*48,"Rupees")

def q9():
    a=float(input("Enter amount of rupees to convert into dollars"))
    print(a,"rupees is equals to",a/48,"Dollars")

def q10():
    a=float(input("Enter amount of Dollars to convert into pound"))
    print(a,"Dollars is equals to",a*48/70,"Pounds")

def q11():
    a=float(input("Enter amount of weight in grams to convert into kilograms"))
    print(a,"grams is equals to",a/10**3,"Kilograms")

def q12():
    a=float(input("Enter amount of weight in kilograms to convert into grams"))
    print(a,"kilograms is equals to",a*10**3,"grams")

def q13():
    a=float(input("Enter bytes to convert into KB,MB and GB"))
    print(a,"bytes is equals to",a/2**10,"KB")
    print(a,"bytes is equals to",a/2**20,"MB")
    print(a,"bytes is equals to",a/2**30,"GB")
    
def q14():
    a=float(input("Enter temperature in celcius to convert into fahrenheit"))
    print(a,"celcius is equals to",(9/5*a)+32,"Fahrenheit")

def q15():
    a=float(input("Enter temperature in fahrenheit to convert into celcius"))
    print(a,"Fahrenheit is equals to",5/9*(a-32),"celcius")

def q16():
    P=float(input("Enter principal amount of loan"))
    R=float(input("Enter Rate of interest"))
    N=float(input("Enter duration of loan in years"))
    I=P*R*N/100
    print("Your Interest of Loan is",I,"Rupees")

def q17():
    L=float(input("Enter length of side of square"))
    A=L**2
    P=4*L
    print("Area of square is",A)
    print("Perimeter of square is",P)

def q18():
    L=float(input("Enter length of rectangle"))
    B=float(input("Enter width of rectangle"))
    A=L*B
    P=2*(L+B)
    print("Area of rectangle is",A)
    print("Perimeter of rectangle is",P)

def q19():
    R=float(input("Enter Radius of Circle"))
    A=22/7*R**2
    print("Area of circle is",A)

def q20():
    H=float(input("Enter Height of triangle"))
    B=float(input("Enter base of triangle"))
    A=0.5*H*B
    print("Area of Triangle is",A)
    
def q21():
    gross_salary=float(input("Enter your Gross salary in rupees"))
    net_salary=(gross_salary)+(gross_salary/10)-(gross_salary*0.03)
    print("Your Net salary is",net_salary,"Rupees")

def q22():
    gross_sales=float(input("Enter your Gross sales"))
    net_sales=gross_sales-(gross_sales/10)
    print("Your Net sales is",net_sales)

def q23():
    s1=float(input("Enter marks of first subject"))
    s2=float(input("Enter marks of fsecond subject"))
    s3=float(input("Enter marks of third subject"))
    total=s1+s2+s3
    avg=total/3
    print("Your average of three subjects is",avg,"And total marks of three subjects is",total)

def q24():
    a=int(input("Enter first num"))
    b=int(input("Enter second num"))
    a,b=b,a
    print("Value of a after swapping",a)
    print("Value of b after swapping",b)
    
    
