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

# class Solution:
#   def isPalindrome(self, x):
    # if x < 0:
    #   return False

    # rev = 0
    # y = x

    # while y:
    #   rev = rev * 10 + y % 10
    #   y //= 10

    # return rev == x       
         
# class Solution(object):
#     def hammingWeight(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         count = 0
#         while n:
#             n = n & (n - 1)
#             count += 1
#         return count 
             

# class Solution(object):
#     def hammingWeight(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         count = 0
#         while n:
#             n = n & (n - 1)
#             count += 1
#         return count  

# class Solution(object):
    # def isPowerOfThree(self, n):
        # """
        # :type n: int
        # :rtype: bool
        # """
        # if n <= 0:
            # return False
        
        # while n > 1:
            # if n % 3 != 0:
                # return False
            # n = n // 3
        
        # return True     
