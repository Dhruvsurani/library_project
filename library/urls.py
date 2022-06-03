from django.urls import path,include
from django.contrib.auth import views as auth_views
from library import views
urlpatterns = [

    path('',views.IndexView.as_view(),name='home'),
    
    path('books/', views.BookListView.as_view(), name='books'),
    path('student/', views.StudentListView.as_view(), name='student'),
    path('book/create/',views.BookCreateView.as_view(),name='book_create'),
    path('student/create/',views.StudentCreateView.as_view(),name='student_create'),
   
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),

]