from ProviderMenuApp import views
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
import settings
admin.autodiscover()


store_user_list = views.StoreUserViewSet.as_view({
    'get': 'list'
})
store_user_detail = views.StoreUserViewSet.as_view({
    'get': 'retrieve'
})




# router = DefaultRouter()
# router.register(r'users', views.UserViewSet)


urlpatterns = patterns('',
                       
#     url(r'^', include(router.urls)),
    
    
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    
    
    url(r'^superadmin/', include(admin.site.urls)),
    url(r'', include('gcm.urls')),
    
    #ADMIN REST URLs
    url(r'^api/superadmin/item/$', views.MenuItem_list.as_view(), name='item-list'),
    url(r'^api/superadmin/category/$', views.MenuCategory_list.as_view(), name='menuCategory-list'),
    url(r'^api/superadmin/device/$', views.Device_list.as_view(), name='device-list'),
    
    
    
#     url(r'^api/superadmin/users/$', store_user_list, name='store-user-list'),
#     url(r'^api/superadmin/users/(?P<pk>[0-9]+)/$', store_user_detail, name='store-user-detail'),
   
    #STORE OWNER/USER REST API
    url(r'^api/$', 'ProviderMenuApp.views.api_root'),
    url(r'^api/store/$', views.Store_list.as_view(), name='store-list'),
    url(r'^api/store/(?P<pk>[0-9]+)/$', views.Store_Detail.as_view()),
    url(r'^api/store/(?P<pk>[0-9]+)/category/$', views.StoreCategory_list.as_view(), name='store-menu-list'),
    url(r'^api/store/(?P<pk>[0-9]+)/category/(?P<catpk>[0-9]+)/$', views.StoreCategory_detail.as_view()),
    url(r'^api/store/(?P<pk>[0-9]+)/category/(?P<catpk>[0-9]+)/item/$', views.StoreCategoryItem_list.as_view()),
    url(r'^api/store/(?P<pk>[0-9]+)/category/(?P<catpk>[0-9]+)/item/(?P<itempk>[0-9]+)/$', views.StoreCategoryItem_detail.as_view()),
    
    #BUYER API
    url(r'^api/users/$', views.BuyerUser_list.as_view(), name='buyer-user-list'),
    url(r'^api/users/(?P<pk>[0-9]+)/$', views.BuyerUser_Detail.as_view(), name='buyer-user-detail'),
    url(r'^api/users/(?P<pk>[0-9]+)/carts/$', views.UserCart_list.as_view(), name="user-cart-list"), 

    #NONREST URLs
    url(r'^$', views.index, name='index'),
    url(r'^store/(?P<pk>[0-9]+)/$', views.NonApiStoreDetail.as_view(), name='storeDetail'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)


urlpatterns += format_suffix_patterns(urlpatterns)