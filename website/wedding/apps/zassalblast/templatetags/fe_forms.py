from django import template
register = template.Library()

###
# Template tags that are particularly useful for manipulating
# form elements
###

# return the form element type for comparison in templates
# ie. {% if field|checkFormClass == 'SelectMultiple' %}
#
# You can {{ field|checkFormClass }} if you want to see the
# various values that your form fields are registered as
@register.filter(name='checkFormClass')
def checkFormClass(field):
    return field.field.widget.__class__.__name__

# add css classes to form fields
# ie. {{ field|add_css:"chosen-select" }}
@register.filter(name='add_css')
def add_css(field, css):
    return field.as_widget(attrs={"class": css})


# add required
# ie.
# {% if field.field.required %}
#   {{ field|add_required }}
# {% endif %}
@register.filter(name='add_required')
def add_required(field):
    return field.as_widget(attrs={"aria-required": "true", "required": "required"})


# add attribute to element
# ie. {{ field|add_attr:'placeholder="Sample Text"'' }}
@register.filter(name='add_attr')
def add_attr(field, values):
    return field.as_widget(attrs=values)