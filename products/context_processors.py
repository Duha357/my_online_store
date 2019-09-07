from .models import Category


def categories(request):
    query = Category.objects.all()
    return {'categories': query}