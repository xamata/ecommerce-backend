import graphene
from graphene_django import DjangoObjectType
from .models import Product

# from graphql.execution.base import ResolveInfo
# from graphql_auth.bases import Output
# from graphene_file_upload.scalars import Upload

# from .forms import CreateCompanyMutationForm


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = "__all__"


class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    product = graphene.Field(ProductType, product_id=graphene.Int())

    def resolve_all_products(self, info, **kwargs):
        return Product.objects.all()

    def resolve_book(self, info, product_id):
        return Product.objects.get(pk=product_id)


class ProductInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    brand = graphene.String()
    category = graphene.String()
    description = graphene.String()
    price = graphene.Decimal()
    countInStock = graphene.Int()


class CreateProduct(graphene.Mutation):
    class Arguments:
        product_data = ProductInput(required=True)


schema = graphene.Schema(query=Query)
