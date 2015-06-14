
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers
from cep import views

router = routers.DefaultRouter()
router.register(r'cep', views.CepViewSet)

urlpatterns = [
    url(r'api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
