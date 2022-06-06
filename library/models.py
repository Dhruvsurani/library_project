from datetime import date
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from mylibrary import settings


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        return self.name


    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    summary = models.TextField(max_length=1000, help_text="description of the book")
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character ISBN number')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    publish_date = models.DateField(null=True)
    total_copies = models.IntegerField()
    available_copies = models.IntegerField()
    pic=models.ImageField(blank=True, null=True, upload_to='book_image')
    def pic_url(self):
        if self.pic:
            return self.pic.url
        return ''
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
CHOICES = (
    ('Author', 'Author'),
    ('Buyer', 'Buyer'),
    ('Admin', 'Admin'),)

class Student(models.Model):
    roll_no = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=10)
    branch = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=10)
    total_books_due=models.IntegerField(default=0)
    email=models.EmailField(unique=True)
    user_type=models.CharField(max_length=20, choices=CHOICES, default='Buyer')
   
    def __str__(self):
        return str(self.name)
def create_user(sender, *args, **kwargs):
    if kwargs['created']:
        User.objects.create(username=kwargs['instance'],password="dummypass")
post_save.connect(create_user, sender=Student)

class Borrower(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    issue_date = models.DateTimeField(null=True,blank=True)
    return_date = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.student.name+" borrowed "+self.book.title