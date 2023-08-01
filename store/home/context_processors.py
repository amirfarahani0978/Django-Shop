from product.models import Category

def category(request):
    category_header = Category.objects.all()    
    return {'categories' : category_header}