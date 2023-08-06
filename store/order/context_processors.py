from .models import Cart

def cart(request):
    cart= Cart.objects.get_or_create(user=request.user, completed=False)
    return {'cart':cart}