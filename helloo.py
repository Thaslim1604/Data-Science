#str1="listen"
#str2="silent"
#if sorted(str1)==sorted(str2):
    #print("Anagram")
#else:
    #print("Not Anagram")   

#import hi
#print(hi.fun(10,40))    
# s=[0,1,0,1,0]
# zeros=[]
# ones=[]
# for i in s:
    # if i==0:
        # zeros.append(i)
    # else:
        # ones.append(i) 
    # result=zeros+ones
# print(result)       
# class person:
    # x=10
    # y=20
    # tup=(1,2,3)
    # c=[5,6,7]
    # d={100,200,300}
    # def func(self):
        # print("this is my class person")
# p1=person()
# p1.func()
# print(p1.x)
# print(p1.y)
# print(p1.c)
# print(p1.d)
# print(p1.tup)
# class Engine5kcc:
    # def Onroad(self,kmph):
        # print(kmph,"km/h")

# bmw=Engine5kcc()
# audi=Engine5kcc()
# ferrari=Engine5kcc()
# bmw.Onroad(500)
# audi.Onroad(520)
# ferrari.Onroad(580)
# class Calculator:
    # def addition(self, a, b):
        # return a + b
    # def subtraction(self, a, b):
        # return a - b
    # def multiplication(self, a, b):
        # return a * b
    # def division(self, a, b):
        # if b == 0:
            # return "Error: Division by zero"
        # return a / b
# calc = Calculator()
# print(calc.addition(10, 5))
# print(calc.subtraction(10, 5))
# print(calc.multiplication(10, 5))
# print(calc.division(10, 5))



# class Engine5kcc:
#     def Onroad(self,kmhr):
#         print(kmhr,"km/hr")

# bmw = Engine5kcc()
# audi =Engine5kcc()
# ferrari = Engine5kcc()

# bmw.Onroad(500)
# audi.Onroad(600)
# ferrari.Onroad(700)


# class Engine5kcc:
    # def __init__(self,kmph,limit):
        # print("This is my Constructor",kmph)
        # self.a= kmph
        # self.limit=limit

    # def Onroad(self,weight):
        # print(self.a-weight)

        # print("Limit is :", self.limit)
# bmw=Engine5kcc(300, 500)
# audi=Engine5kcc(600, 500)
# ferrari=Engine5kcc(500, 500)

# bmw.Onroad(50)
# audi.Onroad(60)
# ferrari.Onroad(70)

# class Math:
    # formula= "(a+b)^2 = a^2 + 2ab + b^2"

# class Chemistry(Math):
    # pass
# obj2=Chemistry()
# print(obj2.formula)

# class math:
    # formula="(a+b)^2=a^2+2ab+b^2"
# class chemistry:
    # obj=math()
    # print(obj.formula)
# obj2=chemistry()        

# class math:
    # formula='a+b'
# class chem(math):
    # x=1
# class bio(math):
    # pass
# obj2=bio()
# print(obj2.formula)

# class math:
    #  formula="a+b"
# class chem:
    #  x=1
# class bio(math,chem):
    #   pass
# obj2=bio()
# print(obj2.formula)
# obj2=bio()
# print(obj2.x)


# class xyz:
    # def __init__(self,a,b):
        # self.a=a
        # self.b=b
    # def add (self):
        # return self.a+self.b

# class abc(xyz):
    # def __init__(self,a,b):
        # a+=10
        # b+=20
        # super().__init__(a,b)
# a=abc(10,20)
# print(a.add())


# class Device:
    # def play(self):
        # print("Playing media on a device")

# class TV(Device):
    # def play(self):
        # print("Playing media on TV")
# class Mobile(Device):
    # def play(self):
        # print("Playing media on Mobile")

# class Tablet(Device):
    # def play(self):
        # print("Playing media on Tablet")

# devices = [TV(), Mobile(), Tablet()]

# for d in devices:
#    d.play() 

# a=int(input("Enter Numerator"))
# b=int(input("Enter Denominator"))
# try:
    # print(a//b)
# except Exception:
    # print("Cannot divide by 0")
# print("welcome") 

# a=int(input("Enter Numerator"))
# b=int(input("Enter Denominator"))
# try:
    # print(a//b)
# except Exception as e:
    # print("Cannot divide by 0",e)
