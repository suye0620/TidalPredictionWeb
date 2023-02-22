from django.shortcuts import render
from .models import Introduction

# Create your views here.
def portfolio(request):
    # the portfolio of introduction pages
    if request.method == 'GET':
        # get the recommended introduction
        top_introduction = Introduction.objects.filter(is_recommend=1)

        method_flag = True

        context = {
            'top_introduction':top_introduction,
            'method_flag':method_flag
        }
        return render(request, "introduce/portfolio.html",context)
    else:
        method_flag = False
        context = {
            'method_flag': method_flag
        }
        return render(request,"introduce/portfolio.html",context)


def introduction_detail(request,id):
    # 暂时充数的介绍页
    return render(request, "introduce/introduce.html")
