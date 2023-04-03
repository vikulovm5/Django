from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import DetailView

from mainapp.models import Product, ProductCategory
from adminapp.forms import ProductEditForm


def products(request, pk):
    title = 'админка/продукты'

    category = get_object_or_404(ProductCategory, pk=pk)
    product_list = Product.objects.filter(category__pk=pk).order_by('name')
    content = {
        'title': title,
        'category': category,
        'objects': product_list
    }
    return render(request, 'adminapp/products.html', content)


def product_create(request, pk):
    title = 'продукт/создание'
    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponse(reverse('admin:products', args=[pk]))
    else:
        product_form = ProductEditForm(initial={'category': category})
    content = {'title': title, 'update_form': product_form, 'category': category}
    return render(request, 'adminapp/product_update.html', content)


def product_update(request, pk):
    title = 'продукт/редактирование'

    edit_product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponse(reverse('admin:product_update', args=[edit_product.pk]))
    else:
        edit_form = ProductEditForm(instance=edit_product)

    content = {'title': title, 'update_form': edit_form, 'category': edit_product.category}
    return render(request, 'adminapp/product_update.html', content)


def product_delete(request, pk):
    title = 'продукт/удаление'

    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.is_active = False
        product.save()
        return HttpResponse(reverse('admin:products', args=[product.category.pk]))

    content = {'title': title, 'product_or_delete': product}
    return render(request, 'adminapp/product_delete.html', content)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'adminapp/product_read.html'
