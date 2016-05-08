from django.views.generic import TemplateView

from tagging_app.forms import TaggingForm


class TaggingFormView(TemplateView):
    form_class = TaggingForm
    template_name = "tagging_app/basic_form_view.html"

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TaggingFormView, self).get_context_data(**kwargs)

        if self.request.POST:
            form = TaggingForm(self.request.POST)
            if form.is_valid():
                m = form.cleaned_data["content_type"].model_class()
                obj = m.objects.get(pk=form.cleaned_data["object_id"])
                obj.tags = form.cleaned_data["tags"]
                obj.save()
                context["form"] = form
            else:
                context["form"] = form
        else:
            context["form"] = TaggingForm()
        return context
