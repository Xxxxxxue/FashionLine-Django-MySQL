# Personalizar tags para usar en el template

from django import template

register = template.Library()

# cambiar letras o espacios que no necesitamos
def change(text,arg):
    if arg == 'ñ':
        return text.replace(arg,'n')
    else:
        return text.replace(arg, '-')

register.filter('change', change)

# cambiar texto de categoria
def singular(value):
    if value == 'diseñadores':
        value = 'diseñador'
    elif value == 'talleres':
        value = 'taller'
    else:
        value = 'empresa'
    return value

register.filter('singular', singular)