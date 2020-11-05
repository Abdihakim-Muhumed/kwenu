from django.urls import path
from . import views
#url paths
urlpatterns = [
    path('',views.index, name='index'),
    path('my_profile/',views.profile,name='profile'),
    path('edit/',views.edit_profile,name='edit-profile'),
    path('new/business/',views.new_business,name='new-business'),
    path('business/view/<business_id>',views.view_business,name='view-business'),
    path('business/search/',views.search_results,name='search'),
    path('join/hood/<hood_id>', views.join_hood, name='join-hood'),
    path('leave/hood/<hood_id>', views.leave_hood, name='leave-hood'),
    path('home/<home_id>', views.home, name='home'),
]