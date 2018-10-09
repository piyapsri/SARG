from django import template

register = template.Library()

@register.filter(name='iconSucess')
def iconSucess(value, arg):
    return value.replace(arg, '<i class="fa fa-check-circle" style="font-size: 30px; color:#1ABB9C;"></i>')