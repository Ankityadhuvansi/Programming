#wap to print "HELLO WORLD"
print("Hello Python")
#wap to print sum of two numbers
a=10
b=20
print(a+b)
#WAP to print sum of two numbers taken from user    
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
print(a+b)
#wap to design a simple calculator
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulo Division") 
ch=int(input("Enter your choice:"))
if ch==1:
    print(a+b)
elif ch==2:
    print(a-b)
elif ch==3:
    print(a*b)
elif ch==4:
    print(a/b)
elif ch==5:
    print(a%b)
else:
    print("Invalid choice")

#Wap to calculate simple interest and compound interest
p=int(input("Enter p value:"))
t=int(input("Enter t value:"))
r=int(input("Enter r value:"))
si=(p*t*r)/100
print("Simple Interest:",si)
ci=p*(1+r/100)**t
print("Compound Interest:",ci)

#wap to input 4 digit numbersand print sum of its digits
n=int(input("Enter a 4 digit number:")) 
s=0
while n>0:
    r=n%10
    s=s+r
    n=n//10
print("Sum of digits:",s)

# WAP to input 4 digit number and print reverse of it
n=int(input("Enter a 4 digit number:"))
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
print("Reverse of a number:",rev)
# calculator without using if else
a=int(input("Enter a value:"))  
b=int(input("Enter b value:"))
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulo Division")
ch=int(input("Enter your choice:"))
print({1:a+b,2:a-b,3:a*b,4:a/b,5:a%b}.get(ch,"Invalid choice"))
# reverse of a number using slicing
n=int(input("Enter a 4 digit number:"))
print("Reverse of a number:",n[::-1])
