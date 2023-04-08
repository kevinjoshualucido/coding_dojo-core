# 1
for num in range(1, 151):
    print(num)

# 2
for num in range(5, 1_001, 5):
    print(num)

# 3
for num in range(1, 101):
    if num % 10 == 0:
        print("Coding Dojo")
    elif num % 5 == 0:
        print("Coding")
    else:
        print(num)

# 4
sum = 0
for num in range(0, 500_001):
    if num % 2 == 1:
        sum += num
print(sum)
# OR
sum = 0
for num in range(1, 500_001, 2):
    sum += num
print(sum)

# 5
# num = 2022
# while num > 0:
#     num -= 4
#     if not num > 0:
#         break
#     print(num)
# CLEANER CODE:
num = 2018
while num > 0:
    print(num)
    num -= 4
# OR
for num in range(2018, 0, -4):
    print(num)

# 6
low_num = 2
high_num = 16
multiple = 3
for z in range(low_num, high_num + 1):
    if z % multiple == 0:
        print(z)
