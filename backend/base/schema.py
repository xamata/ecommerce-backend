from itertools import product
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

    def resolve_product(self, info, product_id):
        return Product.objects.get(pk=product_id)


class ProductInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    image = graphene.String()
    brand = graphene.String()
    category = graphene.String()
    description = graphene.String()
    price = graphene.Decimal()
    countInStock = graphene.Int()
    url = graphene.String()


class CreateProduct(graphene.Mutation):
    class Arguments:
        product_data = ProductInput(required=True)

    product = graphene.Field(ProductType)

    # mutator to add to the database
    @staticmethod
    def mutate(root, info, product_data=None):
        product_instance = Product(
            title=product_data.title,
            author=product_data.author,
            year_published=product_data.year_published,
            review=product_data.review,
        )
        product_instance.save()
        # use CreateProduct class to save a new product
        return CreateProduct(product=product_instance)


class UpdateProduct(graphene.Mutation):
    class Arguments:
        product_data = ProductInput(required=True)

    product = graphene.Field(ProductType)

    @staticmethod
    def mutate(root, info, product_data=None):
        product_instance = product.objects.get(pk=product_data.id)

        if product_instance:
            product_instance.name = product_data.name
            product_instance.author = product_data.author
            product_instance.year_published = product_data.year_published
            product_instance.review = product_data.review
            product_instance.save()

            return UpdateProduct(product=product_instance)
        return UpdateProduct(product=None)


class DeleteBook(graphene.Mutation):
    # DeleteBook uses graphene.ID to remove the product from db
    class Arguments:
        id = graphene.ID()

    product = graphene.Field(ProductType)

    @staticmethod
    def mutate(root, info, id):
        product_instance = Product.objects.get(pk=id)
        product_instance.delete()
        return None


class Mutation(graphene.ObjectType):
    update_book = UpdateProduct.Field()
    create_book = CreateProduct.Field()
    delete_book = DeleteBook.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
