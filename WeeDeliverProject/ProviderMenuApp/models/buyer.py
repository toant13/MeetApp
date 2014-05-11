'''
Created on May 11, 2014

@author: toantran
'''
from django.db import models
from store import MenuItem, Store

class Cart (models.Model):
    store = models.ForeignKey(Store, related_name='store')
    msg_to_store = models.CharField(max_length=160, unique=True)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    delivery_cost = models.DecimalField(max_digits=8, decimal_places=2)
    
    class Meta:
        app_label = 'ProviderMenuApp'

class CartItems (models.Model):
    cart = models.ForeignKey(Cart, related_name='cart')
    item = models.ForeignKey(MenuItem, related_name='cartItem')
    quantity = models.PositiveSmallIntegerField(default=1, blank=True, null=True)
    
    class Meta:
        app_label = 'ProviderMenuApp'