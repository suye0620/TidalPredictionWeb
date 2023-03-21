from django.shortcuts import render
from django.http import JsonResponse
from pandas import read_csv
from pathlib import Path
from pickle import load
from re import split
from numpy import array, round

current_dir = Path(__file__).resolve().parent


def get_siteinfo(filepath: str = current_dir / "data/SiteInfo.csv"):
    df_siteinfo = read_csv(filepath)
    return df_siteinfo


def get_examples_top50(filepath: str = current_dir / "data/examples.csv"):
    df_examples = read_csv(filepath, encoding='utf-8-sig')
    # 随机抽取50行用于预测展示
    return df_examples.sample(n=50, random_state=666)


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
    df_examples = get_examples_top50()
    context = {
        'siteinfo': df_siteinfo.to_dict("index"),
        'examples': df_examples.to_dict("index"),
        'examples_columns': list(df_examples.columns),
    }
    return render(request, 'dashboard/dashboard.html', context)


def line_graph(request):
    site_num = int(request.GET.get("choose-site"))
    # site_series = read_csv(get_siteseries(site_num), encoding='utf-8-sig', index_col=['time'], parse_dates=["time"], )
    site_series = read_csv(get_siteseries(site_num), encoding='utf-8-sig', index_col=['time'], )
    data = site_series.to_dict('dict')
    return JsonResponse(data)


def tidal_prediction(request):
    input_seq = str(request.GET.get("input-seq")).strip('\t\n ')
    model = load(open(file=(current_dir / "model/TidalPredictionModel.pkl"), mode='rb'))
    list_input_seq = split(r"\t|,", input_seq)
    arr_input_seq = array([float(i) for i in list_input_seq])
    prediction_result = model.predict(arr_input_seq.reshape(-1, 10))

    data = {
        # 保留三位
        'prediction_result': round(prediction_result[0], 3)
    }
    return JsonResponse(data)
