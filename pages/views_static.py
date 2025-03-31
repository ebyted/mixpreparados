from django.views.generic import TemplateView

class HomeStaticView(TemplateView):
    template_name = "static_templates/index.html"

class ProductsStaticView(TemplateView):
    template_name = "static_templates/products.html"

class AboutStaticView(TemplateView):
    template_name = "static_templates/about.html"

class TestimonialsStaticView(TemplateView):
    template_name = "static_templates/testimonials.html"

class ContactStaticView(TemplateView):
    template_name = "static_templates/contact.html"