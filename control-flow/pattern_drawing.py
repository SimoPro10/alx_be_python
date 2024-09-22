pattern_size = int(input("Enter the size of the pattern: "))
i=1
while i <= pattern_size:
    for j in range(1,5):
        print("*", end="")
        j+=1
    print()
    i+=1