from django.template import Library
from django.db.models import Count
from thread.models import Category

register = Library()

@register.inclusion_tag('base/tags/category_teg.html')
def categorytag():
    ctx = {}
    ctx['category_list'] = Category.objects.annotate(
            count=Count('topic')).order_by('sort')
    return ctx