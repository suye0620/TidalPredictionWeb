from django.shortcuts import render
from .models import Valine

# Create your views here.
def contact(request):
    valine = Valine.objects.first()  # 取第一条数据
    # contact page
    context = {
        'valine':valine,
    }
    return render(request, 'contact/contact.html',context)
