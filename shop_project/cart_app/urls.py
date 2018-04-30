from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'cart_app'
urlpatterns = [
    url(r'^$', views.load_cart, name='index'),
    # path('<int:category_id>/', views.category_details, name='category_details')

]
