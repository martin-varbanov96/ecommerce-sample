from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'categories'
urlpatterns = [
    url(r'^$', views.load_categories, name='index'),
    path('<int:category_id>/', views.category_details, name='category_details')
]
