from django.shortcuts import render

# Create your views here.
def index(request):
    books = [
        {
            'name': 'Hello Beautiful',
            'author': 'Ann Napolitano',
            'coverImage': 'https://m.media-amazon.com/images/I/51YGx8qVVXL.jpg'
        },
        {
            'name': 'Fourth Wing',
            'author': 'Rebecca Yarros',
            'coverImage': 'https://cdn.kobo.com/book-images/11b52103-2310-4db2-bd9d-3a416cdbc875/1200/1200/False/fourth-wing.jpg'
        },
    ]
    return render(request, 'books/index.html', {
        'show_books': True,
        'books': books
    })


def book_details(request, book_slug):
    print(book_slug)
    selectedBook = {
        'name': 'Hello Beautiful',
        'author': 'Ann Napolitano',
        'coverImage': 'https://m.media-amazon.com/images/I/51YGx8qVVXL.jpg',
        'numPages': 255,
        'desctipion': 'The best book ever',
        'slug': 'hello-beautiful'
    }
    return render(request, 'books/book-details.html', {
        'book': selectedBook
    })
