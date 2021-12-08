from django.urls import path
from .views import IndexView, ModelListView, ResultView

app_name='portal'

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("modelList/make/<str:maker>", ModelListView.as_view(), name='modelList'),
    path("result/<str:maker>/<str:model>/", ResultView.as_view(), name='result'),
]
