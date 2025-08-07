a = int(input("Enter the number whose table you want: "))
b = int(input("Till how many numbers do you want to see the table numbers for: "))

for i in range(1, b+1):
    print(f"{a} x {i} = {a*i}")