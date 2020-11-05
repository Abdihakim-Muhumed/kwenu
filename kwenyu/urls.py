from django.urls import path
from . import views
#url paths
urlpatterns = [
    path('',views.index, name='index'),
    path('my_profile/',views.profile,name='profile'),
    path('edit/',views.edit_profile,name='edit-profile'),
    path('new/business/',views.new_business,name='new-business'),
    path('business/view/<business_id>',views.view_business,name='view-business'),
]