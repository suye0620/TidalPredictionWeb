from django.shortcuts import render


# Create your views here.
def contact(request):
    # contact page
    return render(request, 'contact/contact.html')
