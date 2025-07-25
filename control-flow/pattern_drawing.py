pattern = int(input("Enter the size of the pattern: "))
row = 1

while row <= pattern:
    for i in range(pattern):
        print("*", end="")
    print()
    row += 1

