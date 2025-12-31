from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from cart.cart import CartSession


class SessionAddProductView(View):

    def post(self, request, *args, **kwargs):
        session_cart = CartSession(request.session)
        cart = session_cart.get_cart()
        product_id = request.POST.get('product_id', None)
        session_cart.add_product(product_id)

        return JsonResponse({'cart': cart})

