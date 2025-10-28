"""
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=a+b
print(c)

#Write a program to input side of a square and its area
side=float(input("enter the side of square:"))
Area=side**2
print("The area of square is:", Area)

##Write a program to input two floating numbers and their average
a=float(input("enter first number:"))
b=float(input("enter second number:"))
avg=(a+b)/2
print("The avg of two floating numbers are:", avg)


a=float(input("enter first number:"))
b=float(input("enter second number:"))
print( a>=b)

str1="nitoo "
str2="yadavvvvv"
str3=str1+str2
print(str3)
print(len(str3))
str4=str3[7]
print(str4)
print(str3[2:7])
print(str3[:5])
print(str3[6:])
print(str3.endswith("dav"))
print(str3.capitalize())
print(str3.replace("nitoo" , "shaikh"))
print(str3.find("d"))
print(str3.count("v"))

#Write a program to input user first name and print iys lenght
username=input("enter your name:")
print("The length of your name:", len(username))


#Write a program to take the input and check if user can vote or not
#age=int(input("enter your age:"))
#if (age>=18):
#    print("You can vote")
#else:
#     print("you cannot vote")

##Write a program to take the input and 

#a=str(input("enter the color:"))
#color=a.lower()
#if(color=="red"):
 #    print("stop")
#elif(color=="green"):
 #    print("go")
#elif(color=="yellow"):
 #    print("look")
#else:
 #    print("Color absent")

 

 #write a program to grade the student
a=int(input("enter your marks:"))
if (a>=90):
    print("grade A")
elif(a>=80 and a<90):
    print("grade B")
elif(a>=70 and a<=80):
    print("grade C")
else:
    print("grade D")
    
#write a program to find odd and even number
num=int(input("enter number:"))
y=num%2
if (y==0):
    print("even number")
else:
    print("odd number")
    

#write a program to find greatest of three numbers
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))
if(num1>=num2 and num1>=num3):
    print("The greater number is:" , num1)
elif(num2>=num1 and num2>=num3):
    print("The greater number is:" , num2)
else:
    print("The greater number is:" , num3)
    

num=int(input("enter number:"))
divisor=int(input("enter divisor:"))
remainder=num%divisor
if(remainder==0):
    print("multiple number")
else:
    print("unmultiple number")
    """
x=input("enter anything:")
y=input("enter second anything:")
print(x)
print(y)
z=y
print(z)