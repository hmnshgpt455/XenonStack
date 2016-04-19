from django.conf.urls import url
from .views import SystemMetricesView,PerProcessMetricesView,FileSystemMetricesView

urlpatterns = [
    url(r'^system$',SystemMetricesView),
    url(r'^process$',PerProcessMetricesView),
    url(r'^filesystem$',FileSystemMetricesView),
]