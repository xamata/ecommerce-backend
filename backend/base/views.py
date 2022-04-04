from django.http import JsonResponse
from .products import products


# Create your views here.
def getRoutes(request):
    routes = [
        "/api/products/",
        "/api/products/create",
        "/api/products/upload/",
        "/api/products/<id>/reviews",
    ]
    return JsonResponse(routes, safe=False)


def getProducts(request):
    return JsonResponse(products, safe=False)
