from django.contrib import admin
from .models import Category ,Comment ,Product ,ProductFeature,Offer

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(ProductFeature)
admin.site.register(Offer)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    raw_id_fields = ('category')