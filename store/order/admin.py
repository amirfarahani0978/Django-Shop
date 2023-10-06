from django.contrib import admin
from .models import  Order, OrderItem , Offer 


admin.site.register(Offer)


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ('product',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'created','state','updated','offer','paid')
    list_filter = ('paid',)
    inlines = (OrderItemAdmin,)
