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

