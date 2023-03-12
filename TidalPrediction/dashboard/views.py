from django.shortcuts import render
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

# a=get_siteinfo()
# print(a.to_dict("index"))
