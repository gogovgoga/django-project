from timeit import default_timer

from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpRequest

from .forms import ProductForm, OrderForm
from shopapp.models import Product, Order


def shop_index(request: HttpRequest):
    products = Product.objects.all()
    context = {
        'time_running': default_timer(),
        'products': products,
    }
    return render(request, 'shopapp/shop-index.html', context=context)


def groups_list(request: HttpRequest):
    context = {
        'groups': Group.objects.prefetch_related('permissions').all(),
    }
    return render(request, 'shopapp/groups-list.html', context=context)


def products_list(request: HttpRequest):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'shopapp/products-list.html', context=context)


def create_product(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            url = reverse("shopapp:products_list")
            print("Redirect URL:", url)
            return redirect(url)
        else:
            print("Form is not valid:", form.errors)
    else:
        form = ProductForm()
    context = {
        "form": form,
    }
    return render(request, 'shopapp/create-product.html', context=context)


def orders_list(request: HttpRequest):
    context = {
        'orders': Order.objects.select_related("user").prefetch_related('products').all(),
    }
    return render(request, 'shopapp/orders-list.html', context=context)


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.user = request.user
            selected_products = request.POST.getlist('products')
            order.products.set(selected_products)
            order.save()
            return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'shopapp/create-order.html', {'form': form})