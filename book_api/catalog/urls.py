from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list),
    path('books/', views.book_create),
    path('books/<int:pk>/', views.book_detail),
    path('books/<int:pk>/', views.book_update),
    path('books/<int:pk>/', views.book_delete),
    path('books/<int:pk>/upload-cover/', views.upload_cover),
]
