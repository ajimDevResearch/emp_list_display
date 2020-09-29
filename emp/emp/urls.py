from django.conf.urls import url
from django.contrib import admin
from empApp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^emp_url/', views.emp_view),
]

