from django.urls import path
from . import views
#url paths
urlpatterns = [
    path('',views.index, name='index'),
    path('my_profile/',views.profile,name='profile'),
]