from django.contrib.contenttypes.models import ContentType
from django.template.defaulttags import register
from django.utils.safestring import mark_safe


@register.filter
def gen_tag_attr(obj):
    tag_name_list = []
    for tag in obj.tags:
        tag_name_list.append(tag.name)
    return mark_safe(' objectId="%d" tags="%s" contentType="%d"' % (obj.pk, ",".join(tag_name_list),
                     ContentType.objects.get_for_model(obj).pk))
