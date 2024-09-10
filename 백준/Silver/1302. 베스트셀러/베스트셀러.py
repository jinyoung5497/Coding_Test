input_num = int(input())
book_list = [input() for _ in range(input_num)]
book_dict = {}

for item in book_list:
    if item not in book_dict:
        book_dict[item] = 1
    else:
        book_dict[item] += 1

sorted_books = sorted(book_dict.items(), key=lambda x: (-x[1], x[0]))
print(sorted_books[0][0])