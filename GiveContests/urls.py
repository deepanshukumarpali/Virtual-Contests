from django.urls import path
from . import views


urlpatterns= [
    path('',views.home,name='home'),
    path('virtual',views.virtual,name='virtual')

]