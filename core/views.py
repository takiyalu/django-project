from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm, ProductModelForm
from .models import Product

# Create your views here.
def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'index.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_email()
            messages.success(request, 'E-mail successfully sent!')
            form = ContactForm()
        else:
            messages.error(request, 'Error while sending the e-mail!')
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)


def product(request):
    if str(request.user) != 'AnonymousUser':
        print(f'User: {request.user}')
        if str(request.method) == 'POST':
            form = ProductModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Product successfully saved')
            else:
                messages.error(request, 'Error while trying to save the product')
        form = ProductModelForm()
        context = {
            'form': form
        }
        return render(request, 'product.html', context)
    else:
        return redirect('index')