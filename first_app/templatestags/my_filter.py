from django import template 

register = template.Library()

def my_filter(value):
    return value + "Hello World , This is my filter"

register.filter('my_filter', my_filter)