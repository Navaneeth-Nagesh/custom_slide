from django.conf.urls import include, url
from django.contrib import admin
from custom_slide import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
]
