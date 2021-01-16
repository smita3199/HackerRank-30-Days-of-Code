# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt

def isPrime(n):
    if n is 1:
        return "Not prime"
    for i in range(2, int(sqrt(n)+1)):
        if n % i is 0:
            return "Not prime"
    return "Prime"

t = int(input())
for i in range(t):
    n = int(input())
    print(isPrime(n))
