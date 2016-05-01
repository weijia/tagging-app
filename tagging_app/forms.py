from django import forms
from django.contrib.contenttypes.models import ContentType

from tagging.models import TaggedItem


class TaggingForm(forms.ModelForm):
    tags = forms.CharField(max_length=512, required=True)
    object_id = forms.IntegerField()

    class Meta:
        model = TaggedItem
        exclude = ['tag']
