print("Enter an input")
a = int(input())
n = 1
if a % 2 == 0:
    a = a - 1
for i in range(a):
   print(n, end=' ')
   n = n + 2