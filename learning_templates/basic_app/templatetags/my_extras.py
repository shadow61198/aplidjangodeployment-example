from django import template


register = template.Library()

@register.filter(name='cut') #to registersame as register.flter('cut',cuts)
def cut(value,arg):
    """
    this cuts out all values of arg from sting!
    """
    return value.replace(arg,'')
# register.filter('cut',cut)
