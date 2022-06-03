from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView
from .models import Book,Student
# Create your views here.
from django.views.generic.edit import CreateView


class IndexView(TemplateView):

    template_name = 'registration/index.html'

class BookListView(ListView):
    template_name = 'library/book_list.html'
    model = Book
    context_object_name = 'book_list'

class BookCreateView(CreateView):
    template_name = 'library/form.html'
    model = Book
    fields = '__all__'

class StudentCreateView(CreateView):
    template_name = 'library/form.html'
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('student_create')

class StudentListView(ListView):
    template_name = 'library/student_list.html'
    model = Student
    context_object_name = 'student_list'