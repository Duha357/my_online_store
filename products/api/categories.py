import json
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from products.models import Category
from django.http import HttpResponse, JsonResponse

def rest_category_list(request):
    query = get_list_or_404(Category)
    data = map(
        lambda itm: {
            'title': itm.title,
            'snippet': itm.snippet,
            'modified': itm.modified,  # для HttpResponse необходимо поместить значение в str
            'created': itm.created,  # для HttpResponse необходимо поместить значение в str
        },
        query
    )
    return JsonResponse(
            {
            'results': list(data)
            }
    )
    # return HttpResponse(          - или вот так
    #         json.dumps(
    #             {
    #             'results': list(data)
    #             }
    #         )
    #     )