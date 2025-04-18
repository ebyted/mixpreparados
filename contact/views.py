from django.shortcuts import render, redirect
from .models import ContactMessage
from contact.forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')  # Redirect to a thank-you page
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact.html', {'form': form})
