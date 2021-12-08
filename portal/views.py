from django.shortcuts import render
from django.views.generic import TemplateView, ListView
import requests
import pprint
import json


from . import maker_logo



# Create your views here.


def fetchAPI(make, model, min_year, max_year):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'

    header = {
        'User-Agent': user_agent,
        "content-type": "application/json"
    }

    url = f'https://www.carqueryapi.com/api/0.3/?callback=?&cmd=getTrims&make={make}&model={model}&min_year={min_year}&max_year={max_year}'
    print(url)
    response = requests.get(url, headers=header)

    # str -> dict
    dict = json.loads(response.text[2:-2])["Trims"]

    return dict


class IndexView(TemplateView):

    template_name = "index.html"

    def get(self, request):
        logos = maker_logo.makers

        context = { "logos": logos }
        return render(request, self.template_name, context)

    def post(self, request):
        context = { "postm": "postメソッド" }
        return render(request, self.template_name, context)



class ModelListView(TemplateView):

    template_name = 'portal/modelList.html'

    def get(self, request, maker):

        fetchModels = fetchAPI(maker, "", 2021, 2021)

        setModels = set()
        for model in fetchModels:
            setModels.add(model["model_name"])

        makerDict = {
            'name': maker,
            'logo': maker_logo.makers[maker]
        }

        context = {
            "maker": makerDict,
            "models":setModels
        }
        return render(request, self.template_name, context)



class ResultView(TemplateView):
    template_name = "portal/resultList.html"

    def get(self, request, maker, model):

        fetchData = fetchAPI(maker, model, 1886, 2021)

        makerDict = {
            'name': maker,
            'logo': maker_logo.makers[maker]
        }


        context = {
            "maker": makerDict,
            "data": fetchData
        }
        return render(request, self.template_name, context)
