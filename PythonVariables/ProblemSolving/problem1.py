# hackerrank problem solve
#  problem nembar 1 :
# Task:
# Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

# from asyncio import Task


n =2
if n % 2 !=0:
    print("Weird")
elif n % 2 ==0 and n>=2 and n<=5:
    print("Not Weird") 
elif n % 2 == 0 and n >= 2 and n<=20:
    print("Weird")
else:
    print("Not Weird")


#  problem nembar  2 :
    # Task
# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

a=10
b=20

print(a+b)
print(a-b)
print(a*b)

#  problem nembar   3 :

# Task
# The provided code stub reads an integer, , from STDIN. For all non-negative integers , print .

n=5
for i in range(n) :
    print(i*i)