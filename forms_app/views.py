from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm, FeedbackForm
from .models import Book, Product
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView


# Create your views here.
def contact_us(request):
    # u have to handle form submission
    if request.method == 'POST':
        # check if the form is valid if not render it again with the same contents along with error
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse("Alright no errors!")
    else:
        form = ContactForm()

    return render(request, 'contactUs.html', {'form': form})


# CRUD operations on model object

def book_op(request):
    # retrieve data
    book = Book.objects.get(id=1)

    # insert data
    new_book = Book(title="Django for beginners", author="aashish", publication_date="2024-07-01")
    new_book.save()

    # update data
    book.title = "updated title"
    book.save()

    # filtering data
    django_book = Book.objects.filter(title__contains="Django")

    # ordering data
    ordered_books = Book.objects.order_by('-publication_date')


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank you')
    else:
        form = FeedbackForm()

    return render(request, 'contactUs.html', {'form': form})


class ProductListView(ListView):
    model = Product
    template_name = 'contactUs.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'contactUs.html'


class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'contactUs.html'


class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'contactUs.html'


class ProductDeleteView(DeleteView):
    model = Product
    fields = '__all__'
    template_name = 'contactUs.html'


