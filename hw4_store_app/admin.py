from django.contrib import admin
from .models import *

@admin.action(description='Reset price to 5.00')
def reset_price_to_5(modeladmin, request, queryset):
    queryset.update(price=5.0)

@admin.action(description='Set the status to FINISHED')
def status_to_finished(modeladmin, request, queryset):
    queryset.update(status='FINISHED')

@admin.action(description='Set the status to CANCELED')
def status_to_cancelled(modeladmin, request, queryset):
    queryset.update(status='CANCELED')

@admin.action(description='Set the status to INWORK')
def status_to_in_work(modeladmin, request, queryset):
    queryset.update(status='INWORK')

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'description', 'price']
    readonly_fields = ['date_added']
    fields = ['product_name', 'description', 'price', ('quantity', 'image', 'date_added')]
    search_fields = ['description']
    list_filter = ['price']
    actions = [reset_price_to_5]

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer',  'total_price', 'date_ordered', 'status']
    ordering = ['-status', 'date_ordered']
    readonly_fields = ['date_ordered']
    fields = ['customer', 'products', ('total_price', 'status', 'date_ordered')]
    search_fields = ['customer']
    search_help_text = 'Searching by customers'
    list_filter = ['total_price']
    actions = [status_to_in_work, status_to_finished, status_to_cancelled]

class UserAdmin(admin.ModelAdmin):
    list_display = ['name',  'email', 'phone', 'address', 'birthday']
    readonly_fields = ['name']
    list_per_page = 20
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'phone', 'address'],
                'description': 'customers',
            },
        ),
        (
            'Email, birthday',
            {
                'classes': ['collapse'],
                'description': 'place for description',
                'fields': ['email', 'birthday'],
            }

        )
        ]


admin.site.register(Product, ProductAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)