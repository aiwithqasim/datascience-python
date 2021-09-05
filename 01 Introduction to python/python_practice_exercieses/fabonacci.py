"""
Write a recursive function to compute Ntn Fibonacci number.
Test and trace for N = 6 is 8.
We remember that a Fibonacci number can be recursively defined as: F(n)=F(n-1)+F(n-2)"for" n≥2,
                                                                    where F(0)=0,F(1)=1
"""


def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==0:
        return 0
    # Second Fibonacci number is 1
    elif n==1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

print(Fibonacci(6))