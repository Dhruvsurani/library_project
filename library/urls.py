from django.urls import path,include
from django.contrib.auth import views as auth_views
from library import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',views.IndexView.as_view(),name='home'),
    
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
    path('book/<pk>/update',views.BookUpdateView.as_view(),name = 'book_update'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('student/', views.StudentListView.as_view(), name='student'),
    path('issued-books/',views.IssuedBookListView.as_view(),name = 'issued-books'),
    path('book/create/',views.BookCreateView.as_view(),name='book_create'),
    path('student/create/',views.StudentCreateView.as_view(),name='student_create'),
    path('issue-book/create/',views.BookIsueView.as_view(),name = 'issue-book'),
    path('myissue/',views.myissues,name='my-issue'),

]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)