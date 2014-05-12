'''
Created on Apr 29, 2014

@author: toantran
'''

from ProviderMenuApp.models.buyer import Cart
from django.contrib.auth.models import User
from models import MenuItem, MenuCategory, Store, UserDevice
from rest_framework import serializers

class StoreSerializer(serializers.ModelSerializer):
    menuCategory = serializers.RelatedField(many=True)
    owner = serializers.Field(source='owner.username')
    
    class Meta:
        model = Store
        fields = ('id','storeAvatar', 'storeName', 'menuCategory','owner')
    
    def pre_save(self, obj):
        obj.owner = self.request.user

class MenuCategorySerializer(serializers.ModelSerializer):
    menuItem = serializers.RelatedField(many=True)
    class Meta:
        model = MenuCategory
        fields = ('id','categoryName', 'menuItem')
    

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('id','itemImage', 'name', 'description', 'price')
        
class DeviceSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserDevice
        fields = ('id','username', 'password', 'name', 'dev_id', 'reg_id', 'store')
        
class StoreUserSerializer(serializers.ModelSerializer):
    store = serializers.PrimaryKeyRelatedField(many=True)
     
    class Meta:
        model = User
        fields = ('id', 'username', 'store')
        
class BuyerUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'username', 'cart')
        
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id','owner', 'store', 'msg_to_store', 'subtotal', 'total', 'delivery_cost', 'CartItems')
            
         
        
        