from django.template import Library
register = Library()

###
# Library for inspecting/exploring variables
# and objects that are within your views.
###

# template_dir dumps all of the methods and
# properties of an object
#
# ie. {% template_dir blog_post %}
#
@register.simple_tag
def template_dir(this_object):
    output = dir(this_object)
    return "<code>%s</code>" % str(output)



# template_dict dumps all of the properties
# for an object/variable. This is generally
# more useful for frontend than template_dir
# because we normally don't need access to
# the objects method's on the frontend and
# makes the dump much smaller/quicker to
# scan through to find what you need
#
# ie. {% template_didct blog_post %}
#
@register.simple_tag
def template_dict(this_object):
    output = this_object.__dict__
    return "<code>%s</code>" % str(output)


@register.simple_tag
def template_meta(this_object):
    meta = dir(this_object._meta)
    return "<code>%s</code>" % str(meta)


@register.simple_tag
def template_class(this_object):
    cls = this_object.__class__
    return "<code>%s</code>" % str(cls)


@register.simple_tag
def template_repr(this_object):
    output = this_object.__repr__
    return "<code>%s</code>" % str(output)