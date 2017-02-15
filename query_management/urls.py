from django.conf.urls import url
from query_management import views

urlpatterns = [
    url(r'^query/$', views.RequestQuery),
]
