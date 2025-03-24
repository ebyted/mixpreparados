from django.views.generic import TemplateView

class AboutStaticView(TemplateView):
    template_name = "about.html"
