from django.urls import path

from . import views
app_name = 'coin'

urlpatterns = [
 path('<slug:slug>/', views.module, name='module')
]

