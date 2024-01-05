books_on_the_shelf = input().split('&')
user_input = input()
while user_input != 'Done':
    user_input = user_input.split(' | ')
    command = user_input[0]
    book = user_input[1]
    if command == 'Add Book':
        if book not in books_on_the_shelf:
            books_on_the_shelf.insert(0,book)
    elif command == 'Take Book':
        if book in books_on_the_shelf:
            books_on_the_shelf.remove(book)
    elif command == 'Swap Books':
        book1 = user_input[1]
        book2 = user_input[2]
        if book1 in books_on_the_shelf and book2 in books_on_the_shelf:
            index1 = books_on_the_shelf.index(book1)
            index2 = books_on_the_shelf.index(book2)
            books_on_the_shelf[index1],books_on_the_shelf[index2] = books_on_the_shelf[index2],books_on_the_shelf[index1]
    elif command == 'Insert Book':
        if book not in books_on_the_shelf:
            books_on_the_shelf.append(book)
    elif command == 'Check Book':
        index = int(user_input[1])
        if 0 <= index < len(books_on_the_shelf):
            print(books_on_the_shelf[index])
    user_input = input()
print(', '.join(books_on_the_shelf))
