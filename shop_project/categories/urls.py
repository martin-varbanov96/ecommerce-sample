from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'categories'
urlpatterns = [
    url(r'^$', views.load_categories, name='index'),
    path('<int:category_id>/', views.category_details, name='category_details'),

    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
