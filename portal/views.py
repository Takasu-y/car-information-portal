from datetime import datetime
from os import mkdir
from django import forms
from django.shortcuts import render
from django.views.generic import TemplateView
import requests
import json
import datetime

from . import maker_logo
from . import forms



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

    def get(self, request):
        logos = maker_logo.makers
        form = forms.SearchFrom()

        context = {
            "logos": logos,
            "form": form
        }
        return render(request, "index.html", context)

    def post(self, request):
        maker = request.POST.get("maker")
        model = request.POST.get("model")
        maxYear = request.POST.get("maxYear")
        minYear = request.POST.get("minYear")
        if maxYear == "Any":
            maxYear = ""

        form = forms.SearchFrom(initial={
            "maker":maker,
            "model": model,
            "minYear": minYear,
            "maxYear": maxYear
        })

        fetchData = fetchAPI(maker, model, minYear, maxYear)

        context = {
            "form": form,
            "data": fetchData
        }
        return render(request, "portal/resultList.html", context)



class ModelListView(TemplateView):

    template_name = 'portal/modelList.html'

    def get(self, request, maker):

        currentYear = datetime.datetime.now().year
        fetchModels = fetchAPI(maker, "", currentYear, currentYear)

        setModels = set()
        for model in fetchModels:
            setModels.add(model["model_name"])

        print(setModels)

        makerDict = {
            'name': maker,
            'logo': maker_logo.makers[maker]
        }

        form = forms.SearchFrom(initial={
            "maker": maker,
            "model": "",
            "minYear": currentYear,
            "maxYear": currentYear
        })

        context = {
            "maker": makerDict,
            "models":setModels,
            "form": form
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

        form = forms.SearchFrom(initial={
            "maker": maker,
            "model": model,
            "minYear": 1900,
            "maxYear": 2021
        })

        context = {
            "maker": makerDict,
            "data": fetchData,
            "form": form
        }
        return render(request, self.template_name, context)
