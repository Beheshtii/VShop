from django import template
from product.models import ProductStatusType, Product

register = template.Library()

@register.inclusion_tag('product/includes/latest_product.html')
def show_latest_product():
    latest_products = Product.objects.filter(status=ProductStatusType.active).order_by("-created_date")[:8]

    return {"latest_products": latest_products}

@register.inclusion_tag('product/includes/similar_product.html')
def show_similar_product(product: Product):
    categories = product.category.all()
    similar_products = Product.objects.filter(status=ProductStatusType.active, category__in=categories).exclude(pk=product.pk).order_by("-created_date")[:4]

    return {"similar_products": similar_products}


