from django.conf.urls import url
from views import about, index, Products
from blog.views import post_list
from blog.views import widget
from products.views import all_products

urlpatterns = [
    url(r'^about/', about, name='about'),
    url(r'^$', post_list, name='index'),
    url(r'^products/', all_products, name='products'),

]