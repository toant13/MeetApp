
from ProviderMenuApp.models.buyer import Cart
from django.contrib import admin
from models import MenuItem, MenuCategory, Store
# Register your models here.


admin.site.register(Cart)
admin.site.register(Store)
admin.site.register(MenuCategory)
admin.site.register(MenuItem)
