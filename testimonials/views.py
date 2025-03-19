from django.shortcuts import render
from .models import Testimonial

def testimonial_list(request):
    testimonials = Testimonial.objects.all().order_by('-created_at')  # Show latest reviews first
    return render(request, 'testimonials/testimonials.html', {'testimonials': testimonials})