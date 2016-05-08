from django.template.defaulttags import register
from django.utils.safestring import mark_safe


@register.filter
def gen_tag_attr(obj):
    tag_name_list = []
    for tag in obj.tags:
        tag_name_list.append(tag.name)
    return mark_safe(' objectId="%d" tags="%s"' % (obj.pk, ",".join(tag_name_list)))
