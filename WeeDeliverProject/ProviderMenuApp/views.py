from ProviderMenuApp.MenuSerializer import MenuItemSerializer, \
    MenuCategorySerializer, StoreSerializer, DeviceSerializers
from ProviderMenuApp.models import MenuItem, MenuCategory, Store, UserDevice
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response



class MenuItem_list(generics.ListCreateAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

class MenuCategory_list(generics.ListCreateAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuItemSerializer
    
class Store_list(generics.ListCreateAPIView): 
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    
    
class Device_list(generics.ListCreateAPIView):
    queryset = UserDevice.objects.all()
    serializer_class = DeviceSerializers
