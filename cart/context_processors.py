from cart.cart import CartSession

def cart_session(request):
    cart = request.session.get('cart')
    if cart is None:
        cart = CartSession(request.session)

    return {'cart_session': cart}
