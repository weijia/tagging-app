from django.contrib.contenttypes.models import ContentType


def generate_html_attributes(obj):
    tag_str = get_tag_str(obj)
    return ' objectId="%d" tags="%s" contentType="%d"' % (obj.pk, tag_str,
                                                          ContentType.objects.get_for_model(obj).pk)


def get_tag_str(obj):
    tag_name_list = get_tags(obj)
    tag_str = ",".join(tag_name_list)
    return tag_str


def get_tags(obj):
    tag_name_list = []
    for tag in obj.tags:
        tag_name_list.append(tag.name)
    return tag_name_list
