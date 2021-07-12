print("Enter the number of inputs:")
n = int(input())
myList = []
print("Enter the inputs:")
for i in range(n):
    myList.append(int(input()))

dictionary = {}
for i in range(1, 10):
    count = 0
    for j in range(n):
        if myList[j] % i == 0:
            count += 1
    dictionary[str(i)] = count
print("Output")
print(dictionary)