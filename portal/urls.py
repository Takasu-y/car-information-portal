from django.urls import path
from .views import IndexView, ModelListView, fetchAPI

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("modelList/make/", ModelListView.as_view(), name='modelList'),
    path("fetchAPI/", fetchAPI, name="fetchAPI")
]
