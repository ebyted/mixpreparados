from django.shortcuts import render, redirect
from .forms import TestimonioForm
from .models import Testimonial

def testimonios_view(request):
    testimonios = Testimonial.objects.all().order_by('-created_at')

    if request.method == 'POST':
        form = TestimonioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('testimonials')
    else:
        form = TestimonioForm()

    return render(request, 'testimonials.html', {
        'form': form,
        'testimonios': testimonios
    })