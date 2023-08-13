from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Product , Comment , WishList
from order.forms import CartAddForm
from django.http import JsonResponse
# Create your views here.
class ProductDetailView(View):
    def get(self, request, slug):
        product = Product.objects.get(slug = slug)
        comment = Comment.objects.filter(product_id = product.id)
        form = CartAddForm()
        return render(request, 'product/detail.html', {'product': product , 'form':form , 'comment':comment})
    

class AddWishListView(View):
    def post(self , request):
        if request.is_ajax():
            product_id = request.POST.get('product_id')
            product = Product.objects.get(id=product_id)
            user = self.request.user
            wishlist, created = WishList.objects.get_or_create(user_id=user)
            wishlist.product.add(product)
            return JsonResponse({'message': 'Product added to wishlist!'})
        else:
            return JsonResponse({'error': 'Invalid request'}, status=400)
