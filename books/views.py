from django.shortcuts import render

# Create your views here.
def index(request):
    books = [
        {'name': 'Hello Beautiful', 'author': 'Ann Napolitano'},
        {'name': 'Fourth Wing', 'author': 'Rebecca Yarros'},
    ]
    return render(request, 'books/index.html', {
        'show_books': True,
        'books': books
    })