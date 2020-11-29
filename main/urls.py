from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('process', views.process),
    path('<first_name>/<last_name>/<int:age>/<email>', views.results)

]