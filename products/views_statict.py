from django.views.generic import TemplateView

class ProductsStaticView(TemplateView):
    template_name = "products.html"