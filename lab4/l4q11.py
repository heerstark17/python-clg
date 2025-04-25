def q11():
    def fac(n):
        fact=1
        for i in range (1,n+1):
            fact*=i
            return fact
    n=int(input("Enter number of terms"))
    cos_x=0
    for i in range(0,n):
        power=2*i
        sign= (-1)**i
        cos_x+=sign * ('x'**power) / fac(n)
            
    print("cos_x=", cos_x)
q11()
