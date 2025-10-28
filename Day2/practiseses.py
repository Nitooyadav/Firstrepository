
"""
#WAP to enter name of three movies and store them in list
a=input("enter you first fav movie:")
b=input("enter you second fav movie:")
c=input("enter you third fav movie:")
list=[a,b,c]
print("my fav movies are",list)


#write a program to checl if the list contains palindrome of elements
a=input("enter anything:")
print(a)
b=(''.join(reversed(a)))
print(b)
if a==b:
    print("T")
else:
    print("F")



age = 36
txt = f"My name is John, I am {age}"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

text = "We are the so-called \"Vikings\" from the north."
print(text)



a=input("enter a string:")
b=(''.join(reversed(a)))
print(b)


x=int(input("enter frst number:"))
y=int(input("enter second number:"))
z=int(input("enter third number:"))
if (x>y and x>z):
    print("the greater number is", x)
elif (y>x and y>z):
    print("the greater number is", y)
else:
    print("the greater number is", z)

    


txt=input("enter a name:")
vowels=("a","e","i","o","u")
for i in vowels:

a=input("enter a string:")
print(a[-1:])


#Wap a program to count the numbers of students with A grade in the following tuple
tup=("A","B","A","C","D","A","C","B","A","A","E")
print(type(tup))
print(len(tup))
print(tup.count("A"))
x=list(tup)
x.sort()
print(x)


random={
    "table": ["a piece of furniture","list of facts and figures"], 
    "cat":"a small animal" ,
    "age":25
    }
print(random)
print(type(random))

subjects={"python","java","c++","python","javascript","c","c++","java",
          }
print(subjects)
print(len(subjects))

#wap to enter marks of three subjects from the user and store it in dictionary

emptydict={}
grade=int(input("enter physics: "))
emptydict.update({"physics" : grade})
grade=int(input("enter chemistry: "))
emptydict.update({"chemistry" : grade})
grade=int(input("enter maths: "))
emptydict.update({"maths" : grade})
print(emptydict)


#wap to print numbers from 1 to 100
i=101
while i>1:
    i-=1
    print(i)
    
    
i=1
n=int(input("enter any number:"))
while i<=10:
    b=(n*i)
    print(b)
    i+=1
    
#1,4,9,16,25
i=1
while i<=10:
    b=(i*i)
    print(b)
    i+=1

nums=(1,4,9,16,25,36,49,64,81,100)
idx=0
while idx<10:
    print(nums[idx])
    idx+=1

nums=(1,4,9,16,25,36,49,64,81,100)
x=int(input("enter what to search:"))
i=0
while i<len(nums):
    if nums[i]==x:
        print("found")
        break
    else:
        print("finding")
        i+=1

nums=[1 , 4 , 9 , 1 , 25 , 36 , 49 , 64 , 81 , 100 , 25 , 5 , 25]

idx=0
for el in nums:
    if(el==25):
        print("found at idx",idx)
        idx+=1
        
def converter(usd_val):
    inr_val= usd_val*88.19
    print("The USD val is",usd_val , "and its INR val is",inr_val)
converter(10)


def call_factorial():
    n=int(input("enter the number:"))
    fact=1
    for i in range(1 , n+1):
        fact=fact * i
    print(fact)

call_factorial()


series=["TVD", "TSITP", "MLWWB", "TO"]
def len_list(list):
    print(len(list))
    print(list[0:5],)

len_list(series)

class Student:
    name = "Nitoo"

s1 = Student()  
s2 = Student()  
print(s1.name)
print(s2.name)

class Car:

    def __init__(self,color,brand,name):
        self.color=color
        self.brand=brand
        self.name=name
        print("adding car database..")
    

car1=Car("pink","porsche","abbas car")
print(car1.color, car1.brand,car1.name  )

car2= Car("blue","porsche","Nitoo car")
print(car2.color, car2.brand,car2.name  )
"""
class students:
    def __init__(self,name,maths,lang,sci):
        self.name=name
        self.maths=maths
        self.lang=lang
        self.sci=sci

    def avg(self):
        x=(self.maths+self.lang+self.sci)/3
        print("the avg marks of",self.name,"will be",x)
       

one=students("rudra",35,65,55)
two=students("tithi",85,55,63)



print(one.maths)
print(two.lang)
print(one.avg())
print(two.avg())



    




    