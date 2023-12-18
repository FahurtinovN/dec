from django.shortcuts import render, redirect
from .forms import AddProduct
from .models import Product


def index(request):
    if request.method == 'POST':
        return redirect('product')
    else:
        product = Product.objects.all()
        return render(request, 'app/index.html', context={'product': product})


def product(request):
    if request.method == "POST":
        form = AddProduct(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']

            prod, _ = Product.objects.get_or_create(name=name, price=price, description=description)

            return redirect('index')
    else:
        form = AddProduct()
        return render(request, 'app/product.html', context={'form': form})
