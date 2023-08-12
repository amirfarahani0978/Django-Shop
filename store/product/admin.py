from django.contrib import admin
from .models import Category ,Comment ,Product ,ProductFeature , WishList

admin.site.register(Category)
# admin.site.register(Comment)
admin.site.register(ProductFeature)
admin.site.register(WishList)
#admin.site.register(Product)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ('product_id',)
    list_display = ('comment' , 'profile_id' , 'product_id' , 'created_time')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields =('category__name',)
    list_display = ('name' , 'slug' , 'price' , 'count_buying' , 'status_available','quantity','rate','product_feature',)