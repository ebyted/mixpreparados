from django.views.generic import TemplateView

class ContactStaticView(TemplateView):
    template_name = "contact.html"