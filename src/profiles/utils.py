
import models


# fibonacci function
def fib(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a


print(fib(7))
print(fib(n=models.Transaction.amount))  # here is fibonacci of our amount of money, there is some issue with import
