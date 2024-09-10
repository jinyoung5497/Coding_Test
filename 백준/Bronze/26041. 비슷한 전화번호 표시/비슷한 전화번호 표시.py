str_list = input().split()
phone_num = input()
count = 0
for i in str_list:
    if phone_num != i and i[:len(phone_num)] == phone_num:
        count += 1

print(count)
