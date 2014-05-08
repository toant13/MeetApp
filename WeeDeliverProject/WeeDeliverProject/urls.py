from ProviderMenuApp import views
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
import settings
admin.autodiscover()


user_list = views.UserViewSet.as_view({
    'get': 'list'
})
user_detail = views.UserViewSet.as_view({
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
    url(r'^developer/item/$', views.MenuItem_list.as_view(), name='item-list'),
    url(r'^developer/category/$', views.MenuCategory_list.as_view(), name='menuCategory-list'),
    url(r'^developer/device/$', views.Device_list.as_view(), name='device-list'),
    url(r'^developer/users/$', user_list, name='user-list'),
    url(r'^developer/users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
   
    #STORE USER REST URLs
    url(r'^developer/$', 'ProviderMenuApp.views.api_root'),
    url(r'^developer/store/$', views.Store_list.as_view(), name='store-list'),
    url(r'^developer/store/(?P<pk>[0-9]+)/$', views.Store_Detail.as_view()),
    url(r'^developer/store/(?P<pk>[0-9]+)/category/$', views.StoreCategory_list.as_view(), name='store-menu-list'),
    url(r'^developer/store/(?P<pk>[0-9]+)/category/(?P<catpk>[0-9]+)/$', views.StoreCategory_detail.as_view()),
    url(r'^developer/store/(?P<pk>[0-9]+)/category/(?P<catpk>[0-9]+)/item/$', views.StoreCategoryItem_list.as_view()),
    url(r'^developer/store/(?P<pk>[0-9]+)/category/(?P<catpk>[0-9]+)/item/(?P<itempk>[0-9]+)/$', views.StoreCategoryItem_detail.as_view()),

    #NONREST URLs
    url(r'^$', views.index, name='index'),
    url(r'^store/(?P<pk>[0-9]+)/$', views.NonApiStoreDetail.as_view(), name='storeDetail'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)


urlpatterns += format_suffix_patterns(urlpatterns)