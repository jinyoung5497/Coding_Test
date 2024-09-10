num1, num2 = input().split()

new_num1, new_num2 = int(num1[::-1]), int(num2[::-1])

if new_num1 > new_num2:
    print(new_num1)
else: print(new_num2)
    