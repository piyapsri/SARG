from django import template

register = template.Library()

@register.filter(name='iconOK')
def iconOK(value, arg):
    return value.replace(arg, r'<i class="fa fa-check-circle" style="color:#1ABB9C;"></i>')