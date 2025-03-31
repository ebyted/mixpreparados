from django.views.generic import TemplateView

class TestimonialsStaticView(TemplateView):
    template_name = 'static_templates/testimonials.html'