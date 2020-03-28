from django.conf.urls import url
from . import views

urlpatterns = [
    #http://127.0.0.1:8000/v1/users
    url(r'^$',views.users),
url(r'^/(?P<username>\w{1,11})$', views.users),

]