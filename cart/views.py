import json
from functools import reduce
from django.apps import apps
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, ListView, View
from .models import Purchase, PurchaseItem
from .forms import PurchaseItemForm


class PurchaseListView(ListView):
    model = Purchase
    template_name = 'cart/cart_list.html'


class PurchaseMainCartView(ListView):
    model = Purchase
    template_name = 'cart/cart_create.html'


# class PurchaseCreateView(CreateView):
#     '''
#     Реализация создания заказа для администрации
#     '''
#     model = Purchase
#     fields = ['user', 'is_active']
#     template_name = 'cart/cart_create_forms.html'
#     success_url = reverse_lazy('cart:cart_list')
#
#     def get(self, request):
#         self.object = None
#         context = self.get_context_data()
#         formset = inlineformset_factory(
#             model=PurchaseItem,
#             parent_model=self.model,
#             form=PurchaseItemForm
#         )
#         context.update({
#             'formset': formset
#         })
#         return render(request, self.template_name, context)
#
#     def post(self, request):
#         self.object = None
#         form = self.get_form()
#         formset_class = inlineformset_factory(
#             model=PurchaseItem,
#             parent_model=self.model,
#             form=PurchaseItemForm
#         )
#         formset = formset_class(request.POST)
#         if form.is_valid():
#             form.save()
#             if formset.is_valid():
#                 formset.save()
#
#                 return redirect(self.success_url)
#         return redirect(request, self.template_name, {'form': form, 'formset': formset})


class PurchaseCreateView(LoginRequiredMixin, View):
    login_url = ''
    product_model = apps.get_model('products', 'product')

    def post(self, request):
        data = json.loads(request.body)

        product_list = self.product_model.objects.filter(
            reduce(
                lambda store, key: store | Q(pk=key),
                data.keys(),
                Q()
            )
        )

        obj = Purchase.objects.create(
            user=request.user,
        )

        for product in product_list:
            obj.items.create(
                product=product,
                value=data[str(product.id)],
            )

        return JsonResponse(
            {
                'success_url': reverse(
                    'cart:detail',
                    kwargs={'pk': obj.id}
                )
            }
        )


class PurchaseDetailView(DetailView):
    model = Purchase
    template_name = 'cart/cart_detail.html'
