from django.views.generic import TemplateView

class HomeStaticView(TemplateView):
    template_name = "index.html"
