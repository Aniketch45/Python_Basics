#find GCD of numbers
import math

def gcd_lcm():
    n1=int(input("Enter firt number :"))
    n2=int(input("Enter second number :"))
    gcd=math.gcd(n1,n2)
    lcm=abs(n1*n2)//gcd
    print(f"GCD : {gcd} and LCM : {lcm}")

gcd_lcm()