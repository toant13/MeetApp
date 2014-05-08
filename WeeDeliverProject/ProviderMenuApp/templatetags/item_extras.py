'''
Created on May 7, 2014

@author: toantran
'''
from django import template


register = template.Library()




@register.filter
def items_in_category(menuItem, menuCategory):
    return menuItem.filter(category = menuCategory)