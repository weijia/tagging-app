from django.conf.urls import patterns, include, url
from django.views.decorators.csrf import csrf_exempt

from djangoautoconf.django_rest_framework_utils.serializer_generator import get_create_api_class, ApiClassGenerator, \
    ModelSerializerWithUser
from tagging.models import TaggedItem, Tag
from tagging_app.models import TagInfo


# class TaggedItemWithUserSerializer(ModelSerializer):
#     class Meta:
#         model = TagInfo
#
#     # def save(self, **kwargs):
#     #     user = None
#     #     if "request" in self.context and self.context['request']:
#     #         user = self.context['request'].user
#     #     return super(ModelSerializer, self).save(user=user, **kwargs)
#
#
# class TagInfoApi(ListCreateAPIView):
#     queryset = TagInfo.objects.all()
#     serializer_class = TaggedItemWithUserSerializer
from tagging_app.views import TaggingFormView

urlpatterns = patterns('',
                       url(r'^tagged_item_creation/$', get_create_api_class(TaggedItem).as_view()),
                       url(r'^tag_creation/$', get_create_api_class(Tag).as_view()),
                       url(r'^tagged_item_with_user/$', ApiClassGenerator(
                           serializer_parent=[ModelSerializerWithUser]).get_api_class(TagInfo).as_view()),
                       # url(r'^tagged_item_with_user/$', TagInfoApi.as_view()),
                       url(r'^set_tags/$', csrf_exempt(TaggingFormView.as_view()))
                       )
