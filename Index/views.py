# views.py
from django.shortcuts import render, redirect
from .models import Contact
from django.http import HttpResponse

def about(request):
    return render(request, 'index.html', {'section': 'about'})

def projects(request):
    return render(request, 'index.html', {'section': 'projects'})

def education(request):
    return render(request, 'index.html', {'section': 'education'})

def services(request):
    return render(request, 'index.html', {'section': 'services'})

def contact_view(request):
    if request.method == 'POST':
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        
        # Create an instance of the Contact model
        obj = Contact(
            fname=fname,
            lname=lname,
            email=email,
            subject=subject,
            message=message
        )

        # Save the object to the database
        obj.save()

        # Redirect to a success page or update the logic as needed
        return redirect('about')  # Change 'about' to the appropriate URL name

    return render(request, 'index.html', {'section': 'contact'})
