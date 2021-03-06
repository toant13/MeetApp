from ProviderMenuApp.MenuSerializer import MenuItemSerializer, \
    MenuCategorySerializer, StoreSerializer, DeviceSerializers, StoreUserSerializer, \
    BuyerUserSerializer, CartSerializer
from ProviderMenuApp.models import MenuItem, MenuCategory, Store, UserDevice
from ProviderMenuApp.models.buyer import Cart
from ProviderMenuApp.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from django.views.generic.detail import DetailView
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.reverse import reverse
import logging




logger = logging.getLogger('MYAPP')
    
    
def index(request):
    stores = Store.objects.order_by('storeName')[:5]
    context = RequestContext(request, {'stores' : stores,})
    return render(request, 'provider/index.html', context)



class NonApiStoreDetail(DetailView):
    model = Store
    context_object_name = 'storeDetail'
    template_name = 'provider/store.html'
    
      
    def get_context_data(self, **kwargs):
        pKey = self.kwargs['pk']
        storeObj = Store.objects.get(pk=pKey)
        context = super(NonApiStoreDetail, self).get_context_data(**kwargs)
        context['store'] = storeObj
        context['categories'] = MenuCategory.objects.filter(store = storeObj)
        context['items'] = MenuItem.objects.all()
        context['devices'] = UserDevice.objects.all()
        return context


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
        obj.store = s
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
        pKey = self.kwargs['pk']
        catPK = self.kwargs['catpk']
        return MenuCategory.objects.filter(store=pKey, pk=catPK)


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
        pKey = self.kwargs['pk']
        catPK = self.kwargs['catpk']
        m = MenuCategory.objects.filter(store=pKey, pk=catPK)
        return MenuItem.objects.filter(category=m)
    
class StoreCategoryItem_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer 
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)   
    
    def get_object(self):
        logger.debug("StoreCategoryItem_detail get_object") 
        pKey = self.kwargs['pk']
        obj = get_object_or_404(self.get_queryset())
        s = Store.objects.get(pk=pKey)
        obj.owner = s.owner
        self.check_object_permissions(self.request, obj)
        return obj
    
    def get_queryset(self):
        logger.debug("StoreCategoryItem_detail get_queryset")
        pKey = self.kwargs['pk']
        catPK = self.kwargs['catpk']
        itemPK = self.kwargs['itempk']
        m = MenuCategory.objects.filter(store=pKey, pk=catPK)
        return MenuItem.objects.filter(category=m, pk=itemPK)
    
class BuyerUser_list(generics.ListCreateAPIView):
    queryset = User.objects.filter(groups__name="buyers")
    serializer_class = BuyerUserSerializer
    permission_classes = (IsAdminOrReadOnly, ) #admin only for now, but will open later
    
class BuyerUser_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(groups__name="buyers")
    serializer_class = BuyerUserSerializer
    permission_classes = (IsAdminOrReadOnly, ) #admin only for now, but will open later
    
class UserCart_list(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAdminOrReadOnly, ) #admin only for now, but will open later







    
class Device_list(generics.ListCreateAPIView):
    queryset = UserDevice.objects.all()
    serializer_class = DeviceSerializers
    permission_classes = (permissions.IsAdminUser,)

    
class StoreUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.filter(groups__name="sellers")
    serializer_class = StoreUserSerializer
    permission_classes = (permissions.IsAdminUser,)
    

    
    
@api_view(('GET',))
def api_root(request, format=None):
    return Response({
#         'Store Users': reverse('store-user-list', request=request, format=format),
        'Buyer Accounts API': reverse('buyer-user-list', request=request, format=format),
        'Seller Accounts API': reverse('store-list', request=request, format=format),
#         'Category': reverse('menuCategory-list', request=request, format=format),
#         'Item': reverse('item-list', request=request, format=format),
    })    
    
    