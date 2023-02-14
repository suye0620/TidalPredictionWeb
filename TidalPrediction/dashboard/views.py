from django.shortcuts import render


# Create your views here.
def dashboard(request):
    # dashboard page
    return render(request, 'dashboard/dashboard.html')
