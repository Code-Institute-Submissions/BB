from django.conf.urls import url
from views import about, index
from blog.views import post_list
from blog.views import widget

urlpatterns = [
    url(r'^about/', about, name='about'),
    url(r'^$', post_list, name='index'),
    url(r'^widget/', widget,name='index' )

]