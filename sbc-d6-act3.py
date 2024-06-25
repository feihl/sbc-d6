user = int(input(f"Enter a number: "))

for i in range(user, 1, -1):
    print("*" * i)
for h in range(user-1):
    print("*" if h == 0 else " ", end= "")
for x in range(1, user+1):
    print("*" * x)