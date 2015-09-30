import re
from django import template
register = template.Library()

# active_nav outputs `is-active` when the website slug (exclusive of /'s)
# matches the submitted pattern, for example:
#
# <a href="/contact/" class="{% active_nav request "contact" %}">Contact</a>
#
# The above would render, if the user is on the `/contact/` page, as:
#
# <a href="/contact/" class="is-active">Contact</a>
#
# This is useful for basic pages that are unlikely to change. However,
# if you are using url looksup (`<a href="{% url 'feed' %}">`), then
# you should use the `reverse_active_nav` tag below.
@register.simple_tag
def active_nav(request, pattern):
    if re.search('^/%s/' % (pattern,), request.path):
        return 'is-active'
    elif request.path == '/':
        return 'is-home'
    return ''




# reverse_active_nav outputs `is-active` when the reverse `url` looks
# matches the submitted pattern, for example:
#
# <a href="{% url 'feed' %}" class="{% reverse_active_nav request url "feed" %} w-ActionNav__link">Explore Topics</a>
#
# The above would render, if the user is on the `/contact/` page, as:
#
# <a href="/contact/" class="is-active">Contact</a>
@register.simple_tag
def reverse_active_nav(request, pattern, url_name, *args, **kwargs):
    url = reverse_lazy(url_name, args=args)
    if re.search('^/%s/' % (pattern,), str(url)):
        return 'is-active'

    return ''