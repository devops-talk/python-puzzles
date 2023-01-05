"""
Nth Fibonacci Number
Nth term of Fibonacci series F(n), where F(n) is a function, is calculated using the following formula -
    F(n) = F(n-1) + F(n-2), 
    Where, F(1) =  1, 
           F(2) = 1
Provided N you have to find out the Nth Fibonacci Number.
"""
Fib_Array = [1,1]
def fibonacci(n):
   if n<0:
      print("Fibbonacci can't be computed")
   elif n<=len(Fib_Array):
      return Fib_Array[n-1]
   else:
      temp = fibonacci(n-1)+fibonacci(n-2)
      Fib_Array.append(temp)
      return temp
# Driver Program
n=int(input())
print(fibonacci(n))