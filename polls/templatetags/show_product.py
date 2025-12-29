from django import template
from product.models import ProductStatusType, Product

register = template.Library()

@register.inclusion_tag('product/includes/latest_product.html')
def show_latest_product():
    latest_products = Product.objects.filter(status=ProductStatusType.active).order_by("-created_date")[:8]

    return {"latest_products": latest_products}

