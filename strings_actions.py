def main():

    print("Enter 10 book titles.")

    # list
    books = []
    count = 0

# STRINGS ARE CASE SENSITIVE
    while count < 10:
        title = input(f"Enter the title of the book: {count + 1}: ")

        title = title.title()  # .title makes first letter cap,.upper makes all letters cap
        books.append(title)
        count += 1

    
    sorted_books = sorted(books)

    print("Books in alphabetical order:")
    for book in sorted_books:
        print(book)


main()