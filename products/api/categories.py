import json
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from products.models import Category
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from django.urls import reverse


class CategoryList(ListView):
    model = Category
    paginate_by = 10

    def serialize_object_list(self, queryset):
        return list(
            map(
                lambda itm: {
                    'title': itm.title,
                    'snippet': itm.snippet,
                    'modified': itm.modified,
                    'created': itm.created,
                },
                queryset
            )
        )

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)

        data = {}
        page = context.get('page_obj')
        route_url = reverse('rest_categories:rest_list')

        data['next_url'] = None
        data['previous_url'] = None
        data['page'] = page.number
        data['count'] = page.paginator.count
        data['results'] = self.serialize_object_list(page.object_list)

        if page.has_next():
            data['next_url'] = f'{route_url}?={page.next_page_number()}'

        if page.has_previous():
            data['previous_url'] = f'{route_url}?={page.previous_page_number()}'

        return data

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


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
            {'results': list(data)}
    )
    # return HttpResponse(          - или вот так
    #         json.dumps(
    #             {
    #             'results': list(data)
    #             }
    #         )
    #     )