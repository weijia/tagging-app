from django.contrib.contenttypes.models import ContentType
from django.template.defaulttags import register
from django.utils.safestring import mark_safe

from tagging_app.tagging_app_utils import generate_html_attributes


@register.filter
def gen_tag_attr(obj):
    return mark_safe(generate_html_attributes(obj))
