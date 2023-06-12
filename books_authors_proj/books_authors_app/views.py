from django.shortcuts import render, redirect

from .models import Book, Author


def index(request):
    context = {
        "all_the_Books": Book.objects.all(),
    }
    return render(request, "index.html", context)


def create_book(request):
    Book.objects.create(title=request.POST['title'], desc=request.POST['desc'],
                        )
    return redirect('/')


def authors(request):
    context = {
        "all_the_Authors": Author.objects.all(),
    }
    return render(request, "authors.html", context)


def create_authors(request):
    Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes']
                          )
    return redirect('/authors')


def view_book(request, id):
    book = Book.objects.get(id=id)

    authors = Author.objects.exclude(books__id=id)

    context = {
        'book': book,
        'author': authors
    }
    return render(request, 'book_details.html', context)


def view_author(request, id):
    author = Author.objects.get(id=id)
    context = {
        "author": author,
        "books": Book.objects.exclude(authors__id=id)
    }
    return render(request, 'author_details.html', context)


def assign_book(request, book_id):
    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=request.POST['author_id'])
    book.authors.add(author)
    return redirect(f'/show_book/{book_id}')


def assign_author(request, author_id):
    book = Book.objects.get(id=request.POST['book_id'])
    author = Author.objects.get(id=author_id)
    book.authors.add(author)
    return redirect(f'/show_author/{author_id}')
