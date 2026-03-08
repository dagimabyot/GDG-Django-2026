from django.shortcuts import render
from .models import Book, Author

def books_after_2010_view(request):
    books_after_2010 = Book.objects.filter(published_date__gt=2010)
    return render(request, "store/books_after_2010.html", {"books": books_after_2010})
