from django.shortcuts import render
from .models import Book

# Create your views here.


def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {
        'books': books
    })


def book_details(request, book_slug):
    selectedBook = Book.objects.get(slug=book_slug)
    return render(request, 'books/book-details.html', {
        'book': selectedBook
    })
