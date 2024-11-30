from models import Author,Librarian,Library,Book

author = Author.objects.get(id=1)  # تحديد المؤلف (باستخدام ID أو أي خاصية أخرى)
books_by_author = author.books.all()  # استعلام جميع الكتب المرتبطة بالمؤلف


library = Library.objects.get(id=1)  # تحديد المكتبة (باستخدام ID أو أي خاصية أخرى)
books_in_library = library.books.all()  # استعلام جميع الكتب في المكتبة

library = Library.objects.get(id=1)  # تحديد المكتبة
librarian_for_library = library.librarian  # استعلام أمين المكتبة المرتبط بالمكتبة
