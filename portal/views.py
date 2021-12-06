from json.decoder import JSONDecodeError
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
import requests
import pprint
import json



# Create your views here.


def fetchAPI(request):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'
    # url = ' https://www.carqueryapi.com/api/0.3/?callback=?&cmd=getTrims&make=Ford&year=2005'
    url = 'https://www.carqueryapi.com/api/0.3/?callback=?&cmd=getMakes&year=2020'

    header = {
        'User-Agent': user_agent,
        "content-type": "application/json"
    }




    response = requests.get(url, headers=header)

    # str -> dict
    models = json.loads(response.text[2:-2])['Makes']

    # 集合に変換
    setMakers = set()
    for model in models:
        setMakers.add(model["make_display"])


    context = {
        'models': setMakers
    }
    return render(request, 'index.html', context)


class IndexView(TemplateView):

    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        context = { "getm": "getメソッド" }
        return render(request, self.template_name, context)

    def post(self, request):
        context = { "postm": "postメソッド" }
        return render(request, self.template_name, context)



class ModelListView(TemplateView):

    template_name = 'portal/modelList.html'
    context_object_name = 'modelList'
