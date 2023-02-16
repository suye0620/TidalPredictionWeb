from django.shortcuts import render


# Create your views here.
def portfolio(request):
    # the portfolio of introduction pages
    return render(request, "introduce/portfolio.html")


def introduce(request):
    # 暂时充数的介绍页
    return render(request, "introduce/introduce.html")
