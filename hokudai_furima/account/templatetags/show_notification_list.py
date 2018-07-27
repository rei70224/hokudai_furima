from django import template

register = template.Library()

@register.inclusion_tag('account/_notification_list.html')
def show_notification_list(notification_list):
    return {'notification_list': notification_list}
