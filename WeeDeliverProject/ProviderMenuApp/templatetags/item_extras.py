'''
Created on May 7, 2014

@author: toantran
'''
from django import template
from gcm.models import get_device_model

register = template.Library()




@register.filter
def items_in_category(menuItem, menuCategory):
    return menuItem.filter(category = menuCategory)

@register.filter
def devices_in_store(Device, args):
    return Device.filter(store = args)

@register.filter
def send_phone(Device, args):
    return Device.send_message("testkkdkdkd")