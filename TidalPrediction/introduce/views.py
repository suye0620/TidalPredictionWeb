from django.shortcuts import render


# Create your views here.
def portfolio(request):
    # the portfolio of introduction pages
    return render(request, "introduce/portfolio.html")
