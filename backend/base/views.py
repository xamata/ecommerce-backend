from django.http import JsonResponse
from .products import products


# Create your views here.
def getRoutes(request):
    routes = [
        "/base/products/",
        "/base/products/create",
        "/base/products/upload/",
        "/base/products/<id>/reviews",
    ]
    return JsonResponse(routes, safe=False)


def getProducts(request):
    return JsonResponse(products, safe=False)
