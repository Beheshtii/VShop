from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView

from product.models import *


class ProductGridView(ListView):
    template_name = 'product/product-grid.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 9

    def get_queryset(self, **kwargs):
        query = super().get_queryset()
        query = query.filter(status=ProductStatusType.active).all().prefetch_related('category')

        # Query Search
        q_search = self.request.GET.get('q')
        if q_search:
            query = query.filter(title__icontains=q_search)

        # Min Price
        min_price = self.request.GET.get('min_price')
        if min_price:
            query = query.filter(price__gte=min_price)

        # Max Price
        max_price = self.request.GET.get('max_price')
        if max_price:
            query = query.filter(price__lte=max_price)

        # Category
        category_id = self.request.GET.get('category_id')
        if category_id:
            query = query.filter(category__id=category_id)


        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_items'] = self.get_queryset().count()
        context['categories'] = ProductCategory.objects.all()

        # Query Search
        q_search = self.request.GET.get('q')

        # Min Price
        min_price = self.request.GET.get('min_price')

        # Max Price
        max_price = self.request.GET.get('max_price')

        category_id = self.request.GET.get('category_id')

        context['q_search'] = q_search
        context['min_price'] = min_price
        context['max_price'] = max_price
        context['category_id'] = category_id



        return context

class ProductListView(View):
    def get(self, request):
        return render(request, 'product/product-list.html')


class ProductDetailView(DetailView):
    template_name = 'product/product-detail.html'
    queryset = Product.objects.filter(status=ProductStatusType.active).all()
    context_object_name = 'product'

