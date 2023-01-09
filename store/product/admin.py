from django.contrib import admin
from .models import Category ,Comment ,Product ,ProductFeature

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(ProductFeature)
#admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields =('category',)