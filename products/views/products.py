from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy
from products.forms import ProductModelForm
from products.models import Product
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'results'
    paginate_by = 6

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'instanse'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'products/create.html'
    # fields = ['title', 'category', 'image', 'snippet', 'cost', 'Manufacturer', 'country']
    form_class = ProductModelForm
    success_url = reverse_lazy('products:product_list')

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'products/create.html'
    form_class = ProductModelForm
    success_url = reverse_lazy('products:product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('products:product_list')

def product_list(request):
    #  query = Product.objects.all()
    query = get_list_or_404(Product)  # - для вывода ошибки отсутствия контента
    paginator = Paginator(query, 6)
    page = request.GET.get('page')
    items = paginator.get_page(page)

    # return render(request, 'products/product_list.html', {'results': query}) - для вывода страниц, без пагинации
    return render(request, 'products/product_list.html', {'results': items})


def product_detail(request, pk):
    obj = get_object_or_404(Product, pk=pk)

    return render(request, 'products/product_detail.html', {'instanse': obj})


def product_model_create(request):
    template_write_name = 'Create product'
    template_name = 'products/create.html',
    success_url = reverse_lazy('products:product_list')
    form = ProductModelForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(request, template_name, {'form': form, 'template_write_name': template_write_name})


def product_model_update(request, pk):
    template_write_name = 'Update product'
    template_name = 'products/create.html',
    success_url = reverse_lazy('products:product_list')
    obj = get_object_or_404(Product, pk=pk)
    form = ProductModelForm(instanse=obj)

    if request.method == 'POST':
        form = ProductModelForm(
            request.POST,
            instanse=obj
        )
        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(request, template_name, {'form': form, 'template_write_name': template_write_name})


def product_model_delete(request, pk):
    template_write_name = 'Delete product'
    template_name = 'products/delete.html',
    success_url = reverse_lazy('products:product_list')
    obj = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        obj.delete()

        return redirect(success_url)

    return render(request, template_name, {'template_write_name': template_write_name})