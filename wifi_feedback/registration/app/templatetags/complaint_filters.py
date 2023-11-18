from django import template

register = template.Library()

@register.filter
def get_complaint(dictionary, key):
    return dictionary.get(key, [])