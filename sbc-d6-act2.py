row = int(input(f"Enter a Row: "))
col = int(input(f"Enter a Col: "))

n = 0
while n <= row:
    x = 0
    while x < row:
        if x == 0 or x == row - 1 or n == 0 or n == col -1:
            print(f"*", end="")
        else:
            print("v", end="")
        x += 1
    print("")
    n += 1