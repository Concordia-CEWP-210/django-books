from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), # books/
    path('<slug:book_slug>', views.book_details),
]