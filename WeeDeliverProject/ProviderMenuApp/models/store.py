from django.db import models
from gcm.models import AbstractDevice
import os
import uuid
import random
import re


def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid.uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(path, filename)
    return wrapper



class Store (models.Model):
    owner = models.ForeignKey('auth.User', related_name='store')
    storeName = models.CharField(max_length=20, blank=True, default='')
#     folderName = random.randint(0,99999)
    storeAvatar = models.ImageField('Profile', upload_to=path_and_rename('images/main/' ), blank=True, null=True)
    
    
    class Meta:
        ordering = ('storeName',)
        app_label = 'ProviderMenuApp'
    
    def __str__(self):            
        return self.storeName

    def get_folderName(self):
        return re.sub("\W+" , "", self.pk.lower())
    

        

class MenuCategory (models.Model):
    categoryName = models.CharField(max_length=20, blank=True, default='')
    store = models.ForeignKey(Store, related_name='menuCategory')
    
    class Meta:
        ordering = ('categoryName',)
        app_label = 'ProviderMenuApp'
        
    
    def __str__(self):            
        return self.categoryName
    
class MenuItem (models.Model):
    name = models.CharField(max_length=20, blank=True, default='')
    description = models.CharField(max_length=140, blank=True, default='')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(MenuCategory, related_name='menuItem')
    itemImage = models.ImageField('item', upload_to=path_and_rename('images/item/' ), blank=True, null=True)
    
    class Meta:
        ordering = ('name',)
        app_label = 'ProviderMenuApp'
        
    def __str__(self):            
        return self.name
    
class UserDevice(AbstractDevice):
    username = models.CharField(max_length=20, blank=True, default='')
    password = models.CharField(max_length=20, blank=True, default='')
    store = models.ForeignKey(Store, related_name='Device')
    
    class Meta:
        ordering = ('username',)
        app_label = 'ProviderMenuApp'
    
    def __str__(self):
        return self.username