n = int(input("počet hviezd: "))

for i in range(n):
    print(("* ")*(i+1))

for i in range (n):
    print((" " * (n - i)) + ("* "*n))


for i in range(n):
    print("  " * (n-i-1) + "* " * (i+1))


for i in range (n):
    print (" " * n + "*" * (i+1) )
    n -= 1