# print("Welcome")
  
# try:
    # a = int(input("Enter a Numerator"))
    # b= int(input("Enter  a Denominator"))
    # print(a//b)

# except ZeroDivisionError:
    # print("Can't divide by 0")

# except ValueError:
    # print("Enter correct type of value")

# except Exception:
    # pass

# print("Welcome")         

# try:
    # a = int(input("Enter a Numerator"))
    # b= int(input("Enter  a Denominator"))
    # print(a//b)

# except ZeroDivisionError:
    # print("Can't divide by 0")

# except ValueError:
    # print("Enter correct type of value")

# except Exception:
    # pass
# finally:
    # print("PROGRAM ENDS")

# class Acc:
#     a=10
#     _b=20
#     __c=30
# class oft(Acc):
#     pass
# class c:
#     def z(self):
#         print(self._b)

# obj=c()
# obj=oft()
# obj=Acc()
# print(obj.a)
# print(obj._b)

# add=lambda a,b:"Hi" if a+b > 100 else "bye"
# print(add(100,20))

# isEven=lambda a:"Even" if a%2==0 else "odd"
# print(isEven(6))

# num=[1,2,3,4,7,9,11]
# add=list(filter(lambda a: a%2==0,num))
# print(add)

# num = [1, 2, 3, 4, 7, 9, 11]

# sorted_num = sorted(num, key=lambda x: x, reverse=True)
# print(sorted_num)

######LIBRARIES########

import numpy as np
# arr=np.array([10,20,30])
# print(arr)

# z=np.zeros(5)
# print(z)

# z=np.ones(5)
# print(z)

# arr=np.arange(1,10,2)
# print(arr)

import numpy as np
#arr=np.array([10,20,30])
#print(arr)

# z=np.zeros(5)
# print(z)

# o=np.ones(5)
# print(o)

# ar=np.arange(1,10,5)
# print(ar)

# ls=np.linspace(1,10,2)
# print(ls)

# arr=np.arange(1,7)
# print(arr)
# newarr=arr.reshape(2,3)
# print(newarr)
# newarr=arr.reshape(3,2)
# print(newarr)

# arr2=np.array([[1,2,3],[4,5,6]])
# print(arr2)
# print(arr2.shape)
# print(arr2.ndim)

# arr1=np.sum([2,4,5,8,2])
# print(arr1)
# arr2=np.mean([2,4,5,4,3,5])
# print(arr2)
# arr5=np.sqrt([4,9,10,25])
# print(arr5)
# arr6=np.sort([2,20,3,10,15])
# print(arr6)
# arr7=np.unique([1,2,3,2,1])
# print(arr7)


# arr=np.arange(1,10)
# print(arr.view())
# print(arr.copy())
# print(arr.min())
# print(arr.max())
# print(arr.sort())
# print(arr.dtype)

# arr=np.size([1,2,3,4,5])
# print(arr)

#View & Copy
# a=np.array([1,2,3,4,5])
# b=a.view()
# c=a.copy()
# a[0]=95
# print(b)
# print(c)
# print(np.sqrt(a))

# import pandas as pd
# # data = {"Name": ["Pooja", "Anu"], "Age": [20, 21]}
# # df = pd.DataFrame(data)
# # print(df)


# s=pd.Series([10,20,30])
# print(s)
# s1=pd.Series([100,200,300],index=["pooja","viji","sri"])
# print(s1)
# s3=[[1,2,3],[4,5,6],[7,8,9]]


# df=pd.DataFrame(s3)
# print(df)


# data={"Name":["pooja","viji","sri"],"Age":[20,80,21],"Salary":[50000,1000,60000]}
# df=pd.DataFrame(data)
# print(df["Salary"])
# print(df.loc[0])
# print(df.head)
# print(df.tail)
# print(df.shape)
# print(df.columns)
# print(df.info)


# data={"Dept":["IT","HR","IT","IT","HR"],
    #   "Salary":[50000,60000,70000,45000,55000]}
# df=pd.DataFrame(data)
# print(df)

#groupby
# res1=df.groupby("Dept")["Salary"].sum()
# print(res1)
# res2=df.groupby("Dept")["Salary"].mean()
# print(res2)
# print(df.groupby("Dept").agg({"Salary":["min","max","mean","count"]}))