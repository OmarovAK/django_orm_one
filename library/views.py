from django.shortcuts import render

from library.models import Book

from datetime import datetime


def list_books(request):
    books = Book.objects.all()

    my_dict = {
        'title': 'Список книг',
        'books': books,

    }
    return render(request, 'library/index.html', my_dict)


def filter_date(request, date_):
    books_filter = Book.objects.all().filter(date_pub=date_)
    list_date = sorted(list(set(str(i.date_pub) for i in Book.objects.all())))
    if date_ == list_date[0]:
        previous_date = None
    else:
        previous_date = list_date[list_date.index(date_) - 1]

    if date_ == list_date[-1]:
        next_date = None
    else:
        next_date = list_date[list_date.index(date_) + 1]

    my_dict = {
        'title': date_,
        'books': books_filter,
        'previous_date': previous_date,
        'next_date': next_date,
        'now_date': datetime.strptime(date_, "%Y-%m-%d")
    }
    return render(request, 'library/list_book_filter.html', my_dict)
