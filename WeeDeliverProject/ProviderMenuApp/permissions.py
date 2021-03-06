'''
Created on May 1, 2014

Custom permission classes


@author: toantran
'''

from rest_framework import permissions
from ProviderMenuApp.models import Store
import logging
logger = logging.getLogger('MYAPP')

STOREURLPOSITION = 3

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_permission(self, request, view, obj=None):
        if request.method in permissions.SAFE_METHODS:
            return True

        logger.debug("FULL PATH: " + request.path)
        urlPk = request.path.split('/')
        logger.debug("FULL STORE PK: " + urlPk[STOREURLPOSITION])
        s = Store.objects.get(pk=urlPk[STOREURLPOSITION])
        return (s.owner == request.user) or (request.user and request.user.is_staff)
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return (obj.owner == request.user) or (request.user and request.user.is_staff)
            

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return (request.user and request.user.is_staff)
    
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return False

        return obj.owner == request.user
    

    
    