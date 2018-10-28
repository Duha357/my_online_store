from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from products.forms import CategoryForm
#, CategoryModelForm
from products.models import Category


# Create your views here.
def category_create(request):
    template_write_name = 'Create category'
    template_name = 'products/create.html',
    success_url = reverse_lazy('products:product_list')
    form = CategoryForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            title = form.cleaned_data.get('title')
            snippet = form.cleaned_data.get('snippet')

            Category.objects.create(
                title=title,
                snippet=snippet,
            )

            return redirect(success_url)

    return render(request, template_name, {'form': form, 'template_write_name': template_write_name})

# Более меньшая и сокращённая версия, чем выше
# def category_model_create(request):
#     template_name = 'products/create.html',
#     success_url = reverse_lazy('products:list')
#     form = CategoryModelForm(request.POST)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#
#             return redirect(success_url)
#
#     return render(request, template_name, {'form': form})