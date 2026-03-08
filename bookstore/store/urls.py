from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('books-after-2010/', views.books_after_2010_view, name='books_after_2010'),
]
