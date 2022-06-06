
from django.urls import reverse_lazy

from django.views.generic import TemplateView,ListView
from .models import Book,Student,Borrower
# Create your views here.
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(TemplateView):

    template_name = 'registration/index.html'

class BookListView(ListView):
    template_name = 'library/book_list.html'
    model = Book
    context_object_name = 'book_list'


class BookCreateView(LoginRequiredMixin,CreateView):
    login_url = '/accounts/login/'
    template_name = 'library/form.html'
    model = Book
    fields = '__all__'


class StudentCreateView(LoginRequiredMixin,CreateView):
    login_url = '/accounts/login/'
    template_name = 'library/form.html'
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('student_create')


class StudentListView(LoginRequiredMixin,ListView):
    login_url = '/accounts/login/'
    template_name = 'library/student_list.html'
    model = Student
    context_object_name = 'student_list'


class BookIsueView(LoginRequiredMixin,CreateView):
    login_url = '/accounts/login/'
    template_name = 'library/form.html'
    model = Borrower
    fields = ['student','book','issue_date','return_date']
    success_url = reverse_lazy('issue-book')


class IssuedBookListView(LoginRequiredMixin,ListView):
    login_url = '/accounts/login/'
    template_name = 'library/issuedbook_list.html'
    model = Borrower
    context_object_name = 'issuebook_list'


