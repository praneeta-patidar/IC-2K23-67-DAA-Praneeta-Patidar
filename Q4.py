# Part 4: Count the Steps FOR i = 1 to 5 PRINT i
# 1. How many times does this loop run?
# 2. If the loop ran from 1 to n and n = 20, how many times will it run?
# FOR i = 1 to 5 FOR j = 1 to 5 PRINT i, j
# 3. How many times does the inner PRINT run in total?
# 4. If both loops ran from 1 to n and n = 10, how many times will PRINT run?

print("1.")
print("FOR i = 1 to 5")
count = 0
for i in range(1, 6):
    print(i)
    count += 1
print("Loop runs", count, "times")

print("\n2.")
print("FOR i = 1 to n, n = 20")
n = 20
count = 0
for i in range(1, n + 1):
    count += 1
print("Loop runs", count, "times")

print("\n3.")
print("FOR i = 1 to 5, FOR j = 1 to 5, PRINT i, j")
count = 0
for i in range(1, 6):
    for j in range(1, 6):
        print(i, j)
        count += 1
print("PRINT runs", count, "times")


print("\n4.")
print("FOR i = 1 to n, FOR j = 1 to n, n = 10")
n = 10
count = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        count += 1
print("PRINT runs", count, "times")