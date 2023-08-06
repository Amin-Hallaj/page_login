from django.urls import path
from . import views

urlpatterns = [

    path('',views.master_index, name='master_index'),
    path('operator/',views.operator_index, name='operator_index'),
    path('master/login/',views.master_login, name='master_login'),
    path('master/login/submit/',views.master_login_submit, name='master_login_submit'),
    path('master/logout/',views.master_logout, name='master_logout'),
    path('operator/login/submit/', views.operator_login_submit, name='operator_login_submit'),
    path('operator/member/registration/', views.member_registration, name='member_registration'),
    path('operator/member/registration/submit/', views.member_registration_submit, name='member_registration_submit'),

]



