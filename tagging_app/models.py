from django.contrib.auth.models import User
from django.db import models

from tagging.models import TaggedItem
from django.utils.translation import ugettext_lazy as _


class TagInfo(models.Model):
    """
    Holds the relationship between a tag and the item being tagged.
    """
    tagged_item = models.ForeignKey(TaggedItem, verbose_name=_('tagged_item'), related_name='tagged_item')
    user = models.ForeignKey(User, verbose_name=_('tagging_user'), related_name='tagging_user')
    tag_app = models.CharField(_(u"Tag creator"), help_text=_(u"Tag creator"), max_length=50, null=True, blank=True)
