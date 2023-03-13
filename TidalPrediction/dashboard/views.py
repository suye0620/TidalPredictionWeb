from django.shortcuts import render
from django.http import JsonResponse
from pandas import read_csv
from pathlib import Path

current_dir = Path(__file__).resolve().parent


def get_siteinfo(filepath: str = current_dir / "data/SiteInfo.csv"):
    df_siteinfo = read_csv(filepath)
    return df_siteinfo


# Create your views here.
def dashboard(request):
    # dashboard page
    df_siteinfo = get_siteinfo()
    context = {
        'siteinfo': df_siteinfo.to_dict("index")
    }
    return render(request, 'dashboard/dashboard.html', context)


def line_graph(request):
    site_num = request.GET.get("choose-site")
    data = {'name': 'suye', 'age': site_num}
    return JsonResponse(data)
