from django import template

register = template.Library()

@register.filter
def to_slesh(value):
    return value.replace("_"," ").capitalize()

@register.filter
def from_slesh(value):
    return value.replace(" ","_").capitalize()

@register.filter
def thouthand_seperator(value):
    value = str(value)[::-1]
    answer = ''
    for i in range(len(value)):
        answer+=value[i]
        if i%3==2:
            answer+=' '
    return answer[::-1]