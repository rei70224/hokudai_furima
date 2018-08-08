from django import template
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.conf import settings

register = template.Library()

@register.inclusion_tag('product/_product_list.html')
def show_product_list(request, product_list):
    paginator = Paginator(product_list, settings.PRODUCT_NUM_PER_PAGE)
    page = request.GET.get('page')
    paginated_product_list = paginator.get_page(page)
    return {'product_list': paginated_product_list}
