
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('create_book', views.create_book),
    path('authors', views.authors),
    path('create_author', views.create_authors),
    path('show_book/<int:id>', views.view_book),
    path('show_author/<int:id>', views.view_author),
    path('books/<int:book_id>/assign', views.assign_book),
    path('authors/<int:author_id>/assign', views.assign_author)
]
