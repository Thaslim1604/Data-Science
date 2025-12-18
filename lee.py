# class Solution(object):
    # def fizzBuzz(self, n):
        # """
        # :type n: int
        # :rtype: List[str]
        # """
        # result=[]
        # for i in range(1,n+1):
            # if i%3==0 and i%5==0:
                # result.append("FizzBuzz")
            # elif i%3==0:
                # result.append("Fizz")
            # elif i%5==0:
                # result.append("Buzz")
            # else:
                # result.append(str(i))
        # return result 
        
# class Solution(object):
    #    def defangIPaddr(self, address):
        #   return address.replace(".","[.]")


# class Solution(object):
    # def numberOfSteps(self, num):
        # """
        # :type num: int
        # :rtype: int
        # """
        # steps = 0
        # while num > 0:
            # if num % 2 == 0:
                # num //= 2  
            # else:
                # num -= 1
            # steps += 1
        # return steps
                
# class Solution(object):
    # def isPowerOfFour(self, n):
        # """
        # :type n: int
        # :rtype: bool
        # """
        # if n <= 0:
            # return False
        # while n % 4 == 0:
            # n //= 4
        # return n == 1  
                          