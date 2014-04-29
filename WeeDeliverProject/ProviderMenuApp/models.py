from django.db import models
from gcm.models import AbstractDevice


class MyDevice(AbstractDevice):
    pass


class Store (models.Model):
    storeName = models.CharField(max_length=20, blank=True, default='')
    
    class Meta:
        ordering = ('storeName',)
    
    def __str__(self):            
        return self.storeName


class MenuCategory (models.Model):
    categoryName = models.CharField(max_length=20, blank=True, default='')
    store = models.ForeignKey(Store, related_name='menuCategory')
    
    class Meta:
        ordering = ('categoryName',)
    
    def __str__(self):            
        return self.categoryName
    
class MenuItem (models.Model):
    name = models.CharField(max_length=20, blank=True, default='')
    description = models.CharField(max_length=140, blank=True, default='')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(MenuCategory, related_name='menuItem')
    
    class Meta:
        ordering = ('name',)
        
    def __str__(self):            
        return self.name
    
