from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^recent/', views.last3, name='last3'),
    url(r'^$', views.widget, name='widget'),
    url(r'^posts/(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^posts/new/$', views.new_post, name='new_post'),
    url(r'^posts/(?P<id>\d+)/edit$', views.edit_post, name='edit_post'),

]