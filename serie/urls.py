from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.search_page, name="search"),
    url(r'^results', views.results_page,name="results")
]