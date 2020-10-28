# Product views
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from .forms import ProductForm, RawProductForm

from .models import Product 

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
         'form': form
    }
    return render(request, "products/product_create.html", context)

def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../../')
    context = {
        'form': form
    }
    return render(request, 'products/product_update.html', context)

def product_list_view(request):
    queryset = Product.objects.all()
    paginator = Paginator(queryset, 10)
    page = request.GET.get('page')
    queryset = paginator.get_page(page)
    context = {
        'object_list': queryset,
    }
    return render(request, 'products/product_list.html', context)


def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        'object': obj
    }
    return render(request, "products/product_delete.html", context)

def dynamic_lookup_view(request, id):
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)

