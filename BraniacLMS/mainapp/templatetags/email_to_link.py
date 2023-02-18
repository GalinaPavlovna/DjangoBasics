from django import template
from django.utils.safestring import mark_safe
from json import load

register = template.Library()

@register.filter
def email_to_link(value):
    return mark_safe(f"<a href='mailto:{value}'>{value}</a>")


file1=open('/home/galka/Desktop/DjangoBasics/BraniacLMS/mainapp/templatetags/textnews.json')
lst = load(file1)
file1.close

@register.filter
def content_getter(value):
    return mark_safe(lst[value]['content'])

@register.filter
def head_getter(value):
    return mark_safe(lst[value]['head'])