from django.conf.urls import url
from ClassOutside import views

urlpatterns= [
    url(r'^$', views.classoutside, name='classoutside'),
]
