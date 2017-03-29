from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^posts/(?P<id>\d+)/$', views.post_detail, name='post_detail')
]