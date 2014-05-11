'''
Created on Apr 29, 2014

@author: toantran
'''

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
        
class UserSerializer(serializers.ModelSerializer):
    store = serializers.PrimaryKeyRelatedField(many=True)
     
    class Meta:
        model = User
        fields = ('id', 'username', 'store')
         
         
        
        