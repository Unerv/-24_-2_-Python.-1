# TODO Найдите количество книг, которое можно разместить на дискете
disk_size_mb = 1.44
number_of_pages = 100
number_of_rows = 50
number_character = 25
character_size_byte = 4

disk_size_byte = disk_size_mb * 1024 * 1024
book_size = number_of_pages * number_of_rows * number_character * character_size_byte
number_books_disk = (disk_size_byte // book_size)

print("Количество книг, помещающихся на дискету:", (f'{number_books_disk:.0f}'))