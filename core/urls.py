from django.contrib.auth import views as auth_views

from django.urls import path

from . import views

#from .form import LoginForm

app_name = 'core'



urlpatterns = [
    path('' , views.index , name='index'), 
    path('coin/' , views.coin , name='coin'),
    path('tokenScreen/' , views.tokenScreen , name='tokenScreen'),
    path('calendar/' , views.EventCalendarView.as_view(), name='event-calendar'),
    path('google_login/', views.google_login, name='google_login'),

    
]

'''
    

    path('signup/', views.signup , name='signup'),
    path('login/', views.login , name='login'),
    path('editinfo',editinfo,name='editinfo'),
    path('profile/<str:username>',views.userprofile, name='profile'), '''