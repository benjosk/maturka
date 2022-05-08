m = input("meno: ")

poc = len(m)
print((m+" ") * poc)
print("")
for i in range(poc):
    print(m)
print("")

print("*" * (poc+4))
print("* " + m + " *")
print("*" * (poc+4))
print("")

for i in range(poc):
    print (m[i]*(i+1))
print("")

for i in range(poc):
    print (" " * poc + m[i]*(i+1))
    poc -=1
print("")

poc = len(m)

for i in range(poc):
    print(m[:i+1])
print("")

for i in range(poc):
    print(" " * poc + m[:i+1])
    poc -=1
print("")

print(m[::-1])
