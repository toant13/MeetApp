from ProviderMenuApp.MenuSerializer import MenuItemSerializer, \
    MenuCategorySerializer, StoreSerializer, DeviceSerializers, UserSerializer
from ProviderMenuApp.models import MenuItem, MenuCategory, Store, UserDevice
from ProviderMenuApp.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from django.contrib.auth.models import User
from rest_framework import generics, permissions


class MenuItem_list(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    

class MenuCategory_list(generics.ListCreateAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
    
class Store_list(generics.ListCreateAPIView): 
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = (IsAdminOrReadOnly, )
    
    def pre_save(self, obj):
        obj.owner = self.request.user

class Store_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer        
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user
    
class Device_list(generics.ListCreateAPIView):
    queryset = UserDevice.objects.all()
    serializer_class = DeviceSerializers

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
    