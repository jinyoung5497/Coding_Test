card_num = int(input())
fruit_dict = {}

for i in range(card_num):
    fruit, num = input().split()
    if fruit in fruit_dict:
        fruit_dict[fruit] += int(num)
    else:
        fruit_dict[fruit] = int(num)

if 5 in fruit_dict.values():
    print("YES")
else:
    print("NO")