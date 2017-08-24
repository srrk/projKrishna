from django.conf.urls import url

from upload import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^update/$', views.update, name='update'),
        ]
