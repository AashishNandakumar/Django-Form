from django.db import models


# Create your models here.
# A model is a python class representation of a DB table
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()

    def __str__(self):
        return self.title


# demonstration of many-to-many relation
class Student(models.Model):
    name = models.CharField(max_length=100)


"""
    database migrations - are a way of propagating changes made to models into DB schema
        -> Allows version control of DB schema changes
        -> Enables rollback of database changes if needed
"""


class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, through='Enrollment')


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)


# products models depicting many data types
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


# feedback model through which we will create the form
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


#  project model through which we will create form with widgets
class Project(models.Model):
    topic = models.CharField(max_length=100)
    languages = models.CharField(max_length=300)
    duration = models.IntegerField(help_text='Duration in weeks')
