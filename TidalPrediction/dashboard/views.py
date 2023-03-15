from django.shortcuts import render
from django.http import JsonResponse
from pandas import read_csv
from pathlib import Path

current_dir = Path(__file__).resolve().parent


def get_siteinfo(filepath: str = current_dir / "data/SiteInfo.csv"):
    df_siteinfo = read_csv(filepath)
    return df_siteinfo


def get_siteseries(site_num):
    dict_num2data = {
        0: "IrishNationalTideGaugeNetwork_Howth Harbour2017.csv",
        1: "IrishNationalTideGaugeNetwork_Ballycotton Harbour2017.csv",
        2: "IrishNationalTideGaugeNetwork_Ballyglass Harbour2017.csv",
        3: "IrishNationalTideGaugeNetwork_Castletownbere Port2017.csv",
        4: "IrishNationalTideGaugeNetwork_Galway Port2017.csv",
    }
    return current_dir / ("data/" + dict_num2data.get(site_num))


# Create your views here.
def dashboard(request):
    # dashboard page
    df_siteinfo = get_siteinfo()
    context = {
        'siteinfo': df_siteinfo.to_dict("index")
    }
    return render(request, 'dashboard/dashboard.html', context)


def line_graph(request):
    site_num = int(request.GET.get("choose-site"))
    # site_series = read_csv(get_siteseries(site_num), encoding='utf-8-sig', index_col=['time'], parse_dates=["time"], )
    site_series = read_csv(get_siteseries(site_num), encoding='utf-8-sig', index_col=['time'], )
    data = site_series.to_dict('dict')
    return JsonResponse(data)


# S1 = read_csv(get_siteseries(4), encoding='utf-8-sig',)
# S1['time'] = S1['time'].map(lambda x : x[:-6])
# S1.to_csv(get_siteseries(4), encoding='utf-8-sig',index=False)
