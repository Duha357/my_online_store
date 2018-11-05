from django.shortcuts import get_list_or_404
from django.http import JsonResponse
from products.models import Product


def rest_product_list(request):
    query = get_list_or_404(Product)

    data = map(
        lambda itm: {
            'title': itm.title,
            'category': itm.category.title,
            'image': itm.image.url,
            'cost': itm.cost,
            'manufacturer': itm.Manufacturer.name,
            'modified': itm.modified,
            'created': itm.created,
        },
        query
    )
    return JsonResponse(
        {'results': list(data)}
    )
