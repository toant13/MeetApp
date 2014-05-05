from ProviderMenuApp.MenuSerializer import MenuItemSerializer, \
    MenuCategorySerializer, StoreSerializer, DeviceSerializers, UserSerializer
from ProviderMenuApp.models import MenuItem, MenuCategory, Store, UserDevice
from ProviderMenuApp.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly, \
    IsOwner
from django.contrib.auth.models import User
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.reverse import reverse


class MenuItem_list(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = (permissions.IsAdminUser,)

class MenuCategory_list(generics.ListCreateAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
    permission_classes = (permissions.IsAdminUser,)


    
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
        
class StoreCategory_list(generics.ListCreateAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer 
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)  

     
    def pre_save(self, obj):
        pKey = self.kwargs['pk']
        s = Store.objects.get(pk=pKey)
        obj.owner = s.owner        
         

    def get_queryset(self):
        pKey = self.kwargs['pk']
        return MenuCategory.objects.filter(store=pKey)


class StoreCategory_detail(generics.RetrieveUpdateDestroyAPIView): 
    serializer_class = MenuCategorySerializer 
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)   
    
    def pre_save(self, obj):
        pKey = self.kwargs['pk']
        s = Store.objects.get(pk=pKey)
        obj.owner = s.owner 
     
    def get_object(self):
        pKey = self.kwargs['pk']
        s = Store.objects.get(pk=pKey)
        obj = get_object_or_404(self.get_queryset())
        obj.owner = s.owner
        self.check_object_permissions(self.request, obj)
        return obj
     
     
    def get_queryset(self):
        pKey = self.kwargs['catpk']
        return MenuCategory.objects.filter(pk=pKey)


class StoreCategoryItem_list(generics.ListCreateAPIView):
    serializer_class = MenuItemSerializer 
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)   
    
    def pre_save(self, obj):
        pKey = self.kwargs['pk']
        catPK = self.kwargs['catpk']
        s = Store.objects.get(pk=pKey)
        m = MenuCategory.objects.get(pk=catPK)
        obj.category = m
        obj.owner = s.owner 
    
    def get_queryset(self):
        pKey = self.kwargs['catpk']
        return MenuCategory.objects.filter(menuItem=pKey)
    
class StoreCategoryItem_detail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MenuItemSerializer 
    def get_queryset(self):
        pKey = self.kwargs['itempk']
        return MenuItem.objects.filter(category=pKey)  
    
    
class Device_list(generics.ListCreateAPIView):
    queryset = UserDevice.objects.all()
    serializer_class = DeviceSerializers
    permission_classes = (permissions.IsAdminUser,)

    
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)
    
    
@api_view(('GET',))
def api_root(request, format=None):
    return Response({
#         'users': reverse('user-list', request=request, format=format),
        'store': reverse('store-list', request=request, format=format),
        'category': reverse('menuCategory-list', request=request, format=format),
        'item': reverse('item-list', request=request, format=format),
    })    
    
    